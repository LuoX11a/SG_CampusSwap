# SG CampusSwap — Sprint Backlog W9 Update

> **Updated**: 2026-07-12 (Week 9) | **Author**: Huang Hongrui (PM)
> **Phase**: Sprint 4 Closing → Sprint 5 Planning

---

## Sprint 4 (W8–W9): Core Feature Development ✅ CLOSED

### BACKEND (Bowei + Wang Xu)

| ID | Task | Owner | Status |
|----|------|-------|--------|
| S4-B01 | Auth API routes (register/verify/login/refresh) | Bowei | ✅ Done |
| S4-B02 | Database migrations (Alembic) | Bowei | ✅ Done |
| S4-B03 | Item CRUD API (`/api/v1/items`) | Wang Xu | ✅ Done |
| S4-B04 | Search & filter API (`/api/v1/search`) | Wang Xu | ✅ Done |
| S4-B05 | Image upload API (Cloudinary) | Wang Xu | ✅ Done |
| S4-B06 | User profile API (`/api/v1/users`) | Wang Xu | ✅ Done |
| S4-B07 | Reviews API (`/api/v1/reviews`) | Wang Xu | ✅ Done |
| S4-B08 | Firebase chat service | Wang Xu | ✅ Done |
| S4-B09 | API documentation (Swagger UI) | Bowei | ✅ Done |
| S4-B10 | Docker + docker-compose | Bowei | ✅ Done |
| S4-B11 | API router integration (W9) | Bowei | ✅ Done |
| S4-B12 | Backend test suite (50+ cases, W9) | Wang Xu | ✅ Done |
| S4-B13 | CI/CD test job fix (W9) | Bowei | ✅ Done |

### FRONTEND — WEB (Renxian + Jiahai)

| ID | Task | Owner | Status |
|----|------|-------|--------|
| S4-F01 | Next.js 14 project scaffold | Renxian | ✅ Done |
| S4-F02 | Dark Sidebar navigation component | Renxian | ✅ Done |
| S4-F03 | API client (axios + JWT interceptor) | Renxian | ✅ Done |
| S4-F04 | Zustand stores (auth/items/filter) | Renxian | ✅ Done |
| S4-F05 | ItemCard grid component | Renxian | ✅ Done |
| S4-F06 | Home page (grid + search + category chips) | Renxian | ✅ Done |
| S4-F07 | Auth pages (Login/Register/VerifyEmail) | Renxian | ✅ Done |
| S4-F08 | ItemDetail page | Renxian | ✅ Done |
| S4-F09 | CreateListing page (image upload) | Renxian | ✅ Done |
| S4-F10 | SearchResults + FilterModal | Jiahai | ✅ Done |
| S4-F11 | ChatList page | Jiahai | ✅ Done |
| S4-F12 | ChatRoom page (Firebase real-time) | Jiahai | ✅ Done |
| S4-F13 | Profile page + EditProfile | Jiahai | ✅ Done |
| S4-F14 | Settings page | Jiahai | ✅ Done |
| S4-F15 | Reviews page + Rating summary | Jiahai | ✅ Done |
| S4-F16 | MyListings page | Jiahai | ✅ Done |
| S4-F17 | Firebase integration (W9) | Jiahai | ✅ Done |
| S4-F18 | Frontend-backend integration (W9) | Renxian | ✅ Done |
| S4-F19 | Component tests setup (W9) | Jiahai | ✅ Done |

### PM & QA

| ID | Task | Owner | Status |
|----|------|-------|--------|
| S4-Q01 | Web design specifications | Junliang | ✅ Done |
| S4-Q02 | Updated test cases (web adaptation) | Junliang | ✅ Done |
| S4-Q03 | W8 meeting agenda | Hongrui | ✅ Done |
| S4-Q04 | W8 progress report | Hongrui | ✅ Done |
| S4-Q05 | Risk register W8 update | Hongrui | ✅ Done |
| S4-Q06 | W9 meeting agenda | Hongrui | ✅ Done |
| S4-Q07 | W9 progress report | Hongrui | ✅ Done |
| S4-Q08 | Risk register W9 update | Hongrui | ✅ Done |
| S4-Q09 | Test execution report | Junliang | ✅ Done |
| S4-Q10 | Usability test plan | Junliang | ✅ Done |

**Sprint 4 Final: 42/42 tasks completed ✅ (100%)**

---

## Sprint 5 (W10): Testing & Final Delivery 🔴 IN PROGRESS

| ID | Task | Owner | Priority |
|----|------|-------|----------|
| S5-T01 | Backend unit tests (unblock DB tests) | Bowei + Wang Xu | P0 |
| S5-T02 | Frontend component tests (Jest) | Renxian + Jiahai | P0 |
| S5-T03 | Integration tests (API + DB) | Bowei + Wang Xu | P0 |
| S5-T04 | E2E tests (Cypress) | Junliang | P1 |
| S5-T05 | Bug fixes | All | P0 |
| S5-D01 | Deploy backend to AWS EC2 (production) | Bowei | P0 |
| S5-D02 | Deploy frontend to Vercel (production) | Renxian | P0 |
| S5-D03 | Mobile app scaffold (Expo) | Renxian + Jiahai | P1 |
| S5-D04 | Usability testing (10-15 students) | Junliang | P1 |
| S5-D05 | Final report | All | P0 |
| S5-D06 | Final presentation + demo video | All | P0 |

---

## Burn-Down Summary

| Sprint | Weeks | Tasks Total | Done | In Progress | TODO |
|--------|-------|-------------|------|-------------|------|
| Sprint 1 | W1–W2 | 5 | 5 | 0 | 0 |
| Sprint 2 | W3–W5 | 9 | 9 | 0 | 0 |
| Sprint 3 | W6–W7 | 30 | 15 | 0 | 15 |
| Sprint 4 | W8–W9 | 42 | 42 | 0 | 0 |
| **Sprint 5** | **W10** | **11** | **0** | **0** | **11** |

> 🎯 **On track for W10 final delivery.** All feature work complete. Only testing, deployment, and documentation remain.

---

## Key Risks (Updated W9)

| Risk | Severity | Status | Mitigation |
|------|----------|--------|------------|
| EC2 deployment not ready | HIGH | 🔴 | Bowei provisioning; fallback: demo with localhost |
| Database unavailable for tests | MEDIUM | 🟡 | 10 tests blocked; CI can use PostgreSQL service container |
| Firebase not configured in prod | MEDIUM | 🟡 | Service account ready; needs env var injection |
| Mobile app not delivered | HIGH | 🟡 | Expo scaffold W10; MVP web-only if needed |
| Usability testing recruitment | LOW | 🟢 | 15 students recruited by Junliang |

---

> **Sprint 5 Kickoff**: W10 Mon (2026-07-13). Final delivery: W10 Fri (2026-07-17).
