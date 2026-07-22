# SG CampusSwap — Week 9 Technical Delivery Summary

> **Date**: 2026-07-13 | **All 6 members**

---

## What Was Delivered

The `project/` directory now contains a **fully runnable full-stack web application**.

### Quick Start
```bash
# 1. Backend
cd project/backend
cp .env.example .env          # Configure credentials
docker-compose up -d           # PostgreSQL + FastAPI on :8000

# 2. Frontend
cd project/web
cp .env.local.example .env.local  # Configure Firebase keys
npm install && npm run dev         # Next.js on :3000
```

### Project Structure
```
project/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app + health + version endpoints
│   │   ├── config.py            # Settings (env vars → pydantic)
│   │   ├── database.py          # Async SQLAlchemy + session
│   │   ├── models/              # User, Item, Review (+ Image, Transaction, EmailVerification, RefreshToken)
│   │   ├── schemas/             # Pydantic request/response schemas
│   │   ├── api/v1/              # 7 route modules (29 endpoints)
│   │   │   ├── auth.py          # Register, verify, login, refresh, logout, me
│   │   │   ├── items.py         # CRUD + status change
│   │   │   ├── users.py         # Profile, update, listings
│   │   │   ├── upload.py        # Server upload + mobile signature
│   │   │   ├── reviews.py       # Create, list, rating summary
│   │   │   ├── search.py        # Full-text search + 8 filters
│   │   │   └── chat.py          # NEW: Chat rooms + messages (REST)
│   │   ├── services/            # Business logic
│   │   │   ├── auth_service.py  # JWT, password hashing, SendGrid email
│   │   │   ├── item_service.py  # Item CRUD helpers
│   │   │   ├── upload_service.py # Cloudinary + mobile signature
│   │   │   └── chat_service.py  # Firebase Firestore or mock
│   │   └── utils/               # Helpers
│   │       ├── email_whitelist.py
│   │       ├── security.py
│   │       └── mobile.py        # Deep links, API versioning
│   ├── migrations/              # Alembic (async)
│   ├── tests/                   # 4 test files
│   ├── alembic.ini
│   ├── Dockerfile
│   ├── docker-compose.yml       # API + PostgreSQL
│   ├── requirements.txt
│   └── .env.example
│
├── web/
│   ├── src/
│   │   ├── app/                 # 17 pages (Next.js App Router)
│   │   ├── components/          # 8 components
│   │   ├── stores/              # 4 Zustand stores
│   │   └── lib/                 # 5 utility modules
│   ├── public/
│   │   ├── manifest.json        # PWA manifest
│   │   ├── sw.js                # Service Worker
│   │   └── icons/               # App icons
│   ├── next.config.js           # API proxy + PWA headers
│   ├── tailwind.config.ts
│   └── package.json
│
└── docker-compose.yml
```

---

## Member Contributions — Week 9

| Member | Role | Key Deliverables |
|--------|------|-----------------|
| **Huang Hongrui** | PM | Progress report, risk register update, sprint backlog, meeting agenda |
| **Wang Bowei** | BE Lead | Alembic, utils module, API router (7 modules), health/version endpoints, CORS, tests |
| **Wang Xu** | BE Dev | SendGrid email, Cloudinary upload + mobile signature, Firebase chat routes, chat service |
| **Renxian Tang** | FE Lead | PWA (manifest + service worker), next.config, offline page, mobile meta tags, API proxy |
| **Jiahai Xiong** | FE Dev | Firebase client SDK, Cloudinary lib, chat store (real-time), ImageUpload component |
| **Junliang Li** | QA | Usability test plan, test execution report, W10 testing schedule |

---

## API Endpoint Inventory (29 total)

| Module | # | Endpoints |
|--------|---|-----------|
| Auth | 6 | register, verify, login, refresh, logout, me |
| Items | 6 | list, create, get, update, delete, status |
| Users | 4 | profile, update, my-listings, user-listings |
| Upload | 4 | image, images, delete, **mobile-signature** |
| Reviews | 4 | list, create, my-reviews, rating-summary |
| Search | 1 | search (8 filters: q, category, condition, campus, min_price, max_price, sort, page) |
| Chat | 5 | rooms, create-room, messages, send-message, **mark-read** |
| **Health** | 2 | / (health), /health, /api-version |
| **Total** | **29** | |

---

## Mobile App Pre-Work Checklist

- [x] `GET /api-version` — compatibility check endpoint
- [x] `GET /health` — connectivity test
- [x] `POST /upload/mobile-signature` — direct Cloudinary upload
- [x] `X-API-Version` header support
- [x] `X-Mobile-App` header → mobile-optimised pagination
- [x] `sgcampusswap://` deep link scheme
- [x] CORS: capacitor://localhost, ionic://localhost
- [x] PWA manifest.json + service worker
- [x] Apple/Android mobile meta tags

---

## What W10 Needs (NOT in Week 9)

### External Service Registration
- Neon/Supabase PostgreSQL account
- Cloudinary account + API credentials
- Firebase project + Firestore
- SendGrid account + verified sender

### Deployment
- AWS EC2 t2.micro (ap-southeast-1)
- Nginx + Let's Encrypt
- Vercel frontend deployment
- GitHub Actions deploy pipeline

### Mobile App
- Capacitor wrapper (`npx cap init`)
- Native APK/IPA build
- Push notifications (FCM)
- Camera/photo library access

### Final
- Usability testing (10-15 participants)
- Final report
- Presentation slides + demo video

---

> **Week 9 status**: Web project is complete and runnable. `docker-compose up` + `npm run dev` starts the full stack. Ready for W10 deployment.
