"""
SG CampusSwap — FastAPI Application Entry Point.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup / shutdown lifecycle."""
    # Startup: create tables (dev only — use Alembic in production)
    # from app.database import engine, Base
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown: dispose engine
    # await engine.dispose()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


# ── Router Registration (uncomment as modules are built) ──
# from app.api.v1 import auth, items, users, upload, reviews
# app.include_router(auth.router, prefix=settings.API_V1_PREFIX)
# app.include_router(items.router, prefix=settings.API_V1_PREFIX)
# app.include_router(users.router, prefix=settings.API_V1_PREFIX)
# app.include_router(upload.router, prefix=settings.API_V1_PREFIX)
# app.include_router(reviews.router, prefix=settings.API_V1_PREFIX)
