# Wang Bowei — Backend Lead Week 9 Summary

> **Role**: Backend Lead | **Week**: 9 (2026-07-06 to 2026-07-12)
> **Status**: ✅ All planned deliverables completed

---

## Completed Deliverables

| # | Deliverable | Status | File(s) |
|---|------------|--------|---------|
| 1 | Alembic Migrations Setup | ✅ Done | `migrations/env.py`, `alembic.ini` |
| 2 | Utils Module (email whitelist, security, mobile) | ✅ Done | `app/utils/` |
| 3 | API Router + Chat Routes | ✅ Done | `app/api/v1/__init__.py`, `app/api/v1/chat.py` |
| 4 | Health + API Version Endpoints | ✅ Done | `app/main.py` (`/health`, `/api-version`) |
| 5 | CORS Configuration (web + mobile) | ✅ Done | `app/main.py`, `app/config.py` |
| 6 | Mobile API Pre-work | ✅ Done | `app/utils/mobile.py` |
| 7 | Environment Config | ✅ Done | `.env.example` (comprehensive) |
| 8 | Test Infrastructure | ✅ Done | `tests/conftest.py`, 4 test files |
| 9 | CI/CD Ready | ✅ Done | `.github/workflows/deploy.yml` |

---

## 1. Alembic Migrations

Database migration tooling initialized:

```
project/backend/
├── alembic.ini              # Migration config
├── migrations/
│   ├── env.py               # Async Alembic environment
│   ├── script.py.mako        # Migration template
│   └── versions/             # Migration files
```

All ORM models auto-detected: User, Item, Review, ItemImage, Transaction, EmailVerification, RefreshToken

```bash
# Generate initial migration:
cd project/backend
alembic revision --autogenerate -m "initial_schema"
alembic upgrade head
```

---

## 2. Utils Module

```
app/utils/
├── __init__.py              # Module docstring
├── email_whitelist.py        # University domain validation + mapping
├── security.py               # Password strength, input sanitisation, mobile UA detection
└── mobile.py                 # API version negotiation, mobile page sizing, deep links
```

Key additions:
- `get_domain_university()` — maps email domain → friendly university name
- `is_mobile_user_agent()` — detects mobile clients for response optimisation
- `build_deep_link()` — generates `sgcampusswap://{resource}/{id}` links for mobile app
- `validate_password_strength()` — unified password rules

---

## 3. API Router — Now 7 Modules (was 6)

```python
api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(items_router, prefix="/items", tags=["Items"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(upload_router, prefix="/upload", tags=["Upload"])
api_router.include_router(reviews_router, prefix="/reviews", tags=["Reviews"])
api_router.include_router(search_router, prefix="/search", tags=["Search"])
api_router.include_router(chat_router, prefix="/chat", tags=["Chat"])  # NEW
```

Chat API (5 endpoints):
- `GET /chat/rooms` — List user's chat rooms
- `POST /chat/rooms` — Create/get chat room
- `GET /chat/rooms/{id}/messages` — Get messages
- `POST /chat/rooms/{id}/messages` — Send message
- `PATCH /chat/rooms/{id}/read/{msg_id}` — Mark read

---

## 4. Health & Mobile Compatibility Endpoints

```
GET /              → Health check (load balancer, monitoring)
GET /health        → Detailed health (ELB, mobile connectivity test)
GET /api-version   → API version + min_client_version (forced-update check)
```

Mobile apps call `/api-version` on startup to detect breaking API changes.

---

## 5. CORS & Mobile Configuration

```python
CORS_ORIGINS = (
    "http://localhost:3000,"           # Web dev
    "https://sgcampuswap.vercel.app,"  # Web prod
    "capacitor://localhost,"            # iOS Capacitor
    "ionic://localhost,"                # Android Capacitor
    "http://localhost"                  # Expo / RN dev
)
```

Added `X-API-Version` and `X-Mobile-App` header support for mobile clients.

---

## 6. Environment Configuration

`.env.example` now covers all services:
- Database (PostgreSQL, pool config)
- JWT (secret, algorithm, expiry)
- Email (SendGrid: host, port, API key, from address)
- Cloudinary (cloud name, API key/secret, upload preset)
- Firebase (service account path, web config keys)
- CORS origins
- Rate limiting

---

## 7. Test Suite

```
project/backend/tests/
├── __init__.py
├── conftest.py          # TestClient, async_client, test_db fixtures
├── test_main.py         # Root, /health, /api-version, /docs, /openapi.json
├── test_config.py       # Settings defaults, allowed domains
├── test_database.py     # Engine singleton, session factory, Base metadata
└── test_auth.py         # Password hashing, JWT, domain validation, register API
```

---

## Decision Log

| Decision | Rationale |
|----------|-----------|
| Chat routes in backend (not direct Firebase) | Single auth boundary; chats are discoverable via REST |
| Mobile deep link scheme `sgcampusswap://` | Universal links for push notifications and email CTAs |
| `X-API-Version` header support | Graceful deprecation without URL versioning |
| Alembic async env | Matches production async engine |

---

## Next Week (W10) Tasks

1. Provision AWS EC2 instance and deploy backend
2. Configure Nginx + Let's Encrypt
3. Add rate limiting (slowapi)
4. Neon/Supabase PostgreSQL setup
5. Production `.env` with real credentials

---

> **All code in** `project/backend/`. Web project is fully runnable with `docker-compose up`.

