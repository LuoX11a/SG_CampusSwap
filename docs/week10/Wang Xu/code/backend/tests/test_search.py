"""
Tests for Search API endpoints.

GET /api/v1/search — full-text search with filters
"""

import pytest


class TestSearch:
    """GET /api/v1/search — search items."""

    def test_search_basic_returns_200(self, client):
        """Basic search should return 200 (public endpoint)."""
        response = client.get("/api/v1/search")
        assert response.status_code == 200

    def test_search_response_structure(self, client):
        """Response should include results, total, query, filters_applied, sort."""
        response = client.get("/api/v1/search")
        assert response.status_code == 200
        data = response.json()
        assert "results" in data
        assert "total" in data
        assert "query" in data
        assert "filters_applied" in data
        assert "sort" in data

    def test_search_with_keyword(self, client):
        """Search with a keyword query."""
        response = client.get("/api/v1/search?q=textbook")
        assert response.status_code == 200
        data = response.json()
        assert "keyword: textbook" in data.get("filters_applied", [])

    def test_search_with_empty_query(self, client):
        """Empty query should return all available items."""
        response = client.get("/api/v1/search?q=")
        assert response.status_code == 200
        data = response.json()
        assert data["query"] == ""
        # Empty query should not add keyword filter
        assert not any("keyword" in f for f in data.get("filters_applied", []))

    def test_search_with_category_filter(self, client):
        """Search with category filter."""
        response = client.get("/api/v1/search?category=electronics")
        assert response.status_code == 200
        data = response.json()
        assert "category: electronics" in data.get("filters_applied", [])

    def test_search_with_condition_filter(self, client):
        """Search with condition filter."""
        response = client.get("/api/v1/search?condition=like_new")
        assert response.status_code == 200

    def test_search_with_campus_filter(self, client):
        """Search with campus filter."""
        response = client.get("/api/v1/search?campus=NTU")
        assert response.status_code == 200
        data = response.json()
        assert "campus: NTU" in data.get("filters_applied", [])

    def test_search_with_price_range(self, client):
        """Search with price range."""
        response = client.get("/api/v1/search?min_price=500&max_price=5000")
        assert response.status_code == 200
        data = response.json()
        assert "min_price: 500" in data.get("filters_applied", [])
        assert "max_price: 5000" in data.get("filters_applied", [])

    def test_search_with_course_code_only(self, client):
        """Search with has_course_code filter."""
        response = client.get("/api/v1/search?has_course_code=true")
        assert response.status_code == 200
        data = response.json()
        assert "has_course_code: true" in data.get("filters_applied", [])

    def test_search_invalid_page_rejected(self, client):
        """Page < 1 should return 422."""
        response = client.get("/api/v1/search?page=0")
        assert response.status_code == 422

    @pytest.mark.parametrize("sort", ["relevance", "newest", "price_asc", "price_desc", "popular"])
    def test_search_sort_options(self, client, sort):
        """All sort options should be accepted."""
        response = client.get(f"/api/v1/search?sort={sort}")
        assert response.status_code == 200

    def test_search_combined_filters(self, client):
        """Multiple filters combined should all appear in filters_applied."""
        response = client.get(
            "/api/v1/search?q=laptop&category=electronics&min_price=100&max_price=10000"
        )
        assert response.status_code == 200
        data = response.json()
        filters = data.get("filters_applied", [])
        assert len(filters) >= 3  # keyword, category, min_price, max_price

    def test_search_result_item_structure(self, client):
        """Each search result should have expected fields."""
        response = client.get("/api/v1/search?q=test")
        assert response.status_code == 200
        data = response.json()
        for item in data.get("results", []):
            assert "id" in item
            assert "title" in item
            assert "price" in item
            assert "category" in item
            assert "condition" in item
            assert "seller_name" in item
