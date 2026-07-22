# SG CampusSwap

<div align="center">

**A campus-centric C2C marketplace for Singapore university students**

[![Next.js](https://img.shields.io/badge/Frontend-Next.js_14-000000?logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/Database-Neon_PostgreSQL-4169E1?logo=postgresql)](https://neon.tech/)
[![Vercel](https://img.shields.io/badge/Hosting-Frontend_Vercel-000000?logo=vercel)](https://vercel.com/)
[![Render](https://img.shields.io/badge/Hosting-Backend_Render-46E3B7?logo=render)](https://render.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**[🔗 Live Demo](https://sg-campusswap.vercel.app)** · **[📖 API Docs](https://sg-campusswap-api.onrender.com/docs)**

</div>

---

## About

SG CampusSwap is a **mobile-first web application** that provides a trusted, convenient, and campus-centric platform for Singapore university students to trade second-hand goods — textbooks, electronics, furniture, and daily necessities.

### Why This Exists

General-purpose marketplaces like Carousell and Facebook Marketplace are not designed for student-specific needs. SG CampusSwap addresses this gap with:

- **Verified student community** — Registration requires a university email (37 Singapore university domains supported)
- **Campus-based discovery** — Filter items by campus location, find suggested meetup points
- **Course-code textbook search** — Search for textbooks by course code (e.g., "CS1010", "MA1101R")
- **In-app messaging** — Chat between buyers and sellers
- **Trust via ratings** — User profiles with transaction reviews

---

## Live Deployment

| Component | URL | Status |
|-----------|-----|--------|
| **Frontend** | [sg-campusswap.vercel.app](https://sg-campusswap.vercel.app) | 🟢 Live |
| **Backend API** | [sg-campusswap-api.onrender.com](https://sg-campusswap-api.onrender.com) | 🟢 Live |
| **API Docs** | [Swagger UI](https://sg-campusswap-api.onrender.com/docs) | 🟢 Live |
| **Database** | Neon PostgreSQL (ap-southeast-1) | 🟢 Live |

### Demo Account
| Email | Password |
|-------|----------|
| `demo@e.ntu.edu.sg` | `Demo123!` |

> **Note**: Render free tier sleeps after 15 minutes of inactivity. First request may take 30-50 seconds.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Next.js 14 (App Router) + TypeScript + Tailwind CSS |
| **State Management** | Zustand |
| **Backend** | FastAPI (Python 3.11) + Uvicorn |
| **Database** | Neon PostgreSQL (serverless, 0.5GB free) |
| **ORM** | SQLAlchemy 2.0 + Alembic |
| **Auth** | JWT + university email domain whitelist |
| **Email** | SendGrid (optional; DEBUG mode bypasses verification) |
| **Image Upload** | Cloudinary (with dev fallback to placeholder images) |
| **Chat** | Firebase Firestore (optional fallback available) |
| **Frontend Hosting** | Vercel (free, auto HTTPS, global CDN) |
| **Backend Hosting** | Render (free, Docker, Singapore region) |
| **CI/CD** | GitHub Actions + Vercel/Render auto-deploy |

---

## Project Structure

```
sg-campusswap/
├── backend/                    # FastAPI server
│   ├── app/
│   │   ├── main.py            # App entry + lifespan + health
│   │   ├── config.py          # Settings & env vars (pydantic-settings)
│   │   ├── database.py        # SQLAlchemy async engine + session
│   │   ├── models/            # ORM models (User, Item, Review, Transaction, etc.)
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── api/v1/            # 7 routers: auth, items, users, upload, reviews, search, chat
│   │   └── services/          # auth, chat, item, upload services
│   ├── migrations/            # Alembic migrations (8 tables)
│   ├── tests/                 # Pytest test suite
│   ├── Dockerfile             # Docker build for Render
│   ├── runtime.txt            # Python version (3.11)
│   └── requirements.txt       # Python dependencies
│
├── project/web/               # Next.js frontend
│   ├── src/app/               # App Router pages (15 pages)
│   ├── src/components/        # Reusable UI (Sidebar, ItemCard, MobileBottomNav, etc.)
│   ├── src/stores/            # Zustand stores (auth, item, chat, filter)
│   ├── src/lib/               # API client, types, formatters
│   ├── public/                # PWA manifest, icons, service worker
│   ├── next.config.js
│   ├── tailwind.config.ts
│   └── package.json
│
├── docs/                      # Team documentation (Week 7-10)
├── render.yaml                # Render Blueprint config
├── docker-compose.yml
└── .github/workflows/         # CI/CD pipeline
```

---

## Features

### ✅ Implemented (MVP)
- [x] University email registration (37 Singapore university domains)
- [x] Item listing with image upload
- [x] Search by keyword, course code, category with relevance sorting
- [x] Filter by campus, price range, condition, category
- [x] User profile with transaction reviews & ratings
- [x] Campus-based meetup point suggestions
- [x] Mobile-responsive with PWA support
- [x] Infinite scroll item browsing
- [x] JWT authentication with auto-refresh
- [x] Responsive sidebar (desktop) + bottom tab navigation (mobile)

### 🚧 Partially Implemented
- [ ] Email verification (DEBUG mode auto-verifies; SMTP not configured)
- [ ] Real-time chat (REST API ready; Firebase not configured — shows empty state)
- [ ] Image upload (Cloudinary fallback to placeholder images)

### 🔮 Future Versions
- [ ] Push notifications
- [ ] Dark mode
- [ ] Wishlist / saved items
- [ ] Price negotiation system
- [ ] Chat read receipts & typing indicators

---

## Getting Started

### Prerequisites

- **Python 3.11+** with `pip`
- **Node.js 18+** with `npm`
- **PostgreSQL** (or a free [Neon](https://neon.tech) database)

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables (or create .env)
cp .env.example .env
# Edit .env with your DATABASE_URL, JWT_SECRET, etc.

# Run migrations
alembic upgrade head

# Start dev server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API docs at `http://localhost:8000/docs`

### Frontend Setup

```bash
cd project/web

# Install dependencies
npm install

# Set API URL
echo "NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1" > .env.local

# Start dev server
npm run dev
```

Open `http://localhost:3000`

---

## API Overview

| Router | Base Path | Auth | Endpoints |
|--------|-----------|------|-----------|
| Auth | `/api/v1/auth` | Mixed | register, verify, login, refresh, logout, me |
| Items | `/api/v1/items` | Mixed | list, create, detail, update, delete, status |
| Users | `/api/v1/users` | Mixed | profile, update, my-listings |
| Upload | `/api/v1/upload` | Yes | single/multi image upload, delete |
| Reviews | `/api/v1/reviews` | Mixed | user reviews, create, rating summary |
| Search | `/api/v1/search` | No | full-text search with filters |
| Chat | `/api/v1/chat` | Yes | rooms, messages (Firebase backend) |

Full API documentation: [Swagger UI](https://sg-campusswap-api.onrender.com/docs)

---

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Neon PostgreSQL async connection | `postgresql+asyncpg://...` |
| `DATABASE_URL_SYNC` | PostgreSQL sync connection (Alembic) | `postgresql://...` |
| `JWT_SECRET` | JWT signing key (≥32 chars) | `change-me-...` |
| `CORS_ORIGINS` | Comma-separated allowed origins | `*` |
| `ENVIRONMENT` | `development` or `production` | `development` |
| `DEBUG` | Auto-verify users, return codes | `false` |
| `ALLOWED_EMAIL_DOMAINS` | University email whitelist | (37 domains) |
| `SMTP_HOST/PORT/USER/PASS` | SendGrid email config | (empty) |
| `CLOUDINARY_*` | Cloudinary image upload | (empty) |
| `GOOGLE_APPLICATION_CREDENTIALS` | Firebase service account | (empty) |

---

## Team

| Name | Role |
|------|------|
| Huang Hongrui | Project Manager |
| Renxian Tang | Frontend Lead |
| Wang Bowei | Backend Lead |
| Jiahai Xiong | Frontend Developer |
| Wang Xu | Backend Developer |
| Junliang Li | UI/UX Designer & QA |

---

## Development

- **Methodology**: Agile / Scrum (2-week sprints)
- **Branching**: `master` → `develop` → `feature/*`, `fix/*`
- **Commits**: [Conventional Commits](https://www.conventionalcommits.org/)
- **Deployment**: Auto-deploy on push to `master` (Vercel + Render)

---

## License

This project is developed as part of the CP3102 coursework at James Cook University Singapore (2026 TR2).
