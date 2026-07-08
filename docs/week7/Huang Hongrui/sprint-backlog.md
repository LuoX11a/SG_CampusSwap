# SG CampusSwap — Sprint Backlog & Task Board

> **Last Updated**: 2026-06-24 (Week 7) | **Methodology**: Agile / Scrum (2-week sprints)  
> **Sprint 3**: Week 6–7 (Foundation Complete → Core Features 50%)  
> **Sprint 4**: Week 8–9 (Core Complete → Testing & QA)

---

## Sprint 1 (W1–W2): Initiation & Requirements ✅ COMPLETED

| ID | Task | Owner | Status | Notes |
|----|------|-------|--------|-------|
| S1-01 | Form team, define roles | All | ✅ Done | 6 members confirmed |
| S1-02 | Project proposal | Hongrui | ✅ Done | CP3102 Assessment 1 |
| S1-03 | User survey (30–50 students) | All | ✅ Done | Validated demand |
| S1-04 | Requirements document | All | ✅ Done | MVP scope defined |
| S1-05 | Team Code of Conduct | All | ✅ Done | All 6 signed |

## Sprint 2 (W3–W5): System Design ✅ COMPLETED

| ID | Task | Owner | Status | Notes |
|----|------|-------|--------|-------|
| S2-01 | Figma wireframes | Junliang | ✅ Done | Low-fidelity |
| S2-02 | Figma high-fidelity prototype | Junliang | ⚠️ Partial | Verify completion W7 |
| S2-03 | Database schema design | Bowei | ✅ Done | 5 core tables defined |
| S2-04 | API endpoint definition | Bowei + Wang Xu | ✅ Done | RESTful, documented |
| S2-05 | Tech stack finalization | Bowei + Renxian | ✅ Done | Documented in README |
| S2-06 | GitHub repo setup | Bowei | ✅ Done | LuoX11a/SG_CampusSwap |
| S2-07 | System architecture diagram | Bowei | ✅ Done | In Technical Plan |
| S2-08 | In-class presentation (W5) | All | ✅ Done | |
| S2-09 | Literature review start | All | 🔵 Ongoing | |

## Sprint 3 (W6–W7): Foundation + Core 50% 🔴 IN PROGRESS

| ID | Task | Owner | Status | Deadline | Notes |
|----|------|-------|--------|----------|-------|
| **BACKEND** |
| S3-B01 | Create `develop` branch | Bowei | 🔴 TODO | W7 Wed | **Critical blocker** |
| S3-B02 | FastAPI project scaffold | Bowei | 🔴 TODO | W7 Fri | `backend/` structure |
| S3-B03 | PostgreSQL schema + Alembic | Bowei | 🔴 TODO | W7 Fri | Users, Items, Reviews, Transactions |
| S3-B04 | Auth: register + verify + login + JWT | Bowei | 🔴 TODO | W8 Mon | Domain whitelist enforced |
| S3-B05 | Item CRUD API (`/api/v1/items`) | Wang Xu | 🔴 TODO | W8 Wed | |
| S3-B06 | Search & filter API | Wang Xu | 🔴 TODO | W8 Wed | Keyword, course code, category, price, campus |
| S3-B07 | Image upload API (Cloudinary) | Wang Xu | 🔴 TODO | W8 Fri | |
| S3-B08 | Firebase Firestore chat setup | Wang Xu | 🔴 TODO | W8 Fri | Chats + Messages collections |
| S3-B09 | User profile API | Wang Xu | 🔴 TODO | W8 Fri | |
| S3-B10 | Reviews API | Wang Xu | 🔴 TODO | W8 Fri | |
| S3-B11 | CI/CD pipeline (GitHub Actions) | Bowei | 🔴 TODO | W8 Fri | Lint → Test → Deploy |
| S3-B12 | AWS EC2 + Nginx + HTTPS | Bowei | 🔴 TODO | W8 Fri | ap-southeast-1 |
| S3-B13 | Cloud accounts setup | Bowei | 🔴 TODO | W7 Wed | Neon, Cloudinary, Firebase, SendGrid |
| **FRONTEND** |
| S3-F01 | Expo project scaffold + navigation | Renxian | 🔴 TODO | W7 Fri | Expo Router file-based routing |
| S3-F02 | API client setup (axios) + types | Renxian | 🔴 TODO | W8 Mon | |
| S3-F03 | Zustand stores (auth, items, filters) | Renxian | 🔴 TODO | W8 Mon | |
| S3-F04 | HomeScreen (item feed + infinite scroll) | Renxian | 🔴 TODO | W8 Wed | |
| S3-F05 | ItemDetailScreen + seller preview | Renxian | 🔴 TODO | W8 Wed | |
| S3-F06 | CreateListingScreen + image picker | Renxian | 🔴 TODO | W8 Fri | Cloudinary integration |
| S3-F07 | SearchResultsScreen + FilterModal | Jiahai | 🔴 TODO | W8 Wed | |
| S3-F08 | ChatListScreen | Jiahai | 🔴 TODO | W8 Fri | Firebase real-time |
| S3-F09 | ChatScreen (messaging) | Jiahai | 🔴 TODO | W8 Fri | Pair with Wang Xu |
| S3-F10 | ProfileScreen + EditProfile | Jiahai | 🔴 TODO | W8 Fri | |
| S3-F11 | MyListingsScreen | Jiahai | 🔴 TODO | W8 Fri | |
| S3-F12 | ReviewsScreen | Jiahai | 🔴 TODO | W8 Fri | |
| **DESIGN & QA** |
| S3-Q01 | Final Figma mockups (all screens) | Junliang | 🔴 TODO | W7 Wed | |
| S3-Q02 | GitHub Issues bug template + labels | Junliang | 🔴 TODO | W7 Wed | |
| S3-Q03 | Test case document (draft) | Junliang | 🟡 TODO | W8 Fri | |
| S3-Q04 | Usability test plan | Junliang | 🟡 TODO | W8 Fri | |
| S3-Q05 | Recruit 10–15 testers | Junliang | 🟡 TODO | W8 Fri | |
| **PM & DOCS** |
| S3-P01 | Risk register update | Hongrui | ✅ Done | W7 | `docs/risk-register.md` |
| S3-P02 | Blockers log | Hongrui | ✅ Done | W7 | `docs/blockers-issues-log.md` |
| S3-P03 | Sprint backlog (this doc) | Hongrui | ✅ Done | W7 | |
| S3-P04 | W7 meeting agenda | Hongrui | ✅ Done | W7 | `docs/week7-meeting-agenda.md` |
| S3-P05 | Final report framework | Hongrui | ✅ Done | W7 | `docs/final-report-framework.md` |
| S3-P06 | W7 presentation slides | Hongrui | 🔴 TODO | W7 Thu | |
| S3-P07 | Phase 1 progress summary | Hongrui | ✅ Done | W7 | `docs/meeting-minutes/phase1-progress-summary-w1-w5.md` |

## Sprint 4 (W8–W9): Core Complete + Testing ⚪ NOT STARTED

| ID | Task | Owner | Status | Notes |
|----|------|-------|--------|-------|
| **TESTING** |
| S4-T01 | Backend unit tests (auth, items, search) | Bowei + Wang Xu | ⚪ | Pytest |
| S4-T02 | Frontend component tests | Renxian + Jiahai | ⚪ | Jest + React Native Testing Library |
| S4-T03 | Integration tests (API + DB) | Bowei + Wang Xu | ⚪ | |
| S4-T04 | Usability testing (10–15 students) | Junliang | ⚪ | |
| S4-T05 | Bug fixes (based on testing) | All | ⚪ | |
| **DEPLOYMENT PREP** |
| S4-D01 | Build APK (Android) via EAS | Renxian | ⚪ | W9 |
| S4-D02 | Build IPA (iOS) via EAS | Renxian | ⚪ | W9 |
| S4-D03 | Google Play Internal Testing submit | Renxian | ⚪ | W10 |
| S4-D04 | TestFlight submit | Renxian | ⚪ | W10 |
| S4-D05 | Direct APK download + QR fallback | Renxian | ⚪ | W10 |

## Sprint 5 (W10): Final Delivery ⚪ NOT STARTED

| ID | Task | Owner | Status | Notes |
|----|------|-------|--------|-------|
| S5-01 | Final report submission | All | ⚪ | |
| S5-02 | Final presentation | All | ⚪ | |
| S5-03 | Literature review final | All | ⚪ | |
| S5-04 | Project handover documentation | Hongrui | ⚪ | |

---

## Burn-Down Summary

| Sprint | Weeks | Tasks Total | Done | In Progress | TODO |
|--------|-------|-------------|------|-------------|------|
| Sprint 1 | W1–W2 | 5 | 5 | 0 | 0 |
| Sprint 2 | W3–W5 | 9 | 7 | 1 | 1 |
| **Sprint 3** | **W6–W7** | **30** | **4** | **0** | **26** |
| Sprint 4 | W8–W9 | 9 | 0 | 0 | 9 |
| Sprint 5 | W10 | 4 | 0 | 0 | 4 |

> ⚠️ **WARNING**: Sprint 3 has 26 open tasks with 2 weeks remaining. Velocity is critically low.  
> **Action**: Must close minimum 13 tasks per week to catch up. Daily stand-ups must report concrete progress.

---

## Task Status Key

| Symbol | Meaning |
|--------|---------|
| ✅ Done | Completed and verified |
| 🔵 Ongoing | Continuous task, on track |
| 🔴 TODO | Not started, urgent |
| 🟡 TODO | Not started, can wait |
| ⚠️ Partial | Started but incomplete |
| ⚪ | Future sprint |
