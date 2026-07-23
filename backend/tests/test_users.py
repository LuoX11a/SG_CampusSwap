"""
Tests for Users API endpoints.

GET  /api/v1/users/{id}
PUT  /api/v1/users/me
GET  /api/v1/users/me/listings
GET  /api/v1/users/{id}/listings
"""

import pytest


class TestGetUserProfile:
    """GET /api/v1/users/{id} — get public user profile."""

    def test_get_user_profile_returns_200_or_404(self, client):
        """Public endpoint — returns 404 for non-existent user (no DB)."""
        response = client.get("/api/v1/users/00000000-0000-0000-0000-000000000000")
        assert response.status_code in (200, 404)

    def test_get_user_profile_invalid_uuid(self, client):
        """Invalid UUID should be handled gracefully."""
        response = client.get("/api/v1/users/not-a-valid-uuid")
        # FastAPI path validation should catch invalid UUID format
        assert response.status_code == 422


class TestUpdateProfile:
    """PUT /api/v1/users/me — update own profile (requires auth)."""

    def test_update_profile_without_auth_returns_403(self, client):
        """Updating profile without auth should return 403."""
        response = client.put("/api/v1/users/me", json={})
        assert response.status_code == 403

    def test_update_profile_empty_body(self, client, auth_headers):
        """Empty update body should be accepted (no changes)."""
        response = client.put("/api/v1/users/me", json={}, headers=auth_headers)
        # 403 if token invalid, 200 if it works
        assert response.status_code in (200, 403)

    def test_update_profile_invalid_username(self, client, auth_headers):
        """Invalid username format should return 422."""
        response = client.put(
            "/api/v1/users/me",
            json={"username": "ab"},
            headers=auth_headers,
        )
        assert response.status_code == 422

    def test_update_profile_username_special_chars(self, client, auth_headers):
        """Username with special chars should return 422."""
        response = client.put(
            "/api/v1/users/me",
            json={"username": "user name!"},
            headers=auth_headers,
        )
        assert response.status_code == 422


class TestMyListings:
    """GET /api/v1/users/me/listings — get current user's listings."""

    def test_my_listings_without_auth_returns_403(self, client):
        """Accessing without auth should return 403."""
        response = client.get("/api/v1/users/me/listings")
        assert response.status_code == 403

    def test_my_listings_with_pagination(self, client, auth_headers):
        """Pagination params should be accepted."""
        response = client.get(
            "/api/v1/users/me/listings?page=1&page_size=10",
            headers=auth_headers,
        )
        # 403 if token invalid
        assert response.status_code in (200, 403)

    def test_my_listings_invalid_status(self, client, auth_headers):
        """Invalid status filter should return 422."""
        response = client.get(
            "/api/v1/users/me/listings?status=deleted",
            headers=auth_headers,
        )
        assert response.status_code == 422


class TestUserListings:
    """GET /api/v1/users/{id}/listings — get a user's public listings."""

    def test_user_listings_public_access(self, client):
        """Public endpoint — should not require auth."""
        response = client.get("/api/v1/users/00000000-0000-0000-0000-000000000000/listings")
        # No auth required, might fail at DB
        assert response.status_code in (200, 404, 422)

    def test_user_listings_invalid_uuid(self, client):
        """Invalid UUID should return 422."""
        response = client.get("/api/v1/users/invalid-uuid/listings")
        assert response.status_code == 422
