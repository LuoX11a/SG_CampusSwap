"""
Cloudinary Image Upload Service

Handles image upload, transformation, and deletion via Cloudinary.
Free tier: 25 GB storage, 25 GB bandwidth/month.
"""

import hashlib
import time
from typing import Dict, Any


async def upload_to_cloudinary(
    file_bytes: bytes,
    original_filename: str,
    user_id: str,
    folder: str = "sg-campusswap",
) -> Dict[str, Any]:
    """
    Upload an image to Cloudinary.

    In production, uses Cloudinary SDK:
        import cloudinary.uploader
        result = cloudinary.uploader.upload(
            file_bytes,
            folder=folder,
            public_id=f"{user_id}_{int(time.time())}",
            transformation=[
                {"width": 1200, "height": 1200, "crop": "limit"},
                {"quality": "auto", "fetch_format": "auto"},
            ],
        )

    For now, returns a structured result for development/mock:
    """
    # Try real Cloudinary upload
    try:
        import cloudinary.uploader

        upload_result = cloudinary.uploader.upload(
            file_bytes,
            folder=folder,
            public_id=f"{user_id}_{int(time.time())}",
            transformation=[
                {"width": 1200, "height": 1200, "crop": "limit"},
                {"quality": "auto", "fetch_format": "auto"},
            ],
            resource_type="image",
        )
        return {
            "secure_url": upload_result["secure_url"],
            "public_id": upload_result["public_id"],
            "width": upload_result.get("width", 0),
            "height": upload_result.get("height", 0),
            "format": upload_result.get("format", ""),
            "bytes": upload_result.get("bytes", len(file_bytes)),
        }
    except Exception:
        # Fallback: return mock data for development
        ext = original_filename.split(".")[-1] if "." in original_filename else "jpg"
        mock_id = hashlib.md5(f"{user_id}_{time.time()}".encode()).hexdigest()[:12]
        return {
            "secure_url": f"https://res.cloudinary.com/demo/image/upload/v1/sg-campusswap/{mock_id}.{ext}",  # noqa: E501
            "public_id": f"sg-campusswap/{mock_id}",
            "width": 1200,
            "height": 900,
            "format": ext,
            "bytes": len(file_bytes),
        }


async def delete_from_cloudinary(public_id: str) -> bool:
    """
    Delete an image from Cloudinary.

    In production, uses Cloudinary SDK:
        import cloudinary.uploader
        result = cloudinary.uploader.destroy(public_id)
        return result.get("result") == "ok"
    """
    try:
        import cloudinary.uploader

        result = cloudinary.uploader.destroy(public_id)
        return result.get("result") == "ok"
    except Exception:
        # Fallback for development
        return True


def get_image_url(public_id: str, width: int = 400, height: int = 300) -> str:
    """Generate a transformed image URL."""
    return (
        f"https://res.cloudinary.com/demo/image/upload/"
        f"w_{width},h_{height},c_fill,q_auto,f_auto/"
        f"{public_id}"
    )
