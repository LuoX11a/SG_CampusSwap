"""
SG CampusSwap — Pydantic Schemas: Item (Request / Response).
"""

import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class ItemCreateRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    category: str = Field(default="other")
    price: int = Field(..., ge=0, description="Price in SGD cents")
    course_code: str | None = Field(None, max_length=20)
    condition: str = Field(default="good")
    campus_location: str = Field(..., max_length=100)
    meetup_point: str | None = Field(None, max_length=200)
    image_urls: list[str] = Field(default_factory=list, max_length=5)


class ItemUpdateRequest(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = None
    category: str | None = None
    price: int | None = Field(None, ge=0)
    course_code: str | None = Field(None, max_length=20)
    condition: str | None = None
    campus_location: str | None = None
    meetup_point: str | None = None
    status: str | None = None


class ItemImageResponse(BaseModel):
    id: uuid.UUID
    url: str
    is_primary: bool

    model_config = {"from_attributes": True}


class ItemResponse(BaseModel):
    id: uuid.UUID
    seller_id: uuid.UUID
    title: str
    description: str | None
    category: str
    price: int
    course_code: str | None
    condition: str
    campus_location: str
    meetup_point: str | None
    status: str
    view_count: int
    images: list[ItemImageResponse] = []
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ItemListResponse(BaseModel):
    items: list[ItemResponse]
    total: int
    page: int
    size: int
    pages: int
