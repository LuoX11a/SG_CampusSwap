"""
User Profile API Routes

GET  /api/v1/users/{id}         — Get public user profile
PUT  /api/v1/users/me           — Update own profile
GET  /api/v1/users/me/listings  — Get current user's listings
GET  /api/v1/users/{id}/listings — Get a user's public listings
"""

import uuid
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field
from sqlalchemy import select, func, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.user import User
from app.models.item import Item, ItemStatus
from app.api.v1.auth import get_current_user

router = APIRouter()


# ─── Schemas ───────────────────────────────────────────────────


class UserProfileResponse(BaseModel):
    id: str
    username: str
    university: str
    campus: str
    avatar_url: Optional[str]
    rating_avg: Optional[float]
    rating_count: int
    member_since: str
    active_listings_count: int

    model_config = {"from_attributes": True}


class ProfileUpdateRequest(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=20, pattern=r"^[a-zA-Z0-9_]+$")
    university: Optional[str] = None
    campus: Optional[str] = None


# ─── Routes ────────────────────────────────────────────────────


@router.get("/{user_id}", response_model=UserProfileResponse)
async def get_user_profile(user_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    """Get a user's public profile."""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    count_q = select(func.count(Item.id)).where(
        and_(Item.seller_id == user.id, Item.status == ItemStatus.available)
    )
    active_count = (await db.execute(count_q)).scalar() or 0

    return {
        "id": str(user.id),
        "username": user.username,
        "university": user.university,
        "campus": user.campus,
        "avatar_url": user.avatar_url,
        "rating_avg": user.rating_avg,
        "rating_count": user.rating_count or 0,
        "member_since": user.created_at.isoformat() if user.created_at else "",
        "active_listings_count": active_count,
    }


@router.put("/me", response_model=UserProfileResponse)
async def update_profile(
    data: ProfileUpdateRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Update current user's profile."""
    if data.username and data.username != current_user.username:
        result = await db.execute(select(User).where(User.username == data.username))
        if result.scalar_one_or_none():
            raise HTTPException(status_code=409, detail="Username already taken")
        current_user.username = data.username

    if data.university:
        current_user.university = data.university
    if data.campus:
        current_user.campus = data.campus

    await db.commit()
    await db.refresh(current_user)

    count_q = select(func.count(Item.id)).where(
        and_(Item.seller_id == current_user.id, Item.status == ItemStatus.available)
    )
    active_count = (await db.execute(count_q)).scalar() or 0

    return {
        "id": str(current_user.id),
        "username": current_user.username,
        "university": current_user.university,
        "campus": current_user.campus,
        "avatar_url": current_user.avatar_url,
        "rating_avg": current_user.rating_avg,
        "rating_count": current_user.rating_count or 0,
        "member_since": current_user.created_at.isoformat() if current_user.created_at else "",
        "active_listings_count": active_count,
    }


@router.get("/me/listings")
async def get_my_listings(
    status: Optional[str] = Query(None, pattern="^(available|sold|reserved)$"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=50),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Get current user's listings with optional status filter."""
    conditions = [Item.seller_id == current_user.id]
    if status:
        try:
            conditions.append(Item.status == ItemStatus[status.upper()])
        except KeyError:
            pass

    count_q = select(func.count(Item.id)).where(and_(*conditions))
    total = (await db.execute(count_q)).scalar() or 0

    q = (
        select(Item)
        .where(and_(*conditions))
        .options(selectinload(Item.images))
        .order_by(Item.created_at.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
    )
    result = await db.execute(q)
    items = result.scalars().all()

    return {
        "items": [
            {
                "id": str(item.id),
                "title": item.title,
                "price": item.price,
                "status": item.status.value if hasattr(item.status, "value") else str(item.status),
                "primary_image": (
                    next((img.url for img in item.images if img.is_primary), None)
                    if item.images
                    else None
                ),
                "created_at": item.created_at.isoformat() if item.created_at else "",
                "view_count": item.view_count,
            }
            for item in items
        ],
        "total": total,
        "page": page,
        "page_size": page_size,
    }


@router.get("/{user_id}/listings")
async def get_user_listings(
    user_id: uuid.UUID,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
):
    """Get a user's public active listings."""
    conditions = [Item.seller_id == user_id, Item.status == ItemStatus.available]

    count_q = select(func.count(Item.id)).where(and_(*conditions))
    total = (await db.execute(count_q)).scalar() or 0

    q = (
        select(Item)
        .where(and_(*conditions))
        .options(selectinload(Item.images))
        .order_by(Item.created_at.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
    )
    result = await db.execute(q)
    items = result.scalars().all()

    return {
        "items": [
            {
                "id": str(item.id),
                "title": item.title,
                "price": item.price,
                "category": (
                    item.category.value if hasattr(item.category, "value") else str(item.category)
                ),
                "primary_image": (
                    next((img.url for img in item.images if img.is_primary), None)
                    if item.images
                    else None
                ),
                "created_at": item.created_at.isoformat() if item.created_at else "",
            }
            for item in items
        ],
        "total": total,
        "page": page,
        "page_size": page_size,
    }


# ── Account Management ────────────────────────────────────────────


class ChangePasswordRequest(BaseModel):
    current_password: str = Field(..., min_length=8)
    new_password: str = Field(..., min_length=8)


@router.post("/me/change-password")
async def change_password(
    req: ChangePasswordRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Change the current user's password."""
    from app.services.auth_service import hash_password, verify_password

    if not verify_password(req.current_password, current_user.password_hash):
        raise HTTPException(status_code=400, detail="Current password is incorrect")
    if req.current_password == req.new_password:
        raise HTTPException(status_code=400, detail="New password must differ from current")

    if not any(c.isupper() for c in req.new_password):
        raise HTTPException(status_code=400, detail="Password must contain an uppercase letter")
    if not any(c.isdigit() for c in req.new_password):
        raise HTTPException(status_code=400, detail="Password must contain a digit")

    current_user.password_hash = hash_password(req.new_password)
    await db.commit()
    return {"message": "Password changed successfully"}


class DeleteAccountRequest(BaseModel):
    password: str = Field(..., min_length=8)


@router.post("/me/delete-account")
async def delete_account(
    req: DeleteAccountRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Delete the current user's account. Requires password confirmation."""
    from app.services.auth_service import verify_password

    if not verify_password(req.password, current_user.password_hash):
        raise HTTPException(status_code=400, detail="Password is incorrect")

    await db.delete(current_user)
    await db.commit()
    return {"message": "Account deleted successfully"}
