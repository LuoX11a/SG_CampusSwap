"""
Auth API Routes

POST /api/v1/auth/register  — Register with university email
POST /api/v1/auth/verify    — Verify email with 6-digit code
POST /api/v1/auth/login     — Login, get JWT tokens
POST /api/v1/auth/refresh   — Refresh expired access token
POST /api/v1/auth/logout    — Invalidate refresh token
GET  /api/v1/auth/me        — Get current user info
"""

from datetime import datetime, timedelta, timezone
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr, Field, field_validator
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database import get_db
from app.models.user import User
from app.models.review import EmailVerification, RefreshToken
from app.services.auth_service import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_token,
    generate_verification_code,
    is_allowed_domain,
)

router = APIRouter()
security = HTTPBearer()


# ─── Request Schemas ───────────────────────────────────────────

class RegisterRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, pattern=r"^[a-zA-Z0-9_]+$")
    email: EmailStr
    university: str = Field(..., min_length=2)
    campus: str = Field(..., min_length=2)
    password: str = Field(..., min_length=8)
    confirm_password: str

    @property
    def password_is_strong(self) -> bool:
        return (
            len(self.password) >= 8
            and any(c.isupper() for c in self.password)
            and any(c.isdigit() for c in self.password)
        )


class VerifyEmailRequest(BaseModel):
    email: EmailStr
    code: str = Field(..., min_length=6, max_length=6)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RefreshRequest(BaseModel):
    refresh_token: str


# ─── Response Schemas ──────────────────────────────────────────

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int = 1800


class UserResponse(BaseModel):
    id: str
    email: str
    username: str
    university: str
    campus: str
    avatar_url: Optional[str] = None
    rating_avg: Optional[float] = None
    rating_count: int = 0
    is_verified: bool

    @field_validator('id', mode='before')
    @classmethod
    def coerce_id(cls, v):
        return str(v)

    class Config:
        from_attributes = True


# ─── Auth Dependency ───────────────────────────────────────────

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> User:
    """Extract and validate JWT, return current User."""
    token = credentials.credentials
    payload = decode_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")

    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return user


# ─── Routes ────────────────────────────────────────────────────

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(req: RegisterRequest, db: AsyncSession = Depends(get_db)):
    """Register a new user with university email."""
    if req.password != req.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    if not req.password_is_strong:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters with 1 uppercase letter and 1 digit",
        )

    if not is_allowed_domain(req.email):
        raise HTTPException(
            status_code=400,
            detail="Please use your university email address (.edu or .edu.sg domain)",
        )

    result = await db.execute(select(User).where(User.email == req.email))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Email already registered")

    result = await db.execute(select(User).where(User.username == req.username))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Username already taken")

    user = User(
        id=uuid4(),
        email=req.email,
        username=req.username,
        password_hash=hash_password(req.password),
        university=req.university,
        campus=req.campus,
        is_verified=False,
    )
    db.add(user)

    code = generate_verification_code()
    verification = EmailVerification(
        id=uuid4(),
        email=req.email,
        code=code,
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=15),
    )
    db.add(verification)

    # In DEBUG mode, auto-verify the user so they can log in immediately
    if settings.DEBUG:
        user.is_verified = True
        verification.is_used = True

    await db.commit()

    response = {
        "message": f"Verification code sent to {req.email}",
        "email": req.email,
    }
    if settings.DEBUG:
        response["code"] = code
        response["note"] = "DEBUG mode: user auto-verified"
    return response


@router.post("/verify")
async def verify_email(req: VerifyEmailRequest, db: AsyncSession = Depends(get_db)):
    """Verify email with 6-digit code and activate account."""
    result = await db.execute(
        select(EmailVerification)
        .where(EmailVerification.email == req.email)
        .where(EmailVerification.code == req.code)
        .where(EmailVerification.is_used == False)
        .where(EmailVerification.expires_at > datetime.now(timezone.utc))
        .order_by(EmailVerification.created_at.desc())
    )
    verification = result.scalar_one_or_none()

    if not verification:
        raise HTTPException(status_code=400, detail="Invalid or expired verification code")

    verification.is_used = True

    result = await db.execute(select(User).where(User.email == req.email))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_verified = True
    await db.commit()

    return {"message": "Email verified successfully. You can now log in."}


@router.post("/login", response_model=TokenResponse)
async def login(req: LoginRequest, db: AsyncSession = Depends(get_db)):
    """Login and receive JWT access + refresh tokens."""
    result = await db.execute(select(User).where(User.email == req.email))
    user = result.scalar_one_or_none()

    if not user or not verify_password(req.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not user.is_verified and not settings.DEBUG:
        raise HTTPException(status_code=403, detail="Please verify your email before logging in")

    access_token = create_access_token(user.id)
    refresh_token_str = create_refresh_token(user.id)

    refresh_token = RefreshToken(
        id=uuid4(),
        user_id=user.id,
        token=refresh_token_str,
        expires_at=datetime.now(timezone.utc) + timedelta(days=7),
    )
    db.add(refresh_token)
    await db.commit()

    return TokenResponse(access_token=access_token, refresh_token=refresh_token_str)


@router.post("/refresh", response_model=TokenResponse)
async def refresh(req: RefreshRequest, db: AsyncSession = Depends(get_db)):
    """Get a new access token using a valid refresh token."""
    result = await db.execute(
        select(RefreshToken)
        .where(RefreshToken.token == req.refresh_token)
        .where(RefreshToken.expires_at > datetime.now(timezone.utc))
        .where(RefreshToken.is_revoked == False)
    )
    token_record = result.scalar_one_or_none()

    if not token_record:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")

    result = await db.execute(select(User).where(User.id == token_record.user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    access_token = create_access_token(user.id)
    new_refresh = create_refresh_token(user.id)

    token_record.is_revoked = True
    refresh_token = RefreshToken(
        id=uuid4(),
        user_id=user.id,
        token=new_refresh,
        expires_at=datetime.now(timezone.utc) + timedelta(days=7),
    )
    db.add(refresh_token)
    await db.commit()

    return TokenResponse(access_token=access_token, refresh_token=new_refresh)


@router.post("/logout", status_code=204)
async def logout(
    req: RefreshRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Invalidate the refresh token."""
    result = await db.execute(
        select(RefreshToken).where(RefreshToken.token == req.refresh_token)
    )
    token_record = result.scalar_one_or_none()
    if token_record:
        token_record.is_revoked = True
        await db.commit()

    return None


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    """Get the currently authenticated user's profile."""
    return current_user
