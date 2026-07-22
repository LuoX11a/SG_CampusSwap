"""
Tests for database module.
"""

import pytest

from app.database import Base, get_async_session, get_engine


class TestEngine:
    """Tests for the database engine factory."""

    @pytest.mark.asyncio
    async def test_get_engine_returns_non_null(self):
        """get_engine() should return an engine instance."""
        engine = get_engine()
        assert engine is not None

    @pytest.mark.asyncio
    async def test_get_engine_is_singleton(self):
        """Calling get_engine() twice should return the same instance."""
        e1 = get_engine()
        e2 = get_engine()
        assert e1 is e2


class TestSessionFactory:
    """Tests for the async session factory."""

    @pytest.mark.asyncio
    async def test_get_async_session_returns_factory(self):
        """get_async_session() should return a session factory."""
        factory = get_async_session()
        assert factory is not None

    @pytest.mark.asyncio
    async def test_get_async_session_is_singleton(self):
        """Calling get_async_session() twice should return the same instance."""
        f1 = get_async_session()
        f2 = get_async_session()
        assert f1 is f2


class TestBase:
    """Tests for the declarative base."""

    def test_base_has_metadata(self):
        """Base should have a MetaData object."""
        assert Base.metadata is not None
