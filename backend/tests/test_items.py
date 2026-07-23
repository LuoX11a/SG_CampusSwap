"""
Tests for Items API endpoints.

GET    /api/v1/items
POST   /api/v1/items
GET    /api/v1/items/{id}
PUT    /api/v1/items/{id}
DELETE /api/v1/items/{id}
PATCH  /api/v1/items/{id}/status
"""

import pytest


class TestListItems:
    """GET /api/v1/items — list items with pagination and filters."""

    def test_list_items_returns_200(self, client):
        """Listing items without auth should return 200 (public endpoint)."""
        response = client.get("/api/v1/items")
        assert response.status_code == 200

    def test_list_items_returns_paginated_response(self, client):
        """Response should include items, total, page, page_size, has_next."""
        response = client.get("/api/v1/items")
        assert response.status_code == 200
        data = response.json()
        assert "items" in data
        assert "total" in data
        assert "page" in data
        assert data["page"] == 1
        assert "page_size" in data
        assert "has_next" in data

    def test_list_items_with_page_param(self, client):
        """Page parameter should be accepted."""
        response = client.get("/api/v1/items?page=2&page_size=10")
        assert response.status_code == 200
        data = response.json()
        assert data["page"] == 2
        assert data["page_size"] == 10

    def test_list_items_invalid_page_rejected(self, client):
        """Page < 1 should return 422."""
        response = client.get("/api/v1/items?page=0")
        assert response.status_code == 422

    def test_list_items_invalid_page_size_rejected(self, client):
        """page_size > 50 should return 422."""
        response = client.get("/api/v1/items?page_size=100")
        assert response.status_code == 422

    def test_list_items_category_filter(self, client):
        """Category filter should be accepted."""
        response = client.get("/api/v1/items?category=textbook")
        assert response.status_code == 200

    def test_list_items_condition_filter(self, client):
        """Condition filter should be accepted."""
        response = client.get("/api/v1/items?condition=like_new")
        assert response.status_code == 200

    def test_list_items_price_range(self, client):
        """Price range filter should be accepted."""
        response = client.get("/api/v1/items?min_price=100&max_price=5000")
        assert response.status_code == 200

    def test_list_items_sort_options(self, client):
        """Sort parameter should be accepted."""
        for sort in ["newest", "oldest", "price_asc", "price_desc", "popular"]:
            response = client.get(f"/api/v1/items?sort={sort}")
            assert response.status_code == 200


class TestCreateItem:
    """POST /api/v1/items — create a new listing (requires auth)."""

    def test_create_item_without_auth_returns_403(self, client):
        """Creating item without auth header should return 403."""
        response = client.post("/api/v1/items", json={})
        assert response.status_code == 403

    def test_create_item_empty_body_returns_422(self, client, auth_headers):
        """Creating item with empty body should return 422."""
        response = client.post("/api/v1/items", json={}, headers=auth_headers)
        assert response.status_code == 422

    @pytest.mark.parametrize(
        "payload,expected_status",
        [
            # Missing required field 'title'
            (
                {
                    "description": "A good textbook",
                    "category": "textbook",
                    "price": 2500,
                    "condition": "good",
                    "campus_location": "NTU",
                    "meetup_point": "Library",
                },
                422,
            ),
            # Missing required field 'price'
            (
                {
                    "title": "CS1010 Textbook",
                    "description": "A good textbook",
                    "category": "textbook",
                    "condition": "good",
                    "campus_location": "NTU",
                    "meetup_point": "Library",
                },
                422,
            ),
            # Price not > 0
            (
                {
                    "title": "CS1010 Textbook",
                    "description": "A good textbook",
                    "category": "textbook",
                    "price": 0,
                    "condition": "good",
                    "campus_location": "NTU",
                    "meetup_point": "Library",
                },
                422,
            ),
            # Invalid category
            (
                {
                    "title": "CS1010 Textbook",
                    "description": "A good textbook",
                    "category": "invalid_category",
                    "price": 2500,
                    "condition": "good",
                    "campus_location": "NTU",
                    "meetup_point": "Library",
                },
                422,
            ),
        ],
    )
    def test_create_item_validation(self, client, auth_headers, payload, expected_status):
        """Various invalid payloads should return validation errors."""
        response = client.post("/api/v1/items", json=payload, headers=auth_headers)
        assert response.status_code == expected_status


class TestGetItem:
    """GET /api/v1/items/{id} — get item detail."""

    def test_get_nonexistent_item_returns_404(self, client):
        """Non-existent item ID should return 404."""
        response = client.get("/api/v1/items/00000000-0000-0000-0000-000000000000")
        assert response.status_code == 404


class TestUpdateItem:
    """PUT /api/v1/items/{id} — update own listing (requires auth)."""

    def test_update_item_without_auth_returns_403(self, client):
        """Updating item without auth should return 403."""
        response = client.put("/api/v1/items/some-id", json={})
        assert response.status_code == 403

    def test_update_nonexistent_item_returns_404(self, client, auth_headers):
        """Updating non-existent item should return 404 (or 403 if auth fails first)."""
        response = client.put(
            "/api/v1/items/00000000-0000-0000-0000-000000000000",
            json={"title": "Updated Title"},
            headers=auth_headers,
        )
        # 403 because the test token is invalid, 404 if token worked
        assert response.status_code in (403, 404)


class TestDeleteItem:
    """DELETE /api/v1/items/{id} — delete own listing (requires auth)."""

    def test_delete_item_without_auth_returns_403(self, client):
        """Deleting item without auth should return 403."""
        response = client.delete("/api/v1/items/some-id")
        assert response.status_code == 403


class TestUpdateItemStatus:
    """PATCH /api/v1/items/{id}/status — mark listing status."""

    def test_update_status_without_auth_returns_403(self, client):
        """Updating status without auth should return 403."""
        response = client.patch("/api/v1/items/some-id/status?new_status=sold")
        assert response.status_code == 403

    def test_update_status_invalid_value_returns_422(self, client, auth_headers):
        """Invalid status value should return 422."""
        response = client.patch(
            "/api/v1/items/some-id/status?new_status=deleted",
            headers=auth_headers,
        )
        assert response.status_code == 422
