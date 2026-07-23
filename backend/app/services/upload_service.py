"""
Local File Upload Service

Stores uploaded images on the local filesystem and serves them
via FastAPI StaticFiles.  Falls back to placeholder URLs when
the uploads directory is not writable (e.g. Render ephemeral storage).
"""

import os
import uuid
from typing import Dict, Any

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "uploads")
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".heic"}


def _ensure_upload_dir() -> bool:
    """Create uploads directory if it doesn't exist. Returns True on success."""
    try:
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        return True
    except OSError:
        return False


async def upload_to_cloudinary(
    file_bytes: bytes,
    original_filename: str,
    user_id: str,
    folder: str = "sg-campusswap",
) -> Dict[str, Any]:
    """
    Save an uploaded image to local storage.

    Uses the same function signature as the old Cloudinary-based
    implementation so callers (api/v1/upload.py) don't need to change.
    """
    ext = ""
    if "." in original_filename:
        ext = "." + original_filename.split(".")[-1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            ext = ".jpg"

    if _ensure_upload_dir():
        # Save to local filesystem
        file_id = uuid.uuid4().hex[:12]
        filename = f"{file_id}{ext}"
        filepath = os.path.join(UPLOAD_DIR, filename)
        try:
            with open(filepath, "wb") as f:
                f.write(file_bytes)
            base_url = os.environ.get("API_BASE_URL", "http://localhost:8000")
            return {
                "secure_url": f"{base_url}/uploads/{filename}",
                "public_id": filename,
                "width": 0,
                "height": 0,
                "format": ext.lstrip("."),
                "bytes": len(file_bytes),
            }
        except OSError:
            pass

    # Fallback: placeholder image (colored SVG via data URI would be better,
    # but this keeps the app working when filesystem is read-only).
    return {
        "secure_url": (
            "https://placehold.co/400x300/e2e8f0/64748b"
            "?text=SG+CampusSwap"
        ),
        "public_id": f"placeholder/{uuid.uuid4().hex[:8]}",
        "width": 400,
        "height": 300,
        "format": ext.lstrip(".") or "jpg",
        "bytes": len(file_bytes),
    }


async def delete_from_cloudinary(public_id: str) -> bool:
    """Delete a locally stored image by filename."""
    filepath = os.path.join(UPLOAD_DIR, public_id)
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            return True
        return False
    except OSError:
        return False


def get_image_url(public_id: str, width: int = 400, height: int = 300) -> str:
    """Return the local URL for an uploaded image."""
    base_url = os.environ.get("API_BASE_URL", "")
    return f"{base_url}/uploads/{public_id}"
