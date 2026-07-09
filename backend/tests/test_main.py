"""
Tests for the FastAPI application entry point.
"""


class TestRootEndpoint:
    """Health check endpoint tests (no database required)."""

    def test_root_returns_200(self, client):
        """The root endpoint should return HTTP 200."""
        response = client.get("/")
        assert response.status_code == 200

    def test_root_returns_json(self, client):
        """The root endpoint should return JSON with expected keys."""
        response = client.get("/")
        data = response.json()
        assert "app" in data
        assert "version" in data
        assert data["status"] == "running"

    def test_app_title_matches_settings(self, client):
        """The app title should match the configured setting."""
        response = client.get("/")
        data = response.json()
        assert data["app"] == "SG CampusSwap API"

    def test_docs_endpoint_accessible(self, client):
        """The Swagger docs endpoint should be accessible."""
        response = client.get("/docs")
        assert response.status_code == 200

    def test_redoc_endpoint_accessible(self, client):
        """The ReDoc endpoint should be accessible."""
        response = client.get("/redoc")
        assert response.status_code == 200

    def test_openapi_schema(self, client):
        """The OpenAPI schema should be readable."""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        schema = response.json()
        assert "openapi" in schema
        assert "paths" in schema
        assert "/" in schema["paths"]
