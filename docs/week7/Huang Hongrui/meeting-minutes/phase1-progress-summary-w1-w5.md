# SG CampusSwap — Phase 1 Progress Summary (Week 1 – Week 5)

> **Period**: 2026 TR2, Week 1 – Week 5 (Teaching Weeks)  
> **Current**: Week 7 (Post Study Break) | **Next Milestone**: Core Feature Development Complete by End of W8  
> **Prepared by**: Huang Hongrui (PM)

---

## 1. Weekly Progress Log

### Week 1 — Team Formation & Direction

| Done | Details |
|------|---------|
| ✅ Team assembled | 6 members confirmed: Hongrui (PM), Renxian (FE Lead), Bowei (BE Lead), Jiahai (FE), Wang Xu (BE), Junliang (UI/QA) |
| ✅ Project direction | Decided on a campus-centric C2C marketplace for Singapore university students — **SG CampusSwap** |
| ✅ Course requirements reviewed | Understood CP3102 assessment structure and deliverables |

### Week 2 — Project Definition

| Done | Details |
|------|---------|
| ✅ Project scope confirmed | Defined MVP features: verified registration, item listing, course-code search, in-app chat, user ratings |
| ✅ Target users identified | Singapore university students — NUS, NTU, SMU, SUTD, SUSS, SIT, polytechnics |
| ✅ User survey planned | Target 30–50 student respondents to validate demand |

### Week 3 — Assessment 1 Submission

| Done | Details |
|------|---------|
| ✅ Assessment 1 written & submitted | Project proposal + initial requirements documentation |
| ✅ Literature review started | All members began sourcing papers (Google Scholar, JCU Library) |
| ✅ Figma wireframes started | Junliang began low-fidelity wireframes |

### Week 4 — GitHub Setup & System Design Kickoff

| Done | Details |
|------|---------|
| ✅ GitHub repository created | [github.com/LuoX11a/SG_CampusSwap](https://github.com/LuoX11a/SG_CampusSwap) — all member accounts verified working |
| ✅ Initial commit pushed | `README.md` with project overview, tech stack, and structure → pushed to `master` |
| ✅ Tech stack finalized | FastAPI + PostgreSQL + React Native (Expo) + Firebase + Cloudinary + AWS Free Tier |
| ✅ Architecture confirmed | System architecture diagram, database schema draft, API endpoint definitions |
| ✅ Team Code of Conduct signed | All 6 members signed the agreement (see `Team Code of Conduct Agreement.pdf`) |
| ✅ Presentation drafted | Prepared in-class presentation script; presentation slot deferred to Week 5 due to scheduling |
| ⚠️ Division of speaking parts | Assigned for Week 4 — may adjust in Week 5 depending on attendance |

### Week 5 — Presentation & Pre-Study Week Wrap-up

| Done | Details |
|------|---------|
| ✅ In-class presentation delivered | Presented project proposal, problem statement, tech stack, and timeline to class |
| ✅ Development workflow confirmed | Agile/Scrum (2-week sprints), Conventional Commits, branching strategy unchanged |
| ✅ Foundation prep | PM confirmed plan to push progress forward during the upcoming study break |
| 📋 Next presentation | **Week 7** — a second in-class presentation is required; content TBD |

---

## 2. Progress vs. Gantt Chart (as of Week 5)

| Stage | Planned | Actual | Status |
|-------|---------|--------|--------|
| **Stage 1**: Initiation & Requirements | W1–W2 | W1–W3 | ✅ **Completed** |
| ├ Project Proposal | W1–W2 | W1–W2 | ✅ Done |
| ├ User Survey & Research | W1–W2 | W1–W2 | ✅ Done |
| └ Requirements Document | W2–W3 | W2–W3 | ✅ Done (Assessment 1) |
| **Stage 2**: System Design | W3–W4 | W3–W5 | ✅ **Largely Complete** |
| ├ Wireframes (Figma) | W3–W4 | W3–W4 | ✅ Done |
| ├ UI Prototype | W4–W5 | Partially done | ⚠️ Needs refinement |
| ├ Database Design | W3–W4 | W3–W4 | ✅ Done (schema documented) |
| └ API Design | W3–W4 | W3–W4 | ✅ Done (endpoints documented) |
| **Ongoing** | W1–W10 | W3–W10 | 🔵 Literature Review in progress |

---

## 3. Study Week Activity (SW1–SW2, After Week 5)

> **Policy**: Light work only — catch up on literature review, no new feature development.

| Member | Planned Activity |
|--------|-----------------|
| Hongrui (PM) | Sprint backlog grooming, literature review, Week 7 presentation preparation |
| Renxian (FE Lead) | Literature review, familiarise with React Native + Expo toolchain |
| Bowei (BE Lead) | Literature review, prototype FastAPI project scaffold, register free-tier accounts (Neon, Cloudinary, Firebase) |
| Jiahai (FE) | Literature review, research Firebase Firestore real-time chat patterns |
| Wang Xu (BE) | Literature review, research Cloudinary upload API and SendGrid email verification |
| Junliang (UI/QA) | Literature review, refine Figma high-fidelity mockups, draft usability test plan |

---

## 4. Where We Are Now — Week 7 (CW7)

> **This is the current week. Stage 3 (Foundation Development) should have been completed in W5–W6. Stage 4 (Core Feature Development) runs W6–W8.**

### ⚠️ Status Check Needed

The following should be confirmed complete or in-progress by now:

| Task | Owner | Expected | Needs Verification |
|------|-------|----------|-------------------|
| FastAPI project scaffold | Bowei | W5 | ☐ |
| PostgreSQL / Neon deployed | Bowei | W5 | ☐ |
| Auth module (JWT + domain whitelist + email code) | Bowei | W5–W6 | ☐ |
| Basic app navigation (Expo Router) | Renxian | W5–W6 | ☐ |
| CI/CD pipeline (GitHub Actions) | Bowei | W5–W6 | ☐ |
| Item CRUD API endpoints | Wang Xu | W6–W7 | ☐ |
| Search & filter API | Wang Xu | W7 | ☐ |
| Firebase chat module (backend) | Wang Xu | W7 | ☐ |
| Home screen (item feed) | Renxian | W6–W7 | ☐ |
| Item detail screen | Renxian | W6–W7 | ☐ |
| Create listing screen | Renxian | W7 | ☐ |
| Chat list + Chat screen | Jiahai | W7 | ☐ |
| Search & filter UI | Jiahai | W7 | ☐ |
| User profile screens | Jiahai | W7 | ☐ |
| Cloudinary upload API | Wang Xu | W7 | ☐ |
| Week 7 presentation | All | **W7** | 🔴 Due this week |

---

## 5. Immediate Action Items (Week 7)

### All Members
- [ ] **Week 7 in-class presentation** — prepare slides and rehearse; adjust speaking roles based on attendance
- [ ] **Literature review** — continue contributing to shared Google Doc; aim for solid draft by W8

### Huang Hongrui (PM)
- [ ] Verify all Stage 3 Foundation tasks are complete — flag any blockers immediately
- [ ] Update Gantt chart to reflect actual progress
- [ ] Organize Week 7 presentation content and speaker assignments

### Renxian Tang (FE Lead)
- [ ] Complete HomeScreen (item feed with infinite scroll)
- [ ] Complete ItemDetailScreen (with seller preview)
- [ ] Complete CreateListingScreen (with image picker integration)
- [ ] Integrate with backend Item CRUD + Search APIs
- [ ] Ensure Zustand state management structure is in place

### Wang Bowei (BE Lead)
- [ ] Verify all Foundation deliverables are complete (scaffold, auth, deployment, CI/CD)
- [ ] Ensure AWS EC2 instance is running with Nginx + HTTPS
- [ ] Support Wang Xu on Item APIs and Firebase integration

### Jiahai Xiong (FE Developer)
- [ ] Build ChatListScreen + ChatScreen (Firebase Firestore real-time)
- [ ] Build SearchResultsScreen + FilterModal
- [ ] Build user profile, edit profile, and reviews screens
- [ ] Ensure design fidelity against Junliang's Figma mockups

### Wang Xu (BE Developer)
- [ ] Complete Item CRUD API (`/api/v1/items`)
- [ ] Complete Search & Filter API (`/api/v1/items/search`)
- [ ] Complete Image Upload API (`/api/v1/upload/image` → Cloudinary)
- [ ] Set up Firebase Firestore chat structure
- [ ] Keep Swagger API documentation up to date

### Junliang Li (UI/UX & QA)
- [ ] Finalize Figma high-fidelity mockups for all remaining screens
- [ ] Begin writing test cases (unit + integration + usability scenarios)
- [ ] Set up GitHub Issues bug-tracking template and labels
- [ ] Start recruiting 10–15 student testers for W8–W9 usability testing

---

## 6. Risk Update

| Risk | Status | Notes |
|------|--------|-------|
| **App not completed on time** | 🟡 Monitor | 4 weeks to W10. Core features must be feature-complete by end of W8. |
| **Study break momentum loss** | 🟢 Resolved | Study weeks are over; team should be back to full velocity. |
| **Presentation in Week 7** | 🟡 Active | Second presentation this week — ensure it does not derail development time. |
| **Firebase chat complexity** | 🟡 Monitor | Per original risk plan, chat module should start by W7. This is the week. |
| **Scope creep** | 🟢 Controlled | Feature freeze after W4. New ideas go to Future Version backlog. |

---

## 7. Key Dates Ahead

| Week | Dates | Milestone |
|------|-------|-----------|
| W7 | Current | 🔴 In-class presentation + Core Features continue |
| W8 | Next | 🔴 **All core features must be complete**; testing begins |
| W9 | | Bug fixes, integration testing, usability testing (10–15 testers) |
| W10 | Final | 🚀 App deployment (APK/IPA), final report submission, final presentation |

---

> **Next Meeting**: Wednesday 11:00 AM – 1:00 PM (Weekly Team Meeting)  
> **Next Sprint Review**: Friday 5:00 PM (End of Week 7)  
> **Document Status**: This summary covers W1–W5 and bridges into current W7.  
> Prepared by Project Manager for the SG CampusSwap team, CP3102 2026 TR2.
