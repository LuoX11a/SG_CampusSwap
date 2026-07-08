# SG CampusSwap — Risk Register Update (Week 8)

> **Updated**: 2026-07-05 | **Author**: Huang Hongrui (PM)
> **Review Cycle**: Weekly

---

## Risk Matrix

| Likelihood → | Low | Medium | High |
|--------------|-----|--------|------|
| **CRITICAL** | | | R1 (was R2) |
| **HIGH** | R4, R7 | R3, R5 | R2 |
| **MEDIUM** | | R6, R8 | |
| **LOW** | | | |

---

## Active Risks

### 🚨 CRITICAL

#### R1: Mobile App Timeline Compression
| Field | Value |
|-------|-------|
| **Status** | 🆕 NEW (W8) |
| **Severity** | CRITICAL |
| **Likelihood** | High |
| **Description** | Web-first strategy delays mobile (Expo) development to W10. Only 1 week remains for building, testing, and deploying both Android APK and iOS TestFlight. |
| **Impact** | Mobile app may not be ready for final presentation |
| **Mitigation** | Share API client + types between web & mobile. Use Expo Web as bridge. Prioritize Android APK over iOS TestFlight. |
| **Contingency** | Demo web app in mobile browser + PWA as fallback |
| **Owner** | Renxian Tang |

---

### 🔴 HIGH

#### R2: No Deployed Environment
| Field | Value |
|-------|-------|
| **Status** | 🔵 ONGOING (since W7) |
| **Severity** | HIGH |
| **Likelihood** | High |
| **Description** | AWS EC2 instance not yet created. Neon PostgreSQL, Cloudinary, Firebase, SendGrid accounts not yet provisioned. Backend and frontend cannot be tested in production-like environment. |
| **Impact** | Delayed integration testing, deployment risks undiscovered |
| **Mitigation** | Bowei to create all cloud accounts by W9 Wed. Use free tiers (Neon, Cloudinary, Firebase all have generous free plans). |
| **Contingency** | Run backend locally for demo if deployment fails |
| **Owner** | Wang Bowei |
| **Deadline** | W9 Wed (2026-07-08) |

#### R3: Integration Failures Between Web Frontend and Backend
| Field | Value |
|-------|-------|
| **Status** | 🟡 MONITORING |
| **Severity** | HIGH |
| **Likelihood** | Medium |
| **Description** | Frontend (Next.js) and backend (FastAPI) developed in parallel. API contract mismatches (field names, response shapes, error formats) may surface during integration. |
| **Impact** | Rework on both sides, delayed testing |
| **Mitigation** | Shared TypeScript types generated from OpenAPI schema. CORS configured correctly. Both teams using the same `.env.example`. |
| **Contingency** | Dedicated integration fix sprint W9 Thu-Fri |
| **Owner** | Renxian + Bowei |

#### R4: Firebase Free Tier Limits
| Field | Value |
|-------|-------|
| **Status** | 🟢 LOW RISK |
| **Severity** | HIGH |
| **Likelihood** | Low |
| **Description** | Firebase Firestore free tier: 50K reads/day, 20K writes/day. Chat real-time listeners may exceed read quota with many active users. |
| **Impact** | Chat stops working → poor UX during demo |
| **Mitigation** | Limit chat polling to visible chats only. Unsubscribe listeners on page unmount. Test with 10+ concurrent users. |
| **Owner** | Wang Xu |

#### R5: API Security Gaps
| Field | Value |
|-------|-------|
| **Status** | 🟡 MONITORING |
| **Severity** | HIGH |
| **Likelihood** | Medium |
| **Description** | No rate limiting, no CSRF protection, no input sanitization beyond Pydantic validation. JWT tokens stored in localStorage (XSS vulnerable). |
| **Impact** | Potential abuse (brute force, spam listings, token theft) |
| **Mitigation** | Add slowapi rate limiting before deploy. Use httpOnly cookies for JWT in production. Validate all file uploads (size, type). |
| **Contingency** | Accept for MVP; document as known limitation |
| **Owner** | Bowei |

---

### 🟡 MEDIUM

#### R6: Image Upload Abuse
| Field | Value |
|-------|-------|
| **Status** | 🟢 MONITORED |
| **Severity** | MEDIUM |
| **Likelihood** | Medium |
| **Description** | Cloudinary free tier has 25 GB storage / 25 GB bandwidth. Users uploading large images or inappropriate content. |
| **Mitigation** | Client-side resize to max 1200px before upload. Server-side validation (file type, size < 5MB). Max 5 images per listing. |
| **Owner** | Wang Xu |

#### R7: Third-Party Service Outages
| Field | Value |
|-------|-------|
| **Status** | 🟢 LOW RISK |
| **Severity** | HIGH |
| **Likelihood** | Low |
| **Description** | Neon (PostgreSQL), Cloudinary (images), Firebase (chat), SendGrid (email) — any one outage breaks a feature. |
| **Mitigation** | Graceful degradation — app shows "temporarily unavailable" instead of crashing. Offline stubs for critical flows. |
| **Owner** | All |

#### R8: Team Availability W10 (Exam Period)
| Field | Value |
|-------|-------|
| **Status** | 🟡 MONITORING |
| **Severity** | MEDIUM |
| **Likelihood** | Medium |
| **Description** | W10 overlaps with other course deadlines. Team members may have limited availability for final bug fixes and presentation prep. |
| **Mitigation** | Front-load critical work to W9. Have backup presenters for final demo. |
| **Owner** | Hongrui |

---

## Resolved Risks

| Risk | Resolution |
|------|------------|
| R1 (W7): No develop branch → code stuck locally | ✅ Code organized in week7/week8 folders; ready to push |
| R3 (W7): asyncpg Windows compatibility | ✅ Docker provides Linux environment; CI runs on Ubuntu |
| R4 (W7): Frontend framework indecision | ✅ Next.js 14 chosen; project scaffolded |

---

> **Next Review**: W9 Fri (2026-07-10)
> **Risk Owner Actions**: Bowei — create EC2 by W9 Wed. Renxian — plan mobile MVP scope.
