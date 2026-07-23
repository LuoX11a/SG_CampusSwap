"""
Item CRUD API Routes

GET    /api/v1/items          — List items (paginated, filterable)
POST   /api/v1/items          — Create a new listing
GET    /api/v1/items/{id}     — Get item detail
PUT    /api/v1/items/{id}     — Update own listing
DELETE /api/v1/items/{id}     — Delete own listing
PATCH  /api/v1/items/{id}/status — Mark as sold/reserved/available
"""

from datetime import datetime, timezone
from typing import Optional, List
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field
from sqlalchemy import select, func, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.user import User
from app.models.item import Item, ItemStatus, ItemCategory, ItemCondition
from app.models.review import ItemImage
from app.api.v1.auth import get_current_user

router = APIRouter()


# ─── Schemas ───────────────────────────────────────────────────

class ItemCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=10, max_length=2000)
    category: ItemCategory
    price: int = Field(..., gt=0, description="Price in cents (e.g., 2500 = $25.00)")
    condition: ItemCondition
    course_code: Optional[str] = Field(None, max_length=20)
    campus_location: str = Field(..., min_length=2)
    meetup_point: str = Field(..., min_length=2)
    image_urls: List[str] = Field(default_factory=list, max_length=5)


class ItemUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, min_length=10, max_length=2000)
    category: Optional[ItemCategory] = None
    price: Optional[int] = Field(None, gt=0)
    condition: Optional[ItemCondition] = None
    course_code: Optional[str] = Field(None, max_length=20)
    campus_location: Optional[str] = None
    meetup_point: Optional[str] = None


class SellerInfo(BaseModel):
    id: str
    username: str
    avatar_url: Optional[str]
    university: str
    campus: str
    rating_avg: Optional[float]
    rating_count: int

    class Config:
        from_attributes = True


class ItemResponse(BaseModel):
    id: str
    title: str
    description: str
    category: str
    price: int
    condition: str
    course_code: Optional[str]
    campus_location: str
    meetup_point: str
    status: str
    view_count: int
    created_at: str
    updated_at: str
    seller: SellerInfo
    images: List[str]
    primary_image: Optional[str] = None

    class Config:
        from_attributes = True


class ItemListResponse(BaseModel):
    items: List[ItemResponse]
    total: int
    page: int
    page_size: int
    has_next: bool


# ─── Helpers ───────────────────────────────────────────────────

def item_to_response(item: Item) -> dict:
    """Convert Item ORM object to response dict."""
    images = [img.url for img in item.images] if item.images else []
    primary = next((img.url for img in item.images if img.is_primary), None) if item.images else None
    return {
        "id": str(item.id),
        "title": item.title,
        "description": item.description,
        "category": item.category.value if hasattr(item.category, 'value') else item.category,
        "price": item.price,
        "condition": item.condition.value if hasattr(item.condition, 'value') else item.condition,
        "course_code": item.course_code,
        "campus_location": item.campus_location,
        "meetup_point": item.meetup_point,
        "status": item.status.value if hasattr(item.status, 'value') else item.status,
        "view_count": item.view_count,
        "created_at": item.created_at.isoformat() if item.created_at else "",
        "updated_at": item.updated_at.isoformat() if item.updated_at else "",
        "seller": {
            "id": str(item.seller.id),
            "username": item.seller.username,
            "avatar_url": item.seller.avatar_url,
            "university": item.seller.university,
            "campus": item.seller.campus,
            "rating_avg": item.seller.rating_avg,
            "rating_count": item.seller.rating_count or 0,
        },
        "images": images,
        "primary_image": primary,
    }


# ─── Routes ────────────────────────────────────────────────────

@router.get("", response_model=ItemListResponse)
async def list_items(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=50),
    category: Optional[str] = Query(None),
    condition: Optional[str] = Query(None),
    campus: Optional[str] = Query(None),
    min_price: Optional[int] = Query(None, ge=0),
    max_price: Optional[int] = Query(None, ge=0),
    status: str = Query("available"),
    sort: str = Query("newest"),
    db: AsyncSession = Depends(get_db),
):
    """List items with pagination and optional filters."""
    item_status = (
        ItemStatus[status.lower()]
        if status.lower() in ItemStatus.__members__
        else ItemStatus.available
    )
    conditions = [Item.status == item_status]

    if category:
        try:
            conditions.append(Item.category == ItemCategory[category.lower()])
        except (KeyError, AttributeError):
            pass

    if condition:
        try:
            conditions.append(Item.condition == ItemCondition[condition.lower()])
        except (KeyError, AttributeError):
            pass

    if campus:
        conditions.append(Item.campus_location.ilike(f"%{campus}%"))

    if min_price is not None:
        conditions.append(Item.price >= min_price)
    if max_price is not None:
        conditions.append(Item.price <= max_price)

    count_q = select(func.count(Item.id)).where(and_(*conditions))
    total = (await db.execute(count_q)).scalar() or 0

    sort_map = {
        "newest": Item.created_at.desc(),
        "oldest": Item.created_at.asc(),
        "price_asc": Item.price.asc(),
        "price_desc": Item.price.desc(),
        "popular": Item.view_count.desc(),
    }
    order_by = sort_map.get(sort, Item.created_at.desc())

    q = (
        select(Item)
        .where(and_(*conditions))
        .options(selectinload(Item.seller), selectinload(Item.images))
        .order_by(order_by)
        .offset((page - 1) * page_size)
        .limit(page_size)
    )
    result = await db.execute(q)
    items = result.scalars().all()

    return {
        "items": [item_to_response(item) for item in items],
        "total": total,
        "page": page,
        "page_size": page_size,
        "has_next": (page * page_size) < total,
    }


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: str, db: AsyncSession = Depends(get_db)):
    """Get a single item with full details."""
    q = (
        select(Item)
        .where(Item.id == item_id)
        .options(selectinload(Item.seller), selectinload(Item.images))
    )
    result = await db.execute(q)
    item = result.scalar_one_or_none()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item.view_count += 1
    await db.commit()

    return item_to_response(item)


@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(
    data: ItemCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Create a new listing."""
    item = Item(
        id=uuid4(),
        seller_id=current_user.id,
        title=data.title,
        description=data.description,
        category=data.category,
        price=data.price,
        condition=data.condition,
        course_code=data.course_code,
        campus_location=data.campus_location,
        meetup_point=data.meetup_point,
        status=ItemStatus.available,
        view_count=0,
    )
    db.add(item)

    for i, url in enumerate(data.image_urls[:5]):
        image = ItemImage(
            id=uuid4(),
            item_id=item.id,
            url=url,
            is_primary=(i == 0),
        )
        db.add(image)

    await db.commit()
    await db.refresh(item)

    q = (
        select(Item)
        .where(Item.id == item.id)
        .options(selectinload(Item.seller), selectinload(Item.images))
    )
    result = await db.execute(q)
    item = result.scalar_one()

    return item_to_response(item)


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(
    item_id: str,
    data: ItemUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Update own listing."""
    q = (
        select(Item)
        .where(Item.id == item_id)
        .options(selectinload(Item.seller), selectinload(Item.images))
    )
    result = await db.execute(q)
    item = result.scalar_one_or_none()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.seller_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only edit your own listings")

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(item, field, value)
    item.updated_at = datetime.now(timezone.utc)

    await db.commit()
    await db.refresh(item)

    return item_to_response(item)


@router.delete("/{item_id}", status_code=204)
async def delete_item(
    item_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Delete own listing."""
    q = select(Item).where(Item.id == item_id)
    result = await db.execute(q)
    item = result.scalar_one_or_none()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.seller_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only delete your own listings")

    await db.delete(item)
    await db.commit()
    return None


@router.patch("/{item_id}/status", response_model=ItemResponse)
async def update_item_status(
    item_id: str,
    new_status: str = Query(..., pattern="^(sold|reserved|available)$"),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Mark listing as sold, reserved, or available."""
    q = (
        select(Item)
        .where(Item.id == item_id)
        .options(selectinload(Item.seller), selectinload(Item.images))
    )
    result = await db.execute(q)
    item = result.scalar_one_or_none()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.seller_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only update your own listings")

    try:
        item.status = ItemStatus[new_status.lower()]
    except KeyError:
        raise HTTPException(status_code=400, detail=f"Invalid status: {new_status}")

    item.updated_at = datetime.now(timezone.utc)
    await db.commit()
    await db.refresh(item)

    return item_to_response(item)
