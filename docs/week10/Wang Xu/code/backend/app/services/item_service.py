"""
Item Business Logic Service

Handles complex item operations beyond basic CRUD:
- Price formatting
- Category validation
- Search relevance scoring
- Listing status transitions
"""

from typing import Optional, List, Dict, Any
from app.models.item import Item, ItemStatus, ItemCategory, ItemCondition


def format_price(cents: int) -> str:
    """Convert cents to display string. e.g., 2500 �?'$25.00'"""
    return f"${cents / 100:,.2f}"


def parse_price(price_str: str) -> int:
    """Parse a price string to cents. e.g., '$25.00' �?2500"""
    cleaned = price_str.replace("$", "").replace(",", "").strip()
    return int(float(cleaned) * 100)


def get_category_emoji(category: ItemCategory) -> str:
    """Get emoji for a category."""
    emoji_map = {
        ItemCategory.TEXTBOOK: "📚",
        ItemCategory.ELECTRONICS: "💻",
        ItemCategory.FURNITURE: "🪑",
        ItemCategory.DAILY_ESSENTIALS: "🧴",
        ItemCategory.OTHER: "📦",
    }
    return emoji_map.get(category, "📦")


def get_condition_label(condition: ItemCondition) -> str:
    """Get human-readable label for condition."""
    label_map = {
        ItemCondition.LIKE_NEW: "Like New",
        ItemCondition.GOOD: "Good",
        ItemCondition.FAIR: "Fair",
        ItemCondition.WORN: "Worn",
    }
    return label_map.get(condition, str(condition))


def get_status_color(status: ItemStatus) -> str:
    """Get display color for item status."""
    color_map = {
        ItemStatus.available: "#10B981",  # Green
        ItemStatus.reserved: "#F59E0B",  # Amber
        ItemStatus.sold: "#6B7280",       # Gray
    }
    return color_map.get(status, "#6B7280")


def validate_status_transition(current: ItemStatus, new: ItemStatus) -> bool:
    """Validate that a status transition is allowed."""
    allowed = {
        ItemStatus.available: [ItemStatus.reserved, ItemStatus.sold],
        ItemStatus.reserved: [ItemStatus.available, ItemStatus.sold],
        ItemStatus.sold: [],  # Terminal state
    }
    return new in allowed.get(current, [])


def compute_search_relevance(item: Item, query: str) -> float:
    """Compute relevance score for search results. 0.0�?.0."""
    if not query:
        return 1.0

    query_lower = query.lower()
    score = 0.0

    # Title exact match
    if query_lower == item.title.lower():
        score += 0.5
    # Title contains query
    elif query_lower in item.title.lower():
        score += 0.3

    # Course code match
    if item.course_code and query_lower in item.course_code.lower():
        score += 0.3

    # Description contains query
    if item.description and query_lower in item.description.lower():
        score += 0.1

    # Category match
    try:
        if query_lower in item.category.value.lower():
            score += 0.1
    except AttributeError:
        pass

    return min(score, 1.0)


def paginate_items(
    items: List[Any],
    page: int = 1,
    page_size: int = 20,
) -> Dict[str, Any]:
    """Paginate a list of items."""
    total = len(items)
    start = (page - 1) * page_size
    end = start + page_size

    return {
        "items": items[start:end],
        "total": total,
        "page": page,
        "page_size": page_size,
        "has_next": end < total,
    }
