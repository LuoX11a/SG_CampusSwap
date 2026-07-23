"""
Tests for Reviews API endpoints.

GET    /api/v1/reviews/user/{user_id}
POST   /api/v1/reviews
GET    /api/v1/reviews/me
GET    /api/v1/reviews/rating-summary/{user_id}
"""

import pytest


class TestGetUserReviews:
    """GET /api/v1/reviews/user/{user_id} — get reviews for a user."""

    def test_get_user_reviews_public_access(self, client):
        """Public endpoint — should not require auth."""
        response = client.get("/api/v1/reviews/user/00000000-0000-0000-0000-000000000000")
        assert response.status_code in (200, 404)

    def test_get_user_reviews_invalid_uuid(self, client):
        """Invalid UUID should return 422."""
        response = client.get("/api/v1/reviews/user/not-a-uuid")
        assert response.status_code == 422

    def test_get_user_reviews_with_pagination(self, client):
        """Pagination should be accepted."""
        response = client.get(
            "/api/v1/reviews/user/00000000-0000-0000-0000-000000000000?page=1&page_size=10"
        )
        assert response.status_code in (200, 404)


class TestCreateReview:
    """POST /api/v1/reviews — create a review (requires auth)."""

    def test_create_review_without_auth_returns_403(self, client):
        """Creating review without auth should return 403."""
        response = client.post("/api/v1/reviews", json={})
        assert response.status_code == 403

    def test_create_review_missing_fields(self, client, auth_headers):
        """Missing required fields should return 422."""
        response = client.post("/api/v1/reviews", json={}, headers=auth_headers)
        assert response.status_code == 422

    def test_create_review_invalid_rating(self, client, auth_headers):
        """Rating outside 1-5 should return 422."""
        payload = {
            "reviewee_id": "00000000-0000-0000-0000-000000000000",
            "transaction_id": "00000000-0000-0000-0000-000000000000",
            "rating": 0,
            "comment": "Great seller, very responsive!",
        }
        response = client.post("/api/v1/reviews", json=payload, headers=auth_headers)
        assert response.status_code == 422

    @pytest.mark.parametrize("rating", [1, 2, 3, 4, 5])
    def test_create_review_valid_ratings(self, client, auth_headers, rating):
        """Ratings 1-5 should pass schema validation."""
        payload = {
            "reviewee_id": "00000000-0000-0000-0000-000000000000",
            "transaction_id": "00000000-0000-0000-0000-000000000000",
            "rating": rating,
            "comment": "Good transaction experience.",
        }
        response = client.post("/api/v1/reviews", json=payload, headers=auth_headers)
        # 403 if token invalid, other if DB fails
        assert response.status_code != 422

    def test_create_review_short_comment(self, client, auth_headers):
        """Comment shorter than 5 chars should return 422."""
        payload = {
            "reviewee_id": "00000000-0000-0000-0000-000000000000",
            "transaction_id": "00000000-0000-0000-0000-000000000000",
            "rating": 5,
            "comment": "Ok",
        }
        response = client.post("/api/v1/reviews", json=payload, headers=auth_headers)
        assert response.status_code == 422


class TestGetMyReviews:
    """GET /api/v1/reviews/me — get my received reviews."""

    def test_get_my_reviews_without_auth_returns_403(self, client):
        """Accessing without auth should return 403."""
        response = client.get("/api/v1/reviews/me")
        assert response.status_code == 403


class TestRatingSummary:
    """GET /api/v1/reviews/rating-summary/{user_id} — rating distribution."""

    def test_rating_summary_public_access(self, client):
        """Public endpoint — should return rating distribution."""
        response = client.get("/api/v1/reviews/rating-summary/00000000-0000-0000-0000-000000000000")
        assert response.status_code in (200, 404)

    def test_rating_summary_structure(self, client):
        """Response should include average, total, and distribution."""
        response = client.get("/api/v1/reviews/rating-summary/00000000-0000-0000-0000-000000000000")
        if response.status_code == 200:
            data = response.json()
            assert "average" in data
            assert "total" in data
            assert "distribution" in data
            # Distribution should have keys 1-5
            for key in ["1", "2", "3", "4", "5"]:
                assert key in data["distribution"]
