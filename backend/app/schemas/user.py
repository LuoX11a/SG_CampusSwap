"""
SG CampusSwap — Pydantic Schemas: User (Request / Response).
"""

import uuid
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, field_validator


# ── Auth ─────────────────────────────────────────────────

class UserRegisterRequest(BaseModel):
    email: str = Field(..., max_length=255, description="University email address")
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=128)
    university: str = Field(..., max_length=100)
    campus: str | None = None

    @field_validator("password")
    @classmethod
    def password_strength(cls, v: str) -> str:
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        return v


class UserLoginRequest(BaseModel):
    email: str = Field(..., max_length=255)
    password: str = Field(..., max_length=128)


class EmailVerifyRequest(BaseModel):
    email: str = Field(..., max_length=255)
    code: str = Field(..., min_length=6, max_length=6)


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    refresh_token: str


# ── User Profile ────────────────────────────────────────

class UserProfileResponse(BaseModel):
    id: uuid.UUID
    username: str
    university: str
    campus: str | None
    avatar_url: str | None
    rating_avg: float
    created_at: datetime

    model_config = {"from_attributes": True}


class UserPublicResponse(BaseModel):
    id: uuid.UUID
    username: str
    university: str
    campus: str | None
    avatar_url: str | None
    rating_avg: float

    model_config = {"from_attributes": True}


class UserUpdateRequest(BaseModel):
    username: str | None = Field(None, min_length=3, max_length=50)
    university: str | None = None
    campus: str | None = None
