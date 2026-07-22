"""
Image Upload API Routes

POST   /api/v1/upload/image     — Upload a single image
POST   /api/v1/upload/images    — Upload multiple images (max 5)
DELETE /api/v1/upload/image     — Delete an uploaded image
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from pydantic import BaseModel
from app.models.user import User
from app.api.v1.auth import get_current_user
from app.services.upload_service import upload_to_cloudinary, delete_from_cloudinary

router = APIRouter()

ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp", "image/heic"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


class UploadResponse(BaseModel):
    url: str
    public_id: str
    width: int
    height: int
    format: str
    bytes: int


class MultiUploadResponse(BaseModel):
    images: List[UploadResponse]
    count: int


class DeleteRequest(BaseModel):
    public_id: str


@router.post("/image", response_model=UploadResponse)
async def upload_image(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
):
    """Upload a single image. Max 5MB, JPG/PNG/WebP/HEIC."""
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {file.content_type}. Allowed: {', '.join(ALLOWED_TYPES)}",  # noqa: E501
        )

    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File too large: {len(contents)} bytes. Max: {MAX_FILE_SIZE} bytes (5 MB)",
        )

    result = await upload_to_cloudinary(contents, file.filename, current_user.id)

    return UploadResponse(
        url=result["secure_url"],
        public_id=result["public_id"],
        width=result["width"],
        height=result["height"],
        format=result["format"],
        bytes=result["bytes"],
    )


@router.post("/images", response_model=MultiUploadResponse)
async def upload_images(
    files: List[UploadFile] = File(..., max_length=5),
    current_user: User = Depends(get_current_user),
):
    """Upload up to 5 images at once."""
    if len(files) > 5:
        raise HTTPException(status_code=400, detail="Maximum 5 images allowed")

    results = []
    for file in files:
        if file.content_type not in ALLOWED_TYPES:
            continue

        contents = await file.read()
        if len(contents) > MAX_FILE_SIZE:
            continue

        result = await upload_to_cloudinary(contents, file.filename, current_user.id)
        results.append(
            UploadResponse(
                url=result["secure_url"],
                public_id=result["public_id"],
                width=result["width"],
                height=result["height"],
                format=result["format"],
                bytes=result["bytes"],
            )
        )

    return MultiUploadResponse(images=results, count=len(results))


@router.delete("/image")
async def delete_image(
    data: DeleteRequest,
    current_user: User = Depends(get_current_user),
):
    """Delete an uploaded image by public_id."""
    success = await delete_from_cloudinary(data.public_id)
    if not success:
        raise HTTPException(status_code=404, detail="Image not found or already deleted")

    return {"message": "Image deleted successfully"}
