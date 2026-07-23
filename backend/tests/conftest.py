"""
Shared fixtures for backend tests.

Fixtures:
    client       — TestClient (no database)
    async_client — httpx.AsyncClient for async test calls
    test_db      — Async SQLAlchemy session (requires running PostgreSQL)

Usage:
    pytest tests/ -v                          # Run all tests
    pytest tests/ -v -k "test_root"           # Run only health-check tests
    pytest tests/ -v --no-header              # Cleaner output
"""

import asyncio
import os
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# Enable DEBUG mode for tests (bypasses email verification)
os.environ["DEBUG"] = "true"

from app.main import app
from app.database import Base, get_db

# ── Test Database URL ──────────────────────────────────────────
# Default: local PostgreSQL (docker-compose or CI postgres:15 service).
# NOTE: Neon pooled connections (with "-pooler" in host) use PgBouncer
# which does NOT support DDL (CREATE TABLE / DROP TABLE).
# Use a non-pooled connection or local Postgres for running tests.
TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/sg_campusswap_test",
)


# ── Synchronous TestClient (no DB needed) ──────────────────────


@pytest.fixture
def client(test_engine):
    """HTTP TestClient bound to the FastAPI app.

    Depends on test_engine so database tables are created before
    any HTTP request hits the database.
    """
    return TestClient(app)


# ── Async HTTP Client ──────────────────────────────────────────


@pytest_asyncio.fixture
async def async_client(test_engine):
    """Async HTTP client for testing async endpoints.

    Depends on test_engine so database tables are created before
    any HTTP request hits the database.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


# ── Async Database Fixtures ────────────────────────────────────


@pytest_asyncio.fixture(scope="session")
def event_loop():
    """Create a single event loop for the test session."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def test_engine():
    """Create a test database engine."""
    engine = create_async_engine(TEST_DATABASE_URL, echo=False)

    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield engine

    # Drop all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await engine.dispose()


@pytest_asyncio.fixture
async def test_db(test_engine) -> AsyncGenerator[AsyncSession, None]:
    """Provide an async database session for a single test.

    Each test gets a fresh transaction that is rolled back after the test,
    keeping tests isolated from each other.
    """
    async_session_factory = async_sessionmaker(
        test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session_factory() as session:
        async with session.begin():
            yield session
            await session.rollback()


# ── Authenticated Client Fixtures ───────────────────────────────

TEST_USER = {
    "email": "test.student@e.ntu.edu.sg",
    "username": "teststudent",
    "password": "TestPass123",
    "confirm_password": "TestPass123",
    "university": "Nanyang Technological University",
    "campus": "NTU Main Campus",
}


@pytest.fixture
def registered_user():
    """Return test user credentials."""
    return TEST_USER.copy()


@pytest.fixture
def auth_headers(client):
    """Register, verify, and login to get a real JWT token."""
    # Register
    client.post("/api/v1/auth/register", json=TEST_USER)
    # Verify email directly via DB is complex; skip verification for tests
    # Login
    resp = client.post(
        "/api/v1/auth/login",
        json={
            "email": TEST_USER["email"],
            "password": TEST_USER["password"],
        },
    )
    if resp.status_code == 200:
        token = resp.json()["access_token"]
        return {"Authorization": f"Bearer {token}"}
    # Fallback: if login fails (e.g., user already exists but not verified),
    # return a placeholder that will fail auth — tests check for 401
    return {"Authorization": "Bearer test-token-placeholder"}
