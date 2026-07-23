"""
API v1 Router Registry

All API endpoints are registered here under /api/v1/.
"""

from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.items import router as items_router
from app.api.v1.users import router as users_router
from app.api.v1.upload import router as upload_router
from app.api.v1.reviews import router as reviews_router
from app.api.v1.search import router as search_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(items_router, prefix="/items", tags=["Items"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(upload_router, prefix="/upload", tags=["Upload"])
api_router.include_router(reviews_router, prefix="/reviews", tags=["Reviews"])
api_router.include_router(search_router, prefix="/search", tags=["Search"])
