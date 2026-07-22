# SG CampusSwap — Week 9 Team Meeting Agenda

> **Date**: 2026-07-10 (Friday) | **Time**: 14:00–15:30 (90 min) | **Platform**: Zoom
> **Attendees**: All 6 members | **Chair**: Huang Hongrui (PM)

---

## 1. Sprint 4 Review (15 min) — Hongrui

### W8 Recap
- ✅ All 27 Sprint 4 tasks completed
- ✅ Backend: 22 API endpoints across 6 route modules
- ✅ Frontend: 16 pages/screens built
- ✅ Design system + test plan updated for web
- 🔄 Strategy pivot: Mobile-first → Web-first (successful)

### W9 Goals
- Testing and quality assurance
- Deployment to staging
- Frontend-backend integration
- Bug fixes
- W10 final delivery preparation

---

## 2. Backend — Testing & Deployment (20 min) — Bowei + Wang Xu

### Bowei (Backend Lead)
- [ ] API routes integrated into main router
- [ ] All 6 route modules deployed: auth, items, users, reviews, search, upload
- [ ] Backend tests: 50+ test cases across 6 test files
- [ ] CI/CD pipeline passing (lint + test jobs)
- [ ] AWS EC2 deployment status
- [ ] Nginx + HTTPS configuration
- [ ] Rate limiting (slowapi)

### Wang Xu (Backend Dev)
- [ ] Unit tests for items API (GET/POST/PUT/DELETE/PATCH)
- [ ] Unit tests for users API
- [ ] Unit tests for reviews API
- [ ] Unit tests for search API
- [ ] Integration test framework with async DB fixtures
- [ ] Input sanitization review
- [ ] Questions: Database test environment ready?

---

## 3. Frontend — Integration & Testing (20 min) — Renxian + Jiahai

### Renxian (Frontend Lead)
- [ ] Frontend-backend API integration
- [ ] Vercel deployment (preview)
- [ ] Responsive testing: mobile, tablet, desktop
- [ ] Accessibility audit (axe DevTools)
- [ ] Performance optimization

### Jiahai (Frontend Dev)
- [ ] Firebase Firestore chat integration
- [ ] Reviews page API connection
- [ ] Profile pages API connection
- [ ] Component unit tests (Jest + React Testing Library)
- [ ] Questions: Firebase credentials configured?

---

## 4. QA & Testing (10 min) — Junliang

- [ ] Test execution progress (85 test cases)
- [ ] Bug reports logged
- [ ] Usability testing plan for W10
- [ ] Key issues found so far
- [ ] Figma design vs implementation review

---

## 5. Blockers & Issues (10 min) — All

### Current Status
1. **EC2 Instance**: Provisioned? SSH access working?
2. **Database**: Neon PostgreSQL connection tested?
3. **Firebase**: Service account configured?
4. **Cloudinary**: API keys distributed?
5. **Vercel**: Project created, env vars set?

### Open Discussion
- Anyone blocked?
- Any integration surprises?
- Timeline concerns for W10?

---

## 6. W10 Planning Preview (10 min) — Hongrui

### Sprint 5 Tasks (W10)
| Task | Owner |
|------|-------|
| Final testing (all categories) | All |
| Bug fixes | All |
| Backend deploy to production | Bowei |
| Frontend deploy to production | Renxian |
| Usability testing (10-15 students) | Junliang |
| Mobile app scaffold (Expo) | Renxian + Jiahai |
| Final report | All |
| Final presentation | All |

---

## 7. Action Items

| # | Action | Owner | By |
|---|--------|-------|-----|
| 1 | Confirm EC2 instance ready | Bowei | Today |
| 2 | Test DB connection from CI | Bowei | Today |
| 3 | Complete API tests | Wang Xu | W9 Fri |
| 4 | Complete component tests | Jiahai | W9 Fri |
| 5 | Deploy frontend preview | Renxian | W9 Fri |
| 6 | Execute all 85 test cases | Junliang | W9 Fri |
| 7 | W9 progress report | Hongrui | W9 Sun |

---

> **Next Meeting**: W10 Mon (2026-07-13) — Sprint 5 Kickoff
