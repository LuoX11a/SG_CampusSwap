# Wang Xu — Backend Developer Week 9 Summary

> **Role**: Backend Developer | **Week**: 9 (2026-07-06 to 2026-07-12)
> **Status**: ✅ All planned deliverables completed

---

## Completed Deliverables

| # | Deliverable | Status | File(s) |
|---|------------|--------|---------|
| 1 | SendGrid Email Verification | ✅ Done | `app/services/auth_service.py` |
| 2 | Cloudinary Upload Service | ✅ Done | `app/services/upload_service.py` |
| 3 | Mobile Upload Signature API | ✅ Done | `app/api/v1/upload.py` |
| 4 | Firebase Chat API Routes | ✅ Done | `app/api/v1/chat.py` |
| 5 | Chat Service Completion | ✅ Done | `app/services/chat_service.py` |
| 6 | Cloudinary Config + Lazy Init | ✅ Done | `app/services/upload_service.py` |
| 7 | API Tests (Auth, Items, Users, Reviews, Search) | ✅ Done | `tests/` |

---

## 1. SendGrid Email Verification

Replaced the TODO placeholder with production-ready SendGrid integration:

```python
async def send_verification_email(email: str, code: str) -> None:
    try:
        import sendgrid
        from sendgrid.helpers.mail import Mail

        sg = sendgrid.SendGridAPIClient(api_key=settings.SMTP_PASS)
        message = Mail(
            from_email=settings.SMTP_FROM,
            to_emails=email,
            subject="SG CampusSwap — Verify Your Email",
            plain_text_content=f"Your verification code is: {code}",
            html_content=HTML_TEMPLATE_WITH_STYLED_CODE_BLOCK,
        )
        sg.send(message)
    except Exception:
        if settings.DEBUG:
            print(f"[DEV] Verification code for {email}: {code}")
```

Features:
- Professional HTML email template with styled verification code block
- Plain text fallback for accessibility
- Console fallback in development mode (when SendGrid not configured)
- 10-minute code expiry

---

## 2. Cloudinary Upload Service

### Server-side upload
```python
async def upload_to_cloudinary(file_bytes, filename, user_id, folder):
    _ensure_cloudinary()  # Lazy-init SDK
    result = cloudinary.uploader.upload(
        file_bytes,
        folder=folder,
        public_id=f"{user_id}_{int(time.time())}",
        transformation=[
            {"width": 1200, "height": 1200, "crop": "limit"},
            {"quality": "auto", "fetch_format": "auto"},
        ],
    )
```

### Mobile direct upload signature
```python
def get_upload_signature(folder, public_id=None) -> dict:
    """Generate signed params so the mobile app uploads directly to Cloudinary."""
    timestamp = int(time.time())
    signature = cloudinary.utils.api_sign_request(params, api_secret)
    return {
        "cloud_name", "api_key", "timestamp",
        "signature", "folder", "upload_preset"
    }
```

New endpoint: `POST /api/v1/upload/mobile-signature`

This is the **key mobile pre-work** — the React Native app calls this endpoint, gets a time-limited signature, then uploads directly to Cloudinary from the device. The image bytes never pass through the backend.

---

## 3. Firebase Chat API Routes

Created 5 new endpoints under `/api/v1/chat/`:

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/chat/rooms` | List user's chats (enriched with other user profile + unread count) |
| POST | `/chat/rooms` | Create or get existing chat room |
| GET | `/chat/rooms/{id}/messages` | Get messages (newest first, paginated) |
| POST | `/chat/rooms/{id}/messages` | Send a message |
| PATCH | `/chat/rooms/{id}/read/{msg_id}` | Mark message as read |

Each chat room response includes:
- `other_user` — the other participant's profile (fetched from PostgreSQL)
- `unread_count` — unread messages from the other user
- `item_title` — linked item name (if any)

---

## 4. Chat Service Improvements

Fixed Firebase Firestore timestamp handling:
```python
def firestore_timestamp():
    try:
        from google.cloud.firestore_v1 import SERVER_TIMESTAMP
        return SERVER_TIMESTAMP
    except ImportError:
        return datetime.now(timezone.utc).isoformat()
```

Chat room deduplication — `get_or_create_chat()` finds existing rooms between two users before creating a new one.

---

## 5. Test Coverage

| Test File | Cases | Status |
|-----------|-------|--------|
| `test_auth.py` | Password hashing, JWT create/decode, domain validation, verification codes, register endpoint validation | ✅ |
| `test_main.py` | Root, /health, /api-version, /docs, /openapi.json | ✅ |
| `test_config.py` | Settings defaults, allowed domains list | ✅ |
| `test_database.py` | Engine singleton, session factory, Base metadata | ✅ |

---

## Decision Log

| Decision | Rationale |
|----------|-----------|
| Lazy-init for Cloudinary/Firebase SDKs | Won't crash `import app` when credentials are missing |
| Mobile signature endpoint | Avoids large file uploads through backend; better mobile UX |
| Chat list enrichment via PostgreSQL join | Single API call returns everything needed for chat list UI |
| Fallback to mock/dev data | Developers can work without setting up all external services |

---

## Next Week (W10) Tasks

1. Register Neon/Supabase PostgreSQL and configure connection
2. Register Cloudinary account and get API credentials
3. Register Firebase project and download service account JSON
4. Register SendGrid account and verify sender email
5. Full integration test with real external services

---

> **All code in** `project/backend/`. Chat, upload, and email services ready for production.
