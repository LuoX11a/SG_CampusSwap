# Wang Bowei — Backend Lead Week 8 Summary

> **Role**: Backend Lead | **Week**: 8 (2026-06-29 to 2026-07-05)
> **Status**: ✅ All planned deliverables completed

---

## Completed Deliverables

| # | Deliverable | Status | File(s) |
|---|------------|--------|---------|
| 1 | Auth API routes (register, verify, login, refresh) | ✅ Done | `backend/app/api/v1/auth.py` |
| 2 | Router registry (`/api/v1/`) | ✅ Done | `backend/app/api/v1/__init__.py` |
| 3 | Alembic database migrations | ✅ Done | `backend/migrations/` |
| 4 | Docker configuration | ✅ Done | `Dockerfile`, `docker-compose.yml` |
| 5 | API documentation (Swagger UI) | ✅ Done | Auto at `/docs` |
| 6 | CORS + middleware configuration | ✅ Done | `backend/app/main.py` update |
| 7 | Environment configuration (`.env.example`) | ✅ Done | `backend/.env.example` |

---

## 1. Auth API Implementation

### Endpoints

| Method | Path | Description | Auth |
|--------|------|-------------|------|
| POST | `/api/v1/auth/register` | Register with university email | No |
| POST | `/api/v1/auth/verify` | Verify email with 6-digit code | No |
| POST | `/api/v1/auth/login` | Login → access + refresh tokens | No |
| POST | `/api/v1/auth/refresh` | Refresh expired access token | Refresh token |
| POST | `/api/v1/auth/logout` | Invalidate refresh token | Access token |
| GET | `/api/v1/auth/me` | Get current user profile | Access token |

### Register Flow
1. Validate email domain against whitelist (22 domains across NUS, NTU, SMU, SUTD, SUSS, SIT, SIM, NP, SP, TP, NYP, RP, LASALLE, NAFA, JCU)
2. Check username + email uniqueness
3. Hash password with bcrypt (12 rounds)
4. Create user (is_verified=False)
5. Generate 6-digit verification code
6. Send verification email (SendGrid)
7. Return: `{ message: "Verification code sent to {email}" }`

### Login Flow
1. Find user by email
2. Verify password with bcrypt
3. Check `is_verified=True`
4. Issue access token (30 min, JWT with user_id + email claims)
5. Issue refresh token (7 days, stored in DB)
6. Return: `{ access_token, refresh_token, token_type: "bearer", expires_in: 1800 }`

### Security
- Passwords: bcrypt with 12 salt rounds
- JWTs: HS256 with configurable SECRET_KEY
- Token expiry: access=30min, refresh=7days
- Domain whitelist: server-side enforced (not just client hint)
- Rate limiting: TODO in W9 (slowapi)

---

## 2. Database Migrations (Alembic)

```
migrations/
├── alembic.ini
├── env.py
├── script.py.mako
└── versions/
    └── 001_initial_schema.py
```

### Migration: 001_initial_schema

Creates:
- `users` table (8 columns, UUID PK, email unique, username unique)
- `items` table (14 columns, FK → users.seller_id)
- `reviews` table (7 columns, FK → users.reviewer_id, users.reviewee_id)
- `item_images` table (4 columns, FK → items.item_id)
- `transactions` table (7 columns, FK → items, users.buyer, users.seller)
- `email_verifications` table (6 columns)
- `refresh_tokens` table (5 columns, FK → users)
- 5 Enum types: `item_category`, `item_condition`, `item_status`, `transaction_status`, `review_rating`
- Indexes: items(seller_id), items(category), items(status), items(created_at DESC), reviews(reviewee_id), email_verifications(email, code)

---

## 3. Docker Configuration

### Dockerfile
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### docker-compose.yml
```yaml
services:
  api:
    build: .
    ports: ["8000:8000"]
    env_file: .env
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: sg_campus_swap
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    ports: ["5432:5432"]
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
volumes:
  pgdata:
```

---

## 4. API Router Registry

```python
# backend/app/api/v1/__init__.py
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
```

---

## 5. CORS Configuration (Updated for Web Frontend)

```python
# In main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",     # Next.js dev
        "https://sgcampuswap.vercel.app",  # Production frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 6. Decision Log

| Decision | Rationale |
|----------|-----------|
| Access token in localStorage (not httpOnly cookie) | Simplifies SPA auth; acceptable for MVP |
| bcrypt over argon2 | bcrypt more widely supported, sufficient for MVP |
| UUID primary keys | Avoids sequential ID guessing |
| Refresh tokens in DB | Enables token revocation |
| No rate limiting in W8 | Defer to W9; slowapi is simple to add |
| PostgreSQL enum types | Better data integrity than VARCHAR |

---

## Next Week (W9) Tasks

1. Deploy to AWS EC2 (t2.micro, ap-southeast-1)
2. Set up Neon PostgreSQL production instance
3. Configure Nginx + Let's Encrypt
4. Add rate limiting (slowapi)
5. Run full test suite (pytest)
6. API performance optimization (query N+1 fixes)

---

> **All code ready** in `week8/Wang Bowei/backend/` and `week8/Wang Xu/backend/`.
