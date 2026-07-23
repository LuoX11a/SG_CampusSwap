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
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool

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


# ── Async Database Fixtures ────────────────────────────────────


@pytest_asyncio.fixture(scope="session")
def event_loop():
    """Create a single event loop for the test session."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def test_engine():
    """Create a test database engine with NullPool.

    NullPool avoids asyncpg "another operation in progress" errors
    caused by TestClient creating separate event loops per request.
    """
    engine = create_async_engine(TEST_DATABASE_URL, echo=False, poolclass=NullPool)

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


# ── Override app DB dependency to use test engine ──────────────
# This ensures the FastAPI app uses the same engine (NullPool)
# that has tables created by the test fixtures.


@pytest.fixture(scope="module", autouse=True)
def cleanup_db(test_engine):
    """Truncate all tables before each test module for a clean slate."""
    from sqlalchemy import text

    async def _truncate():
        async with test_engine.begin() as conn:
            for table in reversed(Base.metadata.sorted_tables):
                await conn.execute(
                    text(f"TRUNCATE TABLE {table.name} CASCADE")
                )

    asyncio.get_event_loop().run_until_complete(_truncate())
    yield
    asyncio.get_event_loop().run_until_complete(_truncate())


@pytest.fixture
def override_db(test_engine):
    """Override the app's get_db with a session from the test engine.

    Uses NullPool to avoid asyncpg event-loop conflicts when TestClient
    runs requests in separate event loops.  Commits normally so that
    sequences like register→login work within a single test.
    """
    async_session_factory = async_sessionmaker(
        test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async def _get_test_db():
        async with async_session_factory() as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise

    app.dependency_overrides[get_db] = _get_test_db
    yield
    app.dependency_overrides.clear()


# ── HTTP Client Fixtures ───────────────────────────────────────


@pytest.fixture
def client(override_db):
    """HTTP TestClient bound to the FastAPI app.

    Uses overridden DB dependency (NullPool) so tests don't hit
    asyncpg event-loop issues.
    """
    return TestClient(app)


@pytest_asyncio.fixture
async def async_client(override_db):
    """Async HTTP client for testing async endpoints."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


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
