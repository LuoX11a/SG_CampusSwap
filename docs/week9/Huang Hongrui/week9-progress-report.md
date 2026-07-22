# SG CampusSwap — Week 9 Progress Report

> **Period**: 2026-07-06 to 2026-07-12 (Week 9)
> **Author**: Huang Hongrui (PM)
> **Status**: 🟢 ON TRACK — Web project fully runnable; mobile pre-work complete

---

## Executive Summary

Week 9 was the final integration week. The web project (`project/`) is now **fully runnable** — `docker-compose up` starts the FastAPI backend + PostgreSQL, and `npm run dev` starts the Next.js frontend. All key services (SendGrid email, Cloudinary upload, Firebase chat) are implemented with graceful fallbacks for development. PWA setup allows the web app to be installed as a mobile app. Mobile app API pre-work (CORS, deep links, direct upload signatures) is complete.

**Key Achievement**: `project/` is a complete, runnable full-stack application. 7 API route modules, 16 web pages, PWA-ready.

---

## Completed Deliverables

### Backend (Bowei + Wang Xu) — 10 tasks ✅

| Deliverable | Details |
|-------------|---------|
| Alembic Migrations | `alembic.ini`, `migrations/env.py`, async environment |
| Utils Module | email_whitelist.py, security.py, mobile.py |
| API Router (7 modules) | Auth, Items, Users, Upload, Reviews, Search, **Chat (NEW)** |
| Health + Version Endpoints | `GET /health`, `GET /api-version` (mobile compatibility check) |
| CORS Config | Web + Capacitor + Ionic origins |
| SendGrid Email | HTML + plain text verification email, dev console fallback |
| Cloudinary Upload | Server-side + mobile signature endpoint |
| Firebase Chat Routes | 5 REST endpoints for chat rooms and messages |
| Environment Config | Comprehensive `.env.example` covering all 6 services |
| Test Suite | 4 test files in `project/backend/tests/` |

### Frontend (Renxian + Jiahai) — 8 tasks ✅

| Deliverable | Details |
|-------------|---------|
| PWA Manifest | Installable on iOS/Android home screen |
| Service Worker | Cache-first static, network-first API, offline fallback, push placeholder |
| Firebase Client SDK | Lazy-init with graceful fallback |
| Cloudinary Client Lib | Server-side upload + mobile signature flow |
| Chat Store | Real-time Firebase listener OR REST polling fallback |
| ImageUpload Component | Drag & drop, preview, progress, multi-file (max 5) |
| Offline Page | Styled fallback when network unavailable |
| Mobile Meta Tags | Apple + Android app-capable, viewport config |

### PM & QA (Hongrui + Junliang) — 5 tasks ✅

| Deliverable | Details |
|-------------|---------|
| W9 Progress Report | This document |
| Sprint Backlog Update | Sprint 4 closing, Sprint 5 prep |
| Risk Register Update | Updated risk status |
| Usability Test Plan | 10-15 participants, 5 core flows, W10 execution |
| Test Execution Report | Coverage and results summary |

---

## Project State: Fully Runnable

### Start the project:
```bash
# Backend
cd project/backend
docker-compose up -d           # PostgreSQL + FastAPI

# Frontend
cd project/web
npm install && npm run dev     # Next.js on http://localhost:3000
```

### What works:
- ✅ User registration with university email domain whitelist (29 domains)
- ✅ Email verification via SendGrid (console fallback in dev)
- ✅ JWT auth with login/refresh/logout
- ✅ Item CRUD with search + filters
- ✅ Image upload via Cloudinary (server-side or mobile direct)
- ✅ Firebase real-time chat (REST polling fallback in dev)
- ✅ User reviews with rating summary
- ✅ PWA installable on mobile home screen
- ✅ Offline fallback page

### What needs external accounts (W10):
- 🔲 Neon/Supabase PostgreSQL (for production DB)
- 🔲 SendGrid API key (for production email)
- 🔲 Cloudinary account (for production image upload)
- 🔲 Firebase project (for production real-time chat)

---

## Metrics

| Metric | W8 | W9 |
|--------|----|----|
| API route modules | 6 | **7** (Chat added) |
| API endpoints | 22 | **29** |
| Backend test files | 3 | **4** (project/backend) |
| Web pages | 16 | **17** (Offline added) |
| Frontend components | 6 | **8** (ImageUpload, PwaRegister) |
| Frontend lib modules | 3 | **5** (firebase.ts, cloudinary.ts) |
| PWA readiness | — | ✅ Installable |

---

## Mobile App Pre-Work (Complete)

The following are ready for the React Native / Capacitor mobile app:

| Pre-work | Location | Purpose |
|----------|----------|---------|
| `GET /health` | `app/main.py` | Mobile connectivity test |
| `GET /api-version` | `app/main.py` | Forced-update check |
| `POST /upload/mobile-signature` | `app/api/v1/upload.py` | Direct-to-Cloudinary upload from device |
| `X-API-Version` header | `app/utils/mobile.py` | API version negotiation |
| `X-Mobile-App` header | `app/utils/mobile.py` | Mobile-optimised pagination |
| `sgcampusswap://` deep links | `app/utils/mobile.py` | Push notification → app screen |
| CORS origins | `app/config.py` | capacitor://, ionic:// |
| `manifest.json` | `public/` | PWA → Capacitor packaging |

---

## Risks Update

| Risk | W8 | W9 | Trend | Mitigation |
|------|-----|-----|-------|------------|
| Timeline delay | MEDIUM | LOW | ↓ | All features done; only deployment + external accounts remain |
| External service setup | — | MEDIUM | 🆕 | 4 services need accounts; W10 task |
| Mobile app timing | HIGH | MEDIUM | ↓ | PWA covers mobile temporarily; Capacitor wrapper W10 |
| Firebase chat in dev | MEDIUM | LOW | ↓ | REST polling fallback works without Firebase config |

---

## Next Week (W10) — Sprint 5: Final Delivery

1. Register external services (Neon, Cloudinary, Firebase, SendGrid)
2. Deploy backend to AWS EC2 + Nginx + HTTPS
3. Deploy frontend to Vercel
4. Capacitor wrapper for native APK/IPA
5. Usability testing with 10-15 students
6. Final report + presentation

---

> **Conclusion**: Week 9 delivered a fully runnable web application with all features integrated. Mobile app pre-work is complete. W10 focuses on production deployment and external service registration.

