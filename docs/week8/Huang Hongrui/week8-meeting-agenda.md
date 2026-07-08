# SG CampusSwap — Week 8 Team Meeting Agenda

> **Date**: 2026-07-03 (Friday) | **Time**: 14:00–15:30 (90 min) | **Platform**: Zoom
> **Attendees**: All 6 members | **Chair**: Huang Hongrui (PM)

---

## 1. Strategy Update: Web-First Pivot (10 min) — Hongrui

### Background
- Original plan: Expo React Native mobile app
- New approach: Next.js web app → mobile app (shared API client + types)
- Figma Make prototype ("Web-version-request") received from external stakeholder

### Decision Points
- ✅ Web framework: Next.js 14 (App Router)
- ✅ UI approach: Custom components matching dark sidebar design
- ✅ Mobile strategy: Build after web is feature-complete
- ⚠️ Timeline impact: Web development is faster than React Native, offsetting pivot cost

---

## 2. Backend Progress Review (15 min) — Bowei + Wang Xu

### Bowei (Backend Lead)
- [ ] Auth API routes implemented and tested
- [ ] Alembic migrations created and verified
- [ ] Docker + docker-compose setup
- [ ] API documentation (Swagger UI)
- [ ] Questions: Neon PostgreSQL connection string shared?

### Wang Xu (Backend Dev)
- [ ] Item CRUD with pagination
- [ ] Search API (keyword + filters + sort)
- [ ] Image upload integration (Cloudinary)
- [ ] Firebase Firestore chat setup
- [ ] Reviews API with rating aggregation
- [ ] Questions: Cloudinary preset configuration?

---

## 3. Frontend Progress Review (20 min) — Renxian + Jiahai

### Renxian (Frontend Lead)
- [ ] Next.js 14 project scaffold with TypeScript
- [ ] Dark Sidebar navigation component
- [ ] API client with JWT interceptor
- [ ] Zustand stores (auth, items, filter)
- [ ] ItemCard grid component (responsive 1-4 columns)
- [ ] Home page with search bar + category chips + infinite scroll
- [ ] Auth pages (Login, Register, VerifyEmail)
- [ ] ItemDetail page with image carousel
- [ ] CreateListing page with image picker
- [ ] Demo: Show the current web app

### Jiahai (Frontend Dev)
- [ ] SearchResults page + FilterModal
- [ ] ChatList page (Firebase real-time listener)
- [ ] ChatRoom page (messaging UI)
- [ ] Profile page + EditProfile
- [ ] Settings page
- [ ] Reviews page with rating summary
- [ ] MyListings page
- [ ] Questions: Firebase config shared?

---

## 4. Design & QA Check-in (10 min) — Junliang

- [ ] Web design specifications (dark sidebar style)
- [ ] Component design system documented
- [ ] Design tokens exported
- [ ] Updated test cases (web adaptation)
- [ ] Figma: Any updates needed for web version?

---

## 5. Blockers & Issues (10 min) — All

### Current Blockers
1. **Server deployment**: No EC2 instance yet — Bowei to create by W9
2. **Cloud accounts**: Neon, Cloudinary, Firebase — credentials to share via `.env`
3. **Cross-origin**: CORS configuration for web frontend ↔ backend

### Open Discussion
- Anyone blocked on someone else's work?
- Any dependency surprises?

---

## 6. W9 Planning (15 min) — Hongrui

### W9 Goals
- Complete all remaining API endpoints
- Complete all frontend pages
- Begin testing (unit + integration)
- Deploy backend staging to EC2
- Deploy frontend preview to Vercel

### Task Assignment
| Task | Owner | Deadline |
|------|-------|----------|
| Deploy backend to EC2 | Bowei | W9 Wed |
| Deploy frontend to Vercel | Renxian | W9 Wed |
| Integration tests | Wang Xu | W9 Fri |
| Component tests | Jiahai | W9 Fri |
| Usability testing prep | Junliang | W9 Fri |
| Risk register update | Hongrui | W9 Fri |

---

## 7. Action Items Summary

| # | Action | Owner | By |
|---|--------|-------|-----|
| 1 | Share Neon DB connection string | Bowei | Today |
| 2 | Share Firebase config | Wang Xu | Today |
| 3 | Share Cloudinary preset | Wang Xu | Today |
| 4 | Create EC2 instance | Bowei | W9 Wed |
| 5 | Write integration tests | Wang Xu | W9 Fri |
| 6 | Write component tests | Jiahai | W9 Fri |
| 7 | Deploy frontend preview | Renxian | W9 Wed |
| 8 | Update Figma for web | Junliang | W9 Mon |

---

> **Next Meeting**: W9 Fri (2026-07-10) — Sprint 4 Review + Sprint 5 Planning
