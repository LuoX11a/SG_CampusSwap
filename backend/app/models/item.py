"""
SG CampusSwap �?Item ORM Model.
"""

import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class ItemCategory(str, enum.Enum):
    textbook = "textbook"
    electronics = "electronics"
    furniture = "furniture"
    daily = "daily"
    other = "other"


class ItemCondition(str, enum.Enum):
    like_new = "like_new"
    good = "good"
    fair = "fair"
    worn = "worn"


class ItemStatus(str, enum.Enum):
    available = "available"
    reserved = "reserved"
    sold = "sold"


class Item(Base):
    __tablename__ = "items"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    seller_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    category: Mapped[ItemCategory] = mapped_column(
        Enum(ItemCategory), nullable=False, default=ItemCategory.other
    )
    price: Mapped[int] = mapped_column(Integer, nullable=False)  # stored in cents (SGD)
    course_code: Mapped[str | None] = mapped_column(String(20), nullable=True, index=True)
    condition: Mapped[ItemCondition] = mapped_column(
        Enum(ItemCondition), nullable=False, default=ItemCondition.good
    )
    campus_location: Mapped[str] = mapped_column(String(100), nullable=False)
    meetup_point: Mapped[str | None] = mapped_column(String(200), nullable=True)
    status: Mapped[ItemStatus] = mapped_column(
        Enum(ItemStatus), nullable=False, default=ItemStatus.available
    )
    view_count: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationships
    seller = relationship("User", back_populates="items")
    images = relationship("ItemImage", back_populates="item", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Item {self.title} ${self.price/100:.2f}>"
