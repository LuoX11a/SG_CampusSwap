"""
SG CampusSwap — Auth Service.
Handles: registration (domain whitelist), email verification, login, JWT tokens.
"""

import random
import string
from uuid import UUID, uuid4
from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.models.review import EmailVerification
from app.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ── Password Hashing ─────────────────────────────────────


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


# ── JWT ────────────────────────────────


def create_access_token(user_id: UUID) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": str(user_id), "exp": expire, "type": "access", "jti": uuid4().hex}
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)


def create_refresh_token(user_id: UUID) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    payload = {"sub": str(user_id), "exp": expire, "type": "refresh", "jti": uuid4().hex}
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )


# ── Email Domain Validation ────────────


def extract_domain(email: str) -> str:
    """Extract the domain portion from an email address."""
    return email.split("@", 1)[1].lower()


def is_allowed_domain(email: str) -> bool:
    """Check if the email domain is in the university whitelist."""
    domain = extract_domain(email)
    return domain in settings.allowed_domains_list


# ── Verification Code ──────────────────


def generate_verification_code() -> str:
    """Generate a random 6-digit verification code."""
    return "".join(random.choices(string.digits, k=settings.VERIFICATION_CODE_LENGTH))


async def send_verification_email(email: str, code: str) -> None:
    """
    Send a verification code to the user's email.
    Uses SMTP (SendGrid) for delivery.
    """
    # TODO: Implement SMTP sending via SendGrid
    # For now, log the code during development
    if settings.DEBUG:
        print(f"[DEV] Verification code for {email}: {code}")


# ── Registration Flow ──────────────────


async def register_user(
    db: AsyncSession, email: str, username: str, password: str, university: str, campus: str | None
) -> User:
    """Register a new user. Validates email domain whitelist first."""
    # 1. Check domain whitelist
    if not is_allowed_domain(email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please use your university email address.",
        )

    # 2. Check duplicate email
    existing = await db.execute(select(User).where(User.email == email))
    if existing.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists.",
        )

    # 3. Check duplicate username
    existing_user = await db.execute(select(User).where(User.username == username))
    if existing_user.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This username is already taken.",
        )

    # 4. Create user
    user = User(
        email=email,
        username=username,
        password_hash=hash_password(password),
        university=university,
        campus=campus,
    )
    db.add(user)
    await db.flush()

    # 5. Generate & send verification code
    code = generate_verification_code()
    verification = EmailVerification(
        email=email,
        code=code,
        expires_at=datetime.now(timezone.utc)
        + timedelta(minutes=settings.VERIFICATION_CODE_EXPIRE_MINUTES),
    )
    db.add(verification)
    await send_verification_email(email, code)

    return user


async def verify_email_code(db: AsyncSession, email: str, code: str) -> User:
    """Verify the email with the provided code."""
    # Find valid verification
    result = await db.execute(
        select(EmailVerification)
        .where(EmailVerification.email == email)
        .where(EmailVerification.code == code)
        .where(~EmailVerification.is_used)
        .where(EmailVerification.expires_at > datetime.now(timezone.utc))
        .order_by(EmailVerification.created_at.desc())
    )
    verification = result.scalar_one_or_none()

    if not verification:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired verification code.",
        )

    # Mark verification as used
    verification.is_used = True

    # Activate user
    user_result = await db.execute(select(User).where(User.email == email))
    user = user_result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

    user.is_verified = True
    return user


async def authenticate_user(db: AsyncSession, email: str, password: str) -> User:
    """Authenticate a user by email and password."""
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )

    if not user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Please verify your email before logging in.",
        )

    return user
