"""
SG CampusSwap — FastAPI Application Entry Point.

Deploy: Render (backend) + Vercel (frontend) + Neon PostgreSQL
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup / shutdown lifecycle — pre-warms the database engine."""
    import logging
    logger = logging.getLogger("uvicorn")

    try:
        logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
        logger.info(f"Environment: {settings.ENVIRONMENT}")
        logger.info(f"CORS origins: {settings.CORS_ORIGINS}")

        from sqlalchemy import text
        from app.database import get_engine
        engine = get_engine()
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        logger.info("Database engine warmed up and connected")
    except Exception as exc:
        logger.error(f"Lifespan startup error: {type(exc).__name__}: {exc}")

    yield

    try:
        from app.database import get_engine
        engine = get_engine()
        await engine.dispose()
        logger.info("Database engine disposed")
    except Exception:
        pass


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# CORS — allow Vercel frontend + local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Health Check (used by Render to detect ready state) ──

@app.get("/")
async def root():
    """Public health check."""
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "env": settings.ENVIRONMENT,
    }


@app.get("/health")
async def health():
    """Render health check — verifies database connectivity."""
    try:
        from app.database import get_engine
        from sqlalchemy import text

        engine = get_engine()
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": str(e)}


# ── Router Registration ──
# Each router is imported individually — if one fails, others still load.
import importlib
import logging
import traceback

_logger = logging.getLogger("uvicorn")
ROUTER_NAMES = ["auth", "items", "users", "upload", "reviews", "search", "chat"]

router_failures = []
for name in ROUTER_NAMES:
    try:
        mod = importlib.import_module(f"app.api.v1.{name}")
        app.include_router(mod.router, prefix=f"{settings.API_V1_PREFIX}/{name}", tags=[name])
        _logger.info(f"✅ router loaded: {name}")
    except Exception as exc:
        router_failures.append(name)
        _logger.error(f"❌ router {name} FAILED: {type(exc).__name__}: {exc}")
        _logger.error(traceback.format_exc())

if router_failures:
    _logger.warning(f"Failed routers: {router_failures}")
else:
    _logger.info("All routers loaded successfully")
