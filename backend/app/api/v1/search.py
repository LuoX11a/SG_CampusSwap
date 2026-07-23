"""
Search & Filter API Routes

GET /api/v1/search — Full-text search with filters
"""

from typing import Optional, List

from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy import select, func, and_, or_, case
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.item import Item, ItemStatus, ItemCategory, ItemCondition

router = APIRouter()


class SearchItemResult(BaseModel):
    id: str
    title: str
    price: int
    category: str
    condition: str
    campus_location: str
    status: str
    created_at: str
    seller_name: str
    seller_rating: Optional[float]
    primary_image: Optional[str]
    relevance: float = 1.0

    model_config = {"from_attributes": True}


class SearchResponse(BaseModel):
    results: List[SearchItemResult]
    total: int
    query: str
    filters_applied: List[str]
    sort: str


@router.get("", response_model=SearchResponse)
async def search_items(
    q: str = Query("", description="Search keyword"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=50),
    category: Optional[str] = Query(None),
    condition: Optional[str] = Query(None),
    campus: Optional[str] = Query(None),
    min_price: Optional[int] = Query(None, ge=0),
    max_price: Optional[int] = Query(None, ge=0),
    has_course_code: Optional[bool] = Query(None),
    sort: str = Query("relevance"),
    db: AsyncSession = Depends(get_db),
):
    """Search items by keyword with optional filters."""
    conditions = [Item.status == ItemStatus.available]
    filters_applied = []

    if q.strip():
        search_term = f"%{q.strip()}%"
        conditions.append(
            or_(
                Item.title.ilike(search_term),
                Item.description.ilike(search_term),
                Item.course_code.ilike(search_term),
            )
        )
        filters_applied.append(f"keyword: {q.strip()}")

    if category:
        try:
            conditions.append(Item.category == ItemCategory[category.lower()])
            filters_applied.append(f"category: {category}")
        except (KeyError, AttributeError):
            pass

    if condition:
        try:
            conditions.append(Item.condition == ItemCondition[condition.lower()])
            filters_applied.append(f"condition: {condition}")
        except (KeyError, AttributeError):
            pass

    if campus:
        conditions.append(Item.campus_location.ilike(f"%{campus}%"))
        filters_applied.append(f"campus: {campus}")

    if min_price is not None:
        conditions.append(Item.price >= min_price)
        filters_applied.append(f"min_price: {min_price}")
    if max_price is not None:
        conditions.append(Item.price <= max_price)
        filters_applied.append(f"max_price: {max_price}")

    if has_course_code:
        conditions.append(Item.course_code.isnot(None))
        conditions.append(Item.course_code != "")
        filters_applied.append("has_course_code: true")

    count_q = select(func.count(Item.id)).where(and_(*conditions))
    total = (await db.execute(count_q)).scalar() or 0

    # Relevance sort: prioritize exact title matches, then other matches
    if sort == "relevance" and q:
        relevance_expr = func.greatest(
            case(
                (Item.title.ilike(f"%{q}%"), 3),
                else_=0,
            ),
            case(
                (Item.description.ilike(f"%{q}%"), 2),
                else_=0,
            ),
            case(
                (Item.course_code.ilike(f"%{q}%"), 1),
                else_=0,
            ),
        )
        order_by = relevance_expr.desc()
    else:
        sort_map = {
            "newest": Item.created_at.desc(),
            "price_asc": Item.price.asc(),
            "price_desc": Item.price.desc(),
            "popular": Item.view_count.desc(),
        }
        order_by = sort_map.get(sort, Item.created_at.desc())

    search_term = q

    query_obj = (
        select(Item)
        .where(and_(*conditions))
        .options(selectinload(Item.seller), selectinload(Item.images))
        .order_by(order_by)
        .offset((page - 1) * page_size)
        .limit(page_size)
    )
    result = await db.execute(query_obj)
    items = result.scalars().all()

    results = []
    for item in items:
        primary = (
            next((img.url for img in item.images if img.is_primary), None) if item.images else None
        )
        results.append(
            {
                "id": str(item.id),
                "title": item.title,
                "price": item.price,
                "category": (
                    item.category.value if hasattr(item.category, "value") else str(item.category)
                ),
                "condition": (
                    item.condition.value
                    if hasattr(item.condition, "value")
                    else str(item.condition)
                ),
                "campus_location": item.campus_location,
                "status": (
                    item.status.value if hasattr(item.status, "value") else str(item.status)
                ),
                "created_at": item.created_at.isoformat() if item.created_at else "",
                "seller_name": item.seller.username if item.seller else "Unknown",
                "seller_rating": item.seller.rating_avg if item.seller else None,
                "primary_image": primary,
                "relevance": 1.0,
            }
        )

    return {
        "results": results,
        "total": total,
        "query": search_term if search_term else "",
        "filters_applied": filters_applied,
        "sort": sort,
    }
