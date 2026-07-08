# SG CampusSwap — Sprint Backlog W8 Update

> **Updated**: 2026-07-07 (Week 8) | **Author**: Huang Hongrui (PM)
> **Strategic Change**: 🔄 Web-First Architecture — build web app first, then derive mobile from web

---

## Strategy Shift: Web-First

**Decision Date**: W8 Mon (2026-06-29)
**Rationale**: 
1. Team more familiar with web technologies (React + TypeScript)
2. Web app can serve as admin/moderator panel later
3. Mobile app (Expo React Native) will share API client, types, and state management
4. Faster iteration cycle — no device/build overhead
5. Desktop-first design provides richer UX for browsing listings

**Impact**: Frontend tasks shift from Expo/React Native → Next.js 14 (App Router)

---

## Sprint 3 (W6–W7): Foundation ✅ CLOSED

| ID | Task | Owner | Status |
|----|------|-------|--------|
| S3-B01 | Create `develop` branch | Bowei | ✅ Done (W8 carry-over) |
| S3-B02 | FastAPI project scaffold | Bowei | ✅ Done |
| S3-B03 | PostgreSQL schema design | Bowei | ✅ Done |
| S3-B04 | Auth service (JWT + bcrypt) | Bowei | ✅ Done |
| S3-F01 | Frontend architecture design | Renxian | ✅ Done |
| S3-F02 | TypeScript type definitions (11 interfaces) | Renxian | ✅ Done |
| S3-F03 | Navigation architecture | Renxian | ✅ Done |
| S3-Q01 | Figma screen specifications (15 screens) | Junliang | ✅ Done |
| S3-Q02 | Test plan (80 test cases) | Junliang | ✅ Done |
| S3-Q03 | GitHub labels & templates | Junliang | ✅ Done |
| S3-P01 | Risk register | Hongrui | ✅ Done |
| S3-P02 | Sprint backlog | Hongrui | ✅ Done |
| S3-P03 | Meeting minutes W1–W5 | Hongrui | ✅ Done |
| S3-P04 | Final report framework | Hongrui | ✅ Done |
| S3-P05 | Literature reviews (all 6) | All | ✅ Done |

---

## Sprint 4 (W8–W9): Core Feature Development 🔴 IN PROGRESS

### BACKEND (Bowei + Wang Xu)

| ID | Task | Owner | Status | Deadline |
|----|------|-------|--------|----------|
| S4-B01 | Auth API routes (register/verify/login/refresh) | Bowei | ✅ Done | W8 Mon |
| S4-B02 | Database migrations (Alembic) | Bowei | ✅ Done | W8 Tue |
| S4-B03 | Item CRUD API (`/api/v1/items`) | Wang Xu | ✅ Done | W8 Wed |
| S4-B04 | Search & filter API (`/api/v1/search`) | Wang Xu | ✅ Done | W8 Wed |
| S4-B05 | Image upload API (Cloudinary) | Wang Xu | ✅ Done | W8 Thu |
| S4-B06 | User profile API (`/api/v1/users`) | Wang Xu | ✅ Done | W8 Thu |
| S4-B07 | Reviews API (`/api/v1/reviews`) | Wang Xu | ✅ Done | W8 Fri |
| S4-B08 | Firebase chat service | Wang Xu | ✅ Done | W8 Fri |
| S4-B09 | API documentation (Swagger UI) | Bowei | ✅ Done | W8 Fri |
| S4-B10 | Docker + docker-compose | Bowei | ✅ Done | W8 Fri |

### FRONTEND — WEB (Renxian + Jiahai)

| ID | Task | Owner | Status | Deadline |
|----|------|-------|--------|----------|
| S4-F01 | Next.js 14 project scaffold | Renxian | ✅ Done | W8 Mon |
| S4-F02 | Dark Sidebar navigation component | Renxian | ✅ Done | W8 Tue |
| S4-F03 | API client (axios + JWT interceptor) | Renxian | ✅ Done | W8 Tue |
| S4-F04 | Zustand stores (auth/items/filter) | Renxian | ✅ Done | W8 Tue |
| S4-F05 | ItemCard grid component | Renxian | ✅ Done | W8 Wed |
| S4-F06 | Home page (grid + search + category chips) | Renxian | ✅ Done | W8 Wed |
| S4-F07 | Auth pages (Login/Register/VerifyEmail) | Renxian | ✅ Done | W8 Wed |
| S4-F08 | ItemDetail page | Renxian | ✅ Done | W8 Thu |
| S4-F09 | CreateListing page (image upload) | Renxian | ✅ Done | W8 Thu |
| S4-F10 | SearchResults + FilterModal | Jiahai | ✅ Done | W8 Thu |
| S4-F11 | ChatList page | Jiahai | ✅ Done | W8 Fri |
| S4-F12 | ChatRoom page (Firebase real-time) | Jiahai | ✅ Done | W8 Fri |
| S4-F13 | Profile page + EditProfile | Jiahai | ✅ Done | W8 Fri |
| S4-F14 | Settings page | Jiahai | ✅ Done | W8 Fri |
| S4-F15 | Reviews page + Rating summary | Jiahai | ✅ Done | W8 Fri |
| S4-F16 | MyListings page | Jiahai | ✅ Done | W8 Fri |

### PM & QA

| ID | Task | Owner | Status | Deadline |
|----|------|-------|--------|----------|
| S4-Q01 | Web design specifications | Junliang | ✅ Done | W8 Tue |
| S4-Q02 | Updated test cases (web adaptation) | Junliang | ✅ Done | W8 Fri |
| S4-Q03 | W8 meeting agenda | Hongrui | ✅ Done | W8 Mon |
| S4-Q04 | W8 progress report | Hongrui | ✅ Done | W8 Fri |
| S4-Q05 | Risk register update | Hongrui | ✅ Done | W8 Fri |

---

## Sprint 5 (W10): Testing & Final Delivery ⚪ PLANNED

| ID | Task | Owner |
|----|------|-------|
| S5-T01 | Backend unit tests (pytest) | Bowei + Wang Xu |
| S5-T02 | Frontend component tests (Jest) | Renxian + Jiahai |
| S5-T03 | Integration tests (API + DB) | Bowei + Wang Xu |
| S5-T04 | E2E tests (Cypress) | Junliang |
| S5-T05 | Bug fixes | All |
| S5-D01 | Deploy backend to AWS EC2 | Bowei |
| S5-D02 | Deploy frontend to Vercel | Renxian |
| S5-D03 | Mobile app (Expo) from web codebase | Renxian + Jiahai |
| S5-D04 | Final report | All |
| S5-D05 | Final presentation | All |

---

## Burn-Down Summary (Updated)

| Sprint | Weeks | Tasks Total | Done | In Progress | TODO |
|--------|-------|-------------|------|-------------|------|
| Sprint 1 | W1–W2 | 5 | 5 | 0 | 0 |
| Sprint 2 | W3–W5 | 9 | 9 | 0 | 0 |
| Sprint 3 | W6–W7 | 30 | 15 | 0 | 15 |
| **Sprint 4** | **W8–W9** | **27** | **27** | **0** | **0** |
| Sprint 5 | W10 | 9 | 0 | 0 | 9 |

> 📊 **Velocity**: Sprint 4 delivered 27 tasks in 2 weeks (excellent velocity after strategy pivot).
> 🎯 **On track** for W10 final delivery.

---

## Key Risks (Updated)

| Risk | Severity | Mitigation |
|------|----------|------------|
| Mobile app timeline compressed | HIGH | Share API client + types between web & mobile |
| Firebase chat not tested at scale | MEDIUM | Limit to 100 concurrent users in MVP |
| Cloudinary quota on free tier | LOW | Image compression + 5-image limit per listing |

---

> **Next**: Sprint 5 starts W10 Mon — Testing & Final Delivery
