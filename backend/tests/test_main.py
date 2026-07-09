"""
Tests for the FastAPI application entry point.
"""

import pytest


class TestRootEndpoint:
    """Health check endpoint tests (no database required)."""

    @pytest.mark.asyncio
    async def test_root_returns_200(self, async_client):
        """The root endpoint should return HTTP 200."""
        response = await async_client.get("/")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_root_returns_json(self, async_client):
        """The root endpoint should return JSON with expected keys."""
        response = await async_client.get("/")
        data = response.json()
        assert "app" in data
        assert "version" in data
        assert data["status"] == "running"

    @pytest.mark.asyncio
    async def test_app_title_matches_settings(self, async_client):
        """The app title should match the configured setting."""
        response = await async_client.get("/")
        data = response.json()
        assert data["app"] == "SG CampusSwap API"

    @pytest.mark.asyncio
    async def test_docs_endpoint_accessible(self, async_client):
        """The Swagger docs endpoint should be accessible."""
        response = await async_client.get("/docs")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_redoc_endpoint_accessible(self, async_client):
        """The ReDoc endpoint should be accessible."""
        response = await async_client.get("/redoc")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_openapi_schema(self, async_client):
        """The OpenAPI schema should be readable."""
        response = await async_client.get("/openapi.json")
        assert response.status_code == 200
        schema = response.json()
        assert "openapi" in schema
        assert "paths" in schema
        assert "/" in schema["paths"]
