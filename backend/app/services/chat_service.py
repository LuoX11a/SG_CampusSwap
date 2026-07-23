"""
PostgreSQL Chat Service

Handles chat room creation, message sending, and message retrieval.
Replaces the Firebase Firestore implementation.
"""

import uuid
from typing import Optional, List, Dict, Any

from sqlalchemy import select, update, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.models.chat import ChatRoom, ChatMessage


class ChatService:
    """Service for managing chat rooms and messages via PostgreSQL."""

    async def _get_session(self) -> AsyncSession:
        factory = get_async_session()
        return factory()

    # ── Room operations ──────────────────────────────────────

    async def create_room(
        self,
        participants: List[str],
        item_id: Optional[str] = None,
        initial_message: Optional[str] = None,
        sender_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        if len(participants) < 2:
            raise ValueError("At least 2 participants required")

        async with await self._get_session() as db:
            room = ChatRoom(
                id=uuid.uuid4(),
                participants=participants,
                item_id=uuid.UUID(item_id) if item_id else None,
            )
            db.add(room)

            if initial_message and sender_id:
                msg = ChatMessage(
                    id=uuid.uuid4(),
                    room_id=room.id,
                    sender_id=uuid.UUID(sender_id),
                    text=initial_message,
                )
                db.add(msg)
                room.last_message_at = msg.sent_at

            await db.commit()

        return {
            "id": str(room.id),
            "participants": participants,
            "item_id": item_id,
            "last_message": (
                {
                    "text": initial_message[:100] if initial_message else "",
                    "sender_id": sender_id or "",
                    "sent_at": msg.sent_at.isoformat() if initial_message and sender_id else "",
                }
                if initial_message
                else None
            ),
            "created_at": room.created_at.isoformat(),
        }

    async def get_room(self, room_id: str) -> Optional[Dict[str, Any]]:
        async with await self._get_session() as db:
            result = await db.execute(select(ChatRoom).where(ChatRoom.id == room_id))
            room = result.scalar_one_or_none()
            if not room:
                return None
            return self._room_to_dict(room)

    async def get_user_rooms(self, user_id: str) -> List[Dict[str, Any]]:
        async with await self._get_session() as db:
            result = await db.execute(
                select(ChatRoom)
                .where(ChatRoom.participants.contains([user_id]))
                .order_by(desc(ChatRoom.last_message_at))
            )
            rooms = result.scalars().all()
            return [self._room_to_dict(r) for r in rooms]

    def _room_to_dict(self, room: ChatRoom) -> Dict[str, Any]:
        lm = None
        if room.last_message_at:
            lm = {
                "text": "",
                "sender_id": "",
                "sent_at": room.last_message_at.isoformat(),
            }
        return {
            "id": str(room.id),
            "participants": room.participants,
            "item_id": str(room.item_id) if room.item_id else None,
            "last_message": lm,
            "created_at": room.created_at.isoformat() if room.created_at else "",
        }

    # ── Message operations ───────────────────────────────────

    async def send_message(
        self,
        room_id: str,
        sender_id: str,
        text: str,
        image_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        async with await self._get_session() as db:
            msg = ChatMessage(
                id=uuid.uuid4(),
                room_id=uuid.UUID(room_id),
                sender_id=uuid.UUID(sender_id),
                text=text,
            )
            db.add(msg)

            # Update room's last_message_at
            await db.execute(
                update(ChatRoom).where(ChatRoom.id == room_id).values(last_message_at=msg.sent_at)
            )
            await db.commit()

        return {
            "id": str(msg.id),
            "sender_id": sender_id,
            "text": text,
            "image_url": image_url,
            "sent_at": msg.sent_at.isoformat(),
            "read": False,
        }

    async def get_messages(
        self,
        room_id: str,
        limit: int = 50,
        before_timestamp=None,
    ) -> List[Dict[str, Any]]:
        async with await self._get_session() as db:
            q = (
                select(ChatMessage)
                .where(ChatMessage.room_id == room_id)
                .order_by(desc(ChatMessage.sent_at))
                .limit(limit)
            )
            result = await db.execute(q)
            messages = result.scalars().all()
            # Return in chronological order (oldest first)
            messages.reverse()
            return [
                {
                    "id": str(m.id),
                    "sender_id": str(m.sender_id),
                    "text": m.text,
                    "sent_at": m.sent_at.isoformat(),
                    "read": m.read,
                }
                for m in messages
            ]

    async def mark_as_read(self, room_id: str, message_id: str):
        async with await self._get_session() as db:
            await db.execute(
                update(ChatMessage).where(ChatMessage.id == message_id).values(read=True)
            )
            await db.commit()

    async def get_unread_count(self, user_id: str, room_id: str) -> int:
        async with await self._get_session() as db:
            result = await db.execute(
                select(ChatMessage)
                .where(ChatMessage.room_id == room_id)
                .where(~ChatMessage.read)
                .where(ChatMessage.sender_id != user_id)
            )
            return len(result.scalars().all())

    # ── Compatibility methods (match old Firebase interface) ──

    async def get_or_create_chat(
        self,
        user_id_1: str,
        user_id_2: str,
        item_id: Optional[str] = None,
    ) -> str:
        async with await self._get_session() as db:
            # Check if a room already exists between these two users
            result = await db.execute(
                select(ChatRoom).where(ChatRoom.participants.contains([user_id_1]))
            )
            for room in result.scalars().all():
                if user_id_2 in room.participants:
                    return str(room.id)

        # Create a new room
        return (
            await self.create_room(
                participants=[user_id_1, user_id_2],
                item_id=item_id,
            )
        )["id"]

    async def create_chat(
        self,
        user_id_1: str,
        user_id_2: str,
        item_id: Optional[str] = None,
        item_title: Optional[str] = None,
    ) -> str:
        return await self.get_or_create_chat(user_id_1, user_id_2, item_id)


chat_service = ChatService()
