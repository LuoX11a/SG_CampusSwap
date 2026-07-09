"""
Shared fixtures for backend tests.
"""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """HTTP test client bound to the FastAPI app."""
    return TestClient(app)
