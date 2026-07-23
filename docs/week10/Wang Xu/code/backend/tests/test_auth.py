"""
Tests for Auth API endpoints.

POST /api/v1/auth/register
POST /api/v1/auth/verify
POST /api/v1/auth/login
POST /api/v1/auth/refresh
POST /api/v1/auth/logout
GET  /api/v1/auth/me
"""

import pytest


class TestRegister:
    """Registration endpoint tests."""

    def test_register_missing_fields_returns_422(self, client):
        """POST /api/v1/auth/register with empty body returns 422."""
        response = client.post("/api/v1/auth/register", json={})
        assert response.status_code == 422

    def test_register_password_mismatch(self, client):
        """Passwords that don't match should return 400."""
        payload = {
            "email": "test@e.ntu.edu.sg",
            "username": "testuser1",
            "password": "StrongPass1",
            "confirm_password": "DifferentPass1",
            "university": "NTU",
            "campus": "Main Campus",
        }
        response = client.post("/api/v1/auth/register", json=payload)
        assert response.status_code == 400
        assert "do not match" in response.json()["detail"].lower()

    def test_register_weak_password_returns_400(self, client):
        """Password without uppercase + digit should be rejected."""
        payload = {
            "email": "test@e.ntu.edu.sg",
            "username": "testuser2",
            "password": "weakpassword",
            "confirm_password": "weakpassword",
            "university": "NTU",
            "campus": "Main Campus",
        }
        response = client.post("/api/v1/auth/register", json=payload)
        assert response.status_code == 400
        assert "password" in response.json()["detail"].lower()

    def test_register_non_edu_email_rejected(self, client):
        """Email not in whitelist domain should be rejected."""
        payload = {
            "email": "student@gmail.com",
            "username": "testuser3",
            "password": "StrongPass1",
            "confirm_password": "StrongPass1",
            "university": "NTU",
            "campus": "Main Campus",
        }
        response = client.post("/api/v1/auth/register", json=payload)
        assert response.status_code == 400
        assert "university email" in response.json()["detail"].lower()

    def test_register_short_username_rejected(self, client):
        """Username shorter than 3 chars should be rejected."""
        payload = {
            "email": "ab@e.ntu.edu.sg",
            "username": "ab",
            "password": "StrongPass1",
            "confirm_password": "StrongPass1",
            "university": "NTU",
            "campus": "Main Campus",
        }
        response = client.post("/api/v1/auth/register", json=payload)
        assert response.status_code == 422


class TestLogin:
    """Login endpoint tests."""

    def test_login_missing_fields_returns_422(self, client):
        """POST /api/v1/auth/login with empty body returns 422."""
        response = client.post("/api/v1/auth/login", json={})
        assert response.status_code == 422

    def test_login_invalid_credentials(self, client):
        """Non-existent user should get 401."""
        payload = {"email": "nonexistent@e.ntu.edu.sg", "password": "SomePass1"}
        response = client.post("/api/v1/auth/login", json=payload)
        assert response.status_code == 401

    def test_login_invalid_email_format(self, client):
        """Invalid email format should return 422."""
        payload = {"email": "not-an-email", "password": "SomePass1"}
        response = client.post("/api/v1/auth/login", json=payload)
        assert response.status_code == 422


class TestVerifyEmail:
    """Email verification endpoint tests."""

    def test_verify_missing_fields_returns_422(self, client):
        """POST /api/v1/auth/verify with empty body returns 422."""
        response = client.post("/api/v1/auth/verify", json={})
        assert response.status_code == 422

    def test_verify_invalid_code_format(self, client):
        """Code shorter than 6 digits should return 422."""
        payload = {"email": "test@e.ntu.edu.sg", "code": "123"}
        response = client.post("/api/v1/auth/verify", json=payload)
        assert response.status_code == 422

    def test_verify_wrong_code(self, client):
        """Wrong verification code should return 400."""
        payload = {"email": "test@e.ntu.edu.sg", "code": "000000"}
        response = client.post("/api/v1/auth/verify", json=payload)
        # 400 because no such pending verification exists in test DB
        assert response.status_code in (400, 404)


class TestRefreshToken:
    """Token refresh endpoint tests."""

    def test_refresh_missing_fields_returns_422(self, client):
        """POST /api/v1/auth/refresh with empty body returns 422."""
        response = client.post("/api/v1/auth/refresh", json={})
        assert response.status_code == 422

    def test_refresh_invalid_token(self, client):
        """Invalid refresh token should return 401."""
        payload = {"refresh_token": "invalid-token-string"}
        response = client.post("/api/v1/auth/refresh", json=payload)
        assert response.status_code == 401


class TestLogout:
    """Logout endpoint tests."""

    def test_logout_without_token_returns_403(self, client):
        """POST /api/v1/auth/logout without auth header returns 403."""
        payload = {"refresh_token": "some-token"}
        response = client.post("/api/v1/auth/logout", json=payload)
        assert response.status_code == 403


class TestGetMe:
    """Get current user endpoint tests."""

    def test_me_without_token_returns_403(self, client):
        """GET /api/v1/auth/me without auth header returns 403."""
        response = client.get("/api/v1/auth/me")
        assert response.status_code == 403


class TestAuthSchemas:
    """Validation of auth request schemas."""

    def test_register_username_special_chars_rejected(self, client):
        """Username with special characters should be rejected."""
        payload = {
            "email": "test@e.ntu.edu.sg",
            "username": "user name!",
            "password": "StrongPass1",
            "confirm_password": "StrongPass1",
            "university": "NTU",
            "campus": "Main Campus",
        }
        response = client.post("/api/v1/auth/register", json=payload)
        assert response.status_code == 422

    def test_register_long_username_rejected(self, client):
        """Username > 20 chars should be rejected."""
        payload = {
            "email": "test@e.ntu.edu.sg",
            "username": "a" * 21,
            "password": "StrongPass1",
            "confirm_password": "StrongPass1",
            "university": "NTU",
            "campus": "Main Campus",
        }
        response = client.post("/api/v1/auth/register", json=payload)
        assert response.status_code == 422

    @pytest.mark.parametrize(
        "email",
        [
            "test@u.nus.edu",
            "test@nus.edu.sg",
            "test@e.ntu.edu.sg",
            "test@smu.edu.sg",
            "test@sutd.edu.sg",
            "test@suss.edu.sg",
            "test@sit.edu.sg",
        ],
    )
    def test_allowed_domains_accepted(self, client, email):
        """Valid university domains should pass domain check (schema level)."""
        payload = {
            "email": email,
            "username": "validuser",
            "password": "StrongPass1",
            "confirm_password": "StrongPass1",
            "university": "Test University",
            "campus": "Main Campus",
        }
        # Domain check happens AFTER schema validation
        # Schema validation should pass for these emails
        response = client.post("/api/v1/auth/register", json=payload)
        # Will fail at domain check or DB level, but NOT at schema validation (422)
        assert response.status_code != 422
