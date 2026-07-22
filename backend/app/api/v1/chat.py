"""
Chat API Routes (Firebase Firestore)

GET    /api/v1/chat/rooms              — List my chat rooms
POST   /api/v1/chat/rooms              — Create a new chat room
GET    /api/v1/chat/rooms/{room_id}    — Get chat room details
GET    /api/v1/chat/rooms/{room_id}/messages — Get messages for a room
POST   /api/v1/chat/rooms/{room_id}/messages — Send a message
"""

from typing import Optional, List
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.models.item import Item
from app.api.v1.auth import get_current_user
from app.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()


# ─── Schemas ───────────────────────────────────────────────────

class CreateRoomRequest(BaseModel):
    participant_id: str
    item_id: Optional[str] = None
    initial_message: Optional[str] = Field(None, max_length=500)


class SendMessageRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=500)


class MessageResponse(BaseModel):
    id: str
    sender_id: str
    text: str
    sent_at: str


class RoomResponse(BaseModel):
    id: str
    participants: List[str]
    item_id: Optional[str] = None
    last_message: Optional[dict] = None
    created_at: str


class RoomListResponse(BaseModel):
    rooms: List[RoomResponse]


class MessageListResponse(BaseModel):
    messages: List[MessageResponse]


# ─── Routes ────────────────────────────────────────────────────

@router.get("/rooms", response_model=RoomListResponse)
async def list_my_rooms(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """List chat rooms for the current user."""
    try:
        rooms = await chat_service.get_user_rooms(str(current_user.id))
        return {"rooms": rooms}
    except Exception:
        # Firebase not configured — return empty list gracefully
        return {"rooms": []}


@router.post("/rooms", status_code=status.HTTP_201_CREATED, response_model=RoomResponse)
async def create_room(
    req: CreateRoomRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Create a new chat room with another user."""
    if req.participant_id == str(current_user.id):
        raise HTTPException(status_code=400, detail="Cannot chat with yourself")

    # Verify participant exists
    result = await db.execute(select(User).where(User.id == req.participant_id))
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Participant not found")

    # Verify item exists if provided
    if req.item_id:
        result = await db.execute(select(Item).where(Item.id == req.item_id))
        if not result.scalar_one_or_none():
            raise HTTPException(status_code=404, detail="Item not found")

    try:
        room = await chat_service.create_room(
            participants=[str(current_user.id), req.participant_id],
            item_id=req.item_id,
            initial_message=req.initial_message,
            sender_id=str(current_user.id),
        )
        return room
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Chat service unavailable: {str(e)}")


@router.get("/rooms/{room_id}", response_model=RoomResponse)
async def get_room(
    room_id: str,
    current_user: User = Depends(get_current_user),
):
    """Get details of a chat room."""
    try:
        room = await chat_service.get_room(room_id)
        if not room:
            raise HTTPException(status_code=404, detail="Room not found")
        if str(current_user.id) not in room.get("participants", []):
            raise HTTPException(status_code=403, detail="Not a participant of this room")
        return room
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Chat service unavailable: {str(e)}")


@router.get("/rooms/{room_id}/messages", response_model=MessageListResponse)
async def get_messages(
    room_id: str,
    current_user: User = Depends(get_current_user),
    limit: int = Query(50, ge=1, le=100),
):
    """Get messages for a chat room."""
    try:
        room = await chat_service.get_room(room_id)
        if not room:
            raise HTTPException(status_code=404, detail="Room not found")
        if str(current_user.id) not in room.get("participants", []):
            raise HTTPException(status_code=403, detail="Not a participant of this room")

        messages = await chat_service.get_messages(room_id, limit=limit)
        return {"messages": messages}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Chat service unavailable: {str(e)}")


@router.post("/rooms/{room_id}/messages", status_code=status.HTTP_201_CREATED, response_model=MessageResponse)
async def send_message(
    room_id: str,
    req: SendMessageRequest,
    current_user: User = Depends(get_current_user),
):
    """Send a message to a chat room."""
    try:
        room = await chat_service.get_room(room_id)
        if not room:
            raise HTTPException(status_code=404, detail="Room not found")
        if str(current_user.id) not in room.get("participants", []):
            raise HTTPException(status_code=403, detail="Not a participant of this room")

        message = await chat_service.send_message(
            room_id=room_id,
            sender_id=str(current_user.id),
            text=req.text,
        )
        return message
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Chat service unavailable: {str(e)}")
