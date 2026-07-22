"""
Reviews API Routes

GET    /api/v1/reviews/user/{user_id}       — Get reviews for a user
POST   /api/v1/reviews                      — Create a review
GET    /api/v1/reviews/me                   — Get my reviews
GET    /api/v1/reviews/rating-summary/{user_id} — Rating distribution
"""

from typing import Optional, List
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field
from sqlalchemy import select, func, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.database import get_db
from app.models.user import User
from app.models.review import Review, Transaction, TransactionStatus
from app.api.v1.auth import get_current_user

router = APIRouter()


# ─── Schemas ───────────────────────────────────────────────────

class ReviewCreate(BaseModel):
    reviewee_id: str
    transaction_id: str
    rating: int = Field(..., ge=1, le=5)
    comment: str = Field(..., min_length=5, max_length=500)


class ReviewResponse(BaseModel):
    id: str
    reviewer: dict
    reviewee_id: str
    transaction_id: str
    rating: int
    comment: str
    created_at: str

    class Config:
        from_attributes = True


class RatingSummary(BaseModel):
    average: float
    total: int
    distribution: dict


# ─── Routes ────────────────────────────────────────────────────

@router.get("/user/{user_id}", response_model=List[ReviewResponse])
async def get_user_reviews(
    user_id: str,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
):
    """Get reviews for a specific user."""
    q = (
        select(Review)
        .where(Review.reviewee_id == user_id)
        .options(joinedload(Review.reviewer))
        .order_by(Review.created_at.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
    )
    result = await db.execute(q)
    reviews = result.scalars().all()

    return [
        {
            "id": str(r.id),
            "reviewer": {
                "id": str(r.reviewer.id),
                "username": r.reviewer.username,
                "avatar_url": r.reviewer.avatar_url,
            },
            "reviewee_id": str(r.reviewee_id),
            "transaction_id": str(r.transaction_id) if r.transaction_id else "",
            "rating": r.rating,
            "comment": r.comment,
            "created_at": r.created_at.isoformat() if r.created_at else "",
        }
        for r in reviews
    ]


@router.post("", status_code=201)
async def create_review(
    data: ReviewCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Create a review for a completed transaction."""
    result = await db.execute(
        select(Transaction).where(
            and_(
                Transaction.id == data.transaction_id,
                Transaction.status == TransactionStatus.completed,
            )
        )
    )
    transaction = result.scalar_one_or_none()

    if not transaction:
        raise HTTPException(status_code=400, detail="Transaction not found or not completed")

    if current_user.id not in [transaction.buyer_id, transaction.seller_id]:
        raise HTTPException(status_code=403, detail="You are not part of this transaction")

    if str(current_user.id) == data.reviewee_id:
        raise HTTPException(status_code=400, detail="You cannot review yourself")

    result = await db.execute(
        select(Review).where(
            and_(
                Review.transaction_id == data.transaction_id,
                Review.reviewer_id == current_user.id,
            )
        )
    )
    if result.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="You have already reviewed this transaction")

    review = Review(
        id=uuid4(),
        reviewer_id=current_user.id,
        reviewee_id=data.reviewee_id,
        transaction_id=data.transaction_id,
        rating=data.rating,
        comment=data.comment,
    )
    db.add(review)

    # Update reviewee's rating average
    result = await db.execute(select(User).where(User.id == data.reviewee_id))
    reviewee = result.scalar_one_or_none()
    if reviewee:
        avg_result = await db.execute(
            select(func.avg(Review.rating)).where(Review.reviewee_id == data.reviewee_id)
        )
        new_avg = avg_result.scalar() or 0.0
        count_result = await db.execute(
            select(func.count(Review.id)).where(Review.reviewee_id == data.reviewee_id)
        )
        new_count = count_result.scalar() or 0
        reviewee.rating_avg = round(float(new_avg), 2)
        reviewee.rating_count = new_count

    await db.commit()

    return {"message": "Review submitted successfully"}


@router.get("/me", response_model=List[ReviewResponse])
async def get_my_reviews(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Get reviews received by current user."""
    q = (
        select(Review)
        .where(Review.reviewee_id == current_user.id)
        .options(joinedload(Review.reviewer))
        .order_by(Review.created_at.desc())
        .limit(50)
    )
    result = await db.execute(q)
    reviews = result.scalars().all()

    return [
        {
            "id": str(r.id),
            "reviewer": {
                "id": str(r.reviewer.id) if r.reviewer else "",
                "username": r.reviewer.username if r.reviewer else "Unknown",
                "avatar_url": r.reviewer.avatar_url if r.reviewer else None,
            },
            "reviewee_id": str(r.reviewee_id),
            "transaction_id": str(r.transaction_id) if r.transaction_id else "",
            "rating": r.rating,
            "comment": r.comment,
            "created_at": r.created_at.isoformat() if r.created_at else "",
        }
        for r in reviews
    ]


@router.get("/rating-summary/{user_id}", response_model=RatingSummary)
async def get_rating_summary(user_id: str, db: AsyncSession = Depends(get_db)):
    """Get rating distribution for a user."""
    distribution = {}
    for rating in range(1, 6):
        count_q = select(func.count(Review.id)).where(
            and_(Review.reviewee_id == user_id, Review.rating == rating)
        )
        count = (await db.execute(count_q)).scalar() or 0
        distribution[str(rating)] = count

    avg_q = select(func.avg(Review.rating)).where(Review.reviewee_id == user_id)
    avg = (await db.execute(avg_q)).scalar() or 0.0
    total = sum(distribution.values())

    return {"average": round(float(avg), 2), "total": total, "distribution": distribution}
