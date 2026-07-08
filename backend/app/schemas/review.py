"""
SG CampusSwap — Pydantic Schemas: Review.
"""

import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class ReviewCreateRequest(BaseModel):
    reviewee_id: uuid.UUID
    transaction_id: uuid.UUID
    rating: int = Field(..., ge=1, le=5)
    comment: str | None = None


class ReviewResponse(BaseModel):
    id: uuid.UUID
    reviewer_id: uuid.UUID
    reviewee_id: uuid.UUID
    transaction_id: uuid.UUID | None
    rating: int
    comment: str | None
    created_at: datetime

    model_config = {"from_attributes": True}
