"""
Firebase Firestore Chat Service

Handles chat room creation, message sending, and real-time listeners.
"""

from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from uuid import uuid4


class ChatService:
    """Service for managing chat rooms and messages via Firebase Firestore."""

    def __init__(self):
        self._db = None
        self._init_firebase()

    def _init_firebase(self):
        """Initialize Firebase Admin SDK if configured."""
        try:
            import firebase_admin
            from firebase_admin import credentials, firestore

            if not firebase_admin._apps:
                cred = credentials.ApplicationDefault()
                firebase_admin.initialize_app(cred)

            self._db = firestore.client()
        except Exception:
            self._db = None

    def _get_db(self):
        if self._db is None:
            raise RuntimeError("Firebase not initialized")
        return self._db

    async def create_chat(
        self,
        user_id_1: str,
        user_id_2: str,
        item_id: Optional[str] = None,
        item_title: Optional[str] = None,
    ) -> str:
        db = self._get_db()
        chat_id = str(uuid4())

        chat_data = {
            "participants": [user_id_1, user_id_2],
            "item_id": item_id,
            "item_title": item_title,
            "created_at": firestore_timestamp(),
            "last_message": None,
        }

        db.collection("chats").document(chat_id).set(chat_data)
        return chat_id

    async def get_or_create_chat(
        self,
        user_id_1: str,
        user_id_2: str,
        item_id: Optional[str] = None,
    ) -> str:
        db = self._get_db()
        chats_ref = db.collection("chats")
        query = chats_ref.where("participants", "array_contains", user_id_1)
        docs = query.stream()

        for doc in docs:
            data = doc.to_dict()
            if user_id_2 in data.get("participants", []):
                if item_id is None or data.get("item_id") == item_id:
                    return doc.id

        return await self.create_chat(user_id_1, user_id_2, item_id)

    async def send_message(
        self,
        chat_id: str,
        sender_id: str,
        text: str,
        image_url: Optional[str] = None,
    ) -> str:
        db = self._get_db()
        msg_id = str(uuid4())
        now = firestore_timestamp()

        message_data = {
            "sender_id": sender_id,
            "text": text,
            "image_url": image_url,
            "sent_at": now,
            "read": False,
        }

        db.collection("chats").document(chat_id).collection("messages").document(msg_id).set(
            message_data
        )
        db.collection("chats").document(chat_id).update(
            {"last_message": {"text": text[:100], "sender_id": sender_id, "sent_at": now}}
        )

        return msg_id

    async def get_messages(
        self,
        chat_id: str,
        limit: int = 50,
        before_timestamp=None,
    ) -> List[Dict[str, Any]]:
        db = self._get_db()
        messages_ref = db.collection("chats").document(chat_id).collection("messages")
        query = messages_ref.order_by("sent_at", direction="DESCENDING").limit(limit)

        if before_timestamp:
            query = query.where("sent_at", "<", before_timestamp)

        docs = query.stream()
        messages = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            data["sent_at"] = (
                data["sent_at"].isoformat()
                if hasattr(data["sent_at"], "isoformat")
                else str(data["sent_at"])
            )
            messages.append(data)

        return messages

    async def mark_as_read(self, chat_id: str, message_id: str):
        db = self._get_db()
        db.collection("chats").document(chat_id).collection("messages").document(message_id).update(
            {"read": True}
        )

    async def get_user_chats(self, user_id: str) -> List[Dict[str, Any]]:
        db = self._get_db()
        chats_ref = db.collection("chats")
        query = chats_ref.where("participants", "array_contains", user_id)
        docs = query.stream()

        chats = []
        for doc in docs:
            data = doc.to_dict()
            if data.get("last_message"):
                data["id"] = doc.id
                lm = data["last_message"]
                if hasattr(lm.get("sent_at"), "isoformat"):
                    lm["sent_at"] = lm["sent_at"].isoformat()
                chats.append(data)

        chats.sort(
            key=lambda c: c.get("last_message", {}).get("sent_at", ""),
            reverse=True,
        )
        return chats

    async def get_unread_count(self, user_id: str, chat_id: str) -> int:
        db = self._get_db()
        messages_ref = db.collection("chats").document(chat_id).collection("messages")
        query = messages_ref.where("read", "==", False).where("sender_id", "!=", user_id)
        docs = query.stream()
        return sum(1 for _ in docs)

    async def get_user_rooms(self, user_id: str) -> List[Dict[str, Any]]:
        """Return chat rooms in the format expected by the API."""
        chats = await self.get_user_chats(user_id)
        rooms = []
        for chat in chats:
            lm = chat.get("last_message")
            rooms.append(
                {
                    "id": chat.get("id", ""),
                    "participants": chat.get("participants", []),
                    "item_id": chat.get("item_id"),
                    "last_message": (
                        {
                            "text": lm.get("text", "") if lm else "",
                            "sender_id": lm.get("sender_id", "") if lm else "",
                            "sent_at": lm.get("sent_at", "") if lm else "",
                        }
                        if lm
                        else None
                    ),
                    "created_at": chat.get("created_at", ""),
                }
            )
        return rooms

    async def create_room(
        self,
        participants: List[str],
        item_id: Optional[str] = None,
        initial_message: Optional[str] = None,
        sender_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Create a new chat room and optionally send the first message."""
        if len(participants) < 2:
            raise ValueError("At least 2 participants required")

        db = self._get_db()
        room_id = str(uuid4())
        now = firestore_timestamp()

        room_data = {
            "participants": participants,
            "item_id": item_id,
            "created_at": now,
            "last_message": None,
        }
        db.collection("chats").document(room_id).set(room_data)

        if initial_message and sender_id:
            msg_id = str(uuid4())
            message_data = {
                "sender_id": sender_id,
                "text": initial_message,
                "sent_at": now,
                "read": False,
            }
            db.collection("chats").document(room_id).collection("messages").document(msg_id).set(
                message_data
            )
            db.collection("chats").document(room_id).update(
                {
                    "last_message": {
                        "text": initial_message[:100],
                        "sender_id": sender_id,
                        "sent_at": now,
                    }
                }
            )

        return {
            "id": room_id,
            "participants": participants,
            "item_id": item_id,
            "last_message": (
                {
                    "text": initial_message[:100] if initial_message else "",
                    "sender_id": sender_id or "",
                    "sent_at": "",
                }
                if initial_message
                else None
            ),
            "created_at": "",
        }

    async def get_room(self, room_id: str) -> Optional[Dict[str, Any]]:
        """Get a single chat room by ID."""
        db = self._get_db()
        doc = db.collection("chats").document(room_id).get()
        if not doc.exists:
            return None
        data = doc.to_dict()
        data["id"] = doc.id
        lm = data.get("last_message")
        if lm and hasattr(lm.get("sent_at"), "isoformat"):
            lm["sent_at"] = lm["sent_at"].isoformat()
        return data


def firestore_timestamp():
    """Get current timestamp in Firestore-compatible format."""
    try:
        from google.cloud import firestore

        return firestore.SERVER_TIMESTAMP
    except ImportError:
        return datetime.now(timezone.utc).isoformat()


chat_service = ChatService()
