# SG CampusSwap — Risk Register W9 Update

> **Updated**: 2026-07-12 (Week 9) | **Author**: Huang Hongrui (PM)
> **Previous Update**: W8 (2026-07-07)

---

## Risk Matrix

| ID | Risk | Category | Probability | Impact | Severity | Trend | Owner |
|----|------|----------|-------------|--------|----------|-------|-------|
| R01 | Timeline delay — not ready for W10 delivery | Schedule | Low (↓) | Critical | MEDIUM | ↓ Improving | Hongrui |
| R02 | AWS EC2 deployment delay | Infrastructure | Medium | High | HIGH | → Stable | Bowei |
| R03 | PostgreSQL test DB unavailable | Infrastructure | Low | Medium | LOW | 🆕 New | Wang Xu |
| R04 | Firebase chat not tested at scale | Technical | Low | Medium | LOW | ↓ Improving | Jiahai |
| R05 | Cloudinary quota exceeded | External | Low | Medium | LOW | → Stable | Wang Xu |
| R06 | Mobile app timeline compressed | Schedule | High | High | HIGH | → Stable | Renxian |
| R07 | Frontend-backend integration issues | Technical | Low | High | MEDIUM | ↓ Improving | Renxian |
| R08 | Usability testing recruitment shortage | People | Low | Medium | LOW | → Stable | Junliang |
| R09 | CI/CD pipeline failures | Infrastructure | Low | Medium | LOW | ↓ Improving | Bowei |
| R10 | Team member unavailability | People | Low | High | MEDIUM | → Stable | Hongrui |

---

## Detailed Risk Analysis

### R01: Timeline Delay
- **W8 Status**: MEDIUM — Strategy pivot (mobile→web) compressed timeline
- **W9 Status**: LOW — All 42 Sprint 4 tasks completed. Only testing + deployment remain. Web development faster than expected.
- **Mitigation**: Buffer W10 for final fixes. Reduce scope (mobile app → web-only MVP) if needed.
- **Trigger**: >3 critical bugs found in W10.

### R02: EC2 Deployment Delay
- **W8 Status**: Not tracked
- **W9 Status**: HIGH — EC2 instance provisioning pending. Bowei responsible.
- **Mitigation**: Fallback: demo with localhost + ngrok if EC2 not ready. Vercel for frontend only.
- **Trigger**: EC2 not provisioned by W10 Wed.

### R03: PostgreSQL Test DB Unavailable
- **W8 Status**: Not tracked
- **W9 Status**: LOW — 10 tests blocked awaiting PostgreSQL. CI already has PostgreSQL service container.
- **Mitigation**: Use SQLite for local dev tests. CI/CD uses PostgreSQL service.
- **Trigger**: CI test job fails due to DB connection errors.

### R04: Firebase Chat Scale
- **W8 Status**: MEDIUM
- **W9 Status**: LOW — Free tier (50K reads/day) sufficient for MVP with < 100 users.
- **Mitigation**: Mock mode available when Firebase not configured.

### R05: Cloudinary Quota
- **W8 Status**: LOW
- **W9 Status**: LOW — 5-image limit + compression keeps usage within free tier (25GB).
- **Mitigation**: Mock upload service falls back to placeholder URLs.

### R06: Mobile App Timeline
- **W8 Status**: HIGH
- **W9 Status**: HIGH — Strategy shifted mobile to post-web. W10 scope: Expo scaffold only.
- **Mitigation**: Web app is mobile-responsive. Ship web-only MVP if needed.

### R07: Frontend-Backend Integration
- **W8 Status**: Not tracked (separate development)
- **W9 Status**: MEDIUM — CORS configured, API client ready. Integration testing done.
- **Mitigation**: Shared API types between frontend and backend. Swagger docs at `/docs`.

### R08: Usability Testing Recruitment
- **W8 Status**: Not tracked
- **W9 Status**: LOW — Junliang has recruitment plan. 10-15 students targeted.
- **Mitigation**: Can test internally with team members if recruitment falls short.

### R09: CI/CD Pipeline
- **W8 Status**: Test job failing
- **W9 Status**: LOW — Lint job passes. Test job structure ready, needs DB env.
- **Mitigation**: Test job skips DB tests when DB unavailable.

### R10: Team Member Unavailability
- **W8 Status**: Not tracked
- **W9 Status**: MEDIUM — All members available. W10 is critical week.
- **Mitigation**: All code committed to GitHub. Bus factor ≥ 2 for all components.

---

## Risk Trend Summary

| Trend | Count | Risks |
|-------|-------|-------|
| ↓ Improving | 4 | R01, R04, R07, R09 |
| → Stable | 5 | R02, R05, R06, R08, R10 |
| ↑ Worsening | 0 | — |
| 🆕 New | 1 | R03 |

---

## Top 3 Risks for W10

1. **R02 — EC2 Deployment** (HIGH): Must resolve by W10 Wed
2. **R06 — Mobile App Timeline** (HIGH): Accept risk; web-only MVP is viable
3. **R01 — Timeline Delay** (MEDIUM): Low probability but high impact

---

> **Next Review**: W10 Fri (2026-07-17) — Final risk assessment before delivery.
