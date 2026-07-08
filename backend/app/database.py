"""
SG CampusSwap — Database Setup.
Async SQLAlchemy engine + session factory + Base class.
Uses lazy initialization so imports don't fail without a DB connection.
"""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

# ── Lazy engine / session — created on first use ────────
_engine = None
_async_session: async_sessionmaker[AsyncSession] | None = None


def get_engine():
    """Return (or create) the async SQLAlchemy engine."""
    global _engine
    if _engine is None:
        _engine = create_async_engine(
            settings.DATABASE_URL,
            echo=settings.DEBUG,
            pool_size=settings.DB_POOL_SIZE,
            max_overflow=settings.DB_MAX_OVERFLOW,
        )
    return _engine


def get_async_session() -> async_sessionmaker[AsyncSession]:
    """Return (or create) the async session factory."""
    global _async_session
    if _async_session is None:
        _async_session = async_sessionmaker(
            get_engine(), class_=AsyncSession, expire_on_commit=False
        )
    return _async_session


class Base(DeclarativeBase):
    """Base class for all ORM models."""
    pass


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI dependency — yields an async database session."""
    session = get_async_session()()
    async with session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
