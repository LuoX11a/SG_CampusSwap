# SG CampusSwap — Weekly Meeting Minutes

> **Note-taker Rotation**: Hongrui → Renxian → Bowei → Jiahai → Wang Xu → Junliang

---

## Week 1 Meeting — Team Formation

| Field | Detail |
|-------|--------|
| **Date** | Week 1, 2026 TR2 |
| **Time** | Wednesday 11:00 AM – 1:00 PM |
| **Location** | JCU Campus |
| **Attendees** | Huang Hongrui, Renxian Tang, Wang Bowei, Jiahai Xiong, Wang Xu, Junliang Li |
| **Note-taker** | Huang Hongrui |

### Agenda
1. Team introductions
2. Project brainstorming
3. Role assignment

### Discussion Summary

**Team Formation**: All 6 members present. Each member introduced their technical background and interests.

**Project Direction**: Brainstormed several ideas:
- Student marketplace (二手交易平台) ← selected
- Study group matching app
- Campus event aggregator

**Decision**: Chose **SG CampusSwap** — a campus-centric C2C marketplace. Rationale:
- Addresses real student need (textbooks, electronics, furniture)
- Clear MVP scope
- Technically feasible within 12 weeks
- Strong alignment with Singapore's sustainability goals

**Roles Assigned**:
| Role | Member | Rationale |
|------|--------|-----------|
| PM | Huang Hongrui | Prior project coordination experience |
| FE Lead | Renxian Tang | React/React Native experience |
| BE Lead | Wang Bowei | Python/FastAPI experience |
| FE Dev | Jiahai Xiong | Frontend development background |
| BE Dev | Wang Xu | Backend + Firebase experience |
| UI/QA | Junliang Li | Design interest + attention to detail |

### Action Items
| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Research existing student marketplaces | All | W2 |
| 2 | Draft project proposal outline | Hongrui | W2 |
| 3 | Survey 30–50 students for demand validation | All | W2 |

---

## Week 2 Meeting — Project Definition

| Field | Detail |
|-------|--------|
| **Date** | Week 2, 2026 TR2 |
| **Time** | Wednesday 11:00 AM – 1:00 PM |
| **Location** | JCU Campus |
| **Attendees** | All 6 members |
| **Note-taker** | Renxian Tang |

### Agenda
1. User survey results review
2. MVP feature scope
3. Assessment 1 planning

### Discussion Summary

**User Survey Results**: ~40 students surveyed. Key findings:
- 85% have bought/sold second-hand goods
- Top pain points: trust (70%), meetup coordination (55%), item discovery (45%)
- 90% would use a student-only marketplace

**MVP Features** (prioritised):
1. University email registration + verification
2. Item listing with photos
3. Course-code textbook search
4. Real-time in-app chat
5. Campus-based filtering
6. User ratings & reviews

**Out of Scope (Future)**:
- Wishlist
- Price negotiation/offer system
- Push notifications
- Listing bump/promote

### Action Items
| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Write Assessment 1 (project proposal) | All sections divided | W3 |
| 2 | Literature review — each find 2 initial sources | All | W3 |
| 3 | Create WeChat group for async stand-ups | Hongrui | Done |

---

## Week 3 Meeting — Assessment 1 Finalisation

| Field | Detail |
|-------|--------|
| **Date** | Week 3, 2026 TR2 |
| **Time** | Wednesday 11:00 AM – 1:00 PM |
| **Location** | JCU Campus |
| **Attendees** | All 6 members |
| **Note-taker** | Wang Bowei |

### Agenda
1. Assessment 1 review & submission
2. System design kickoff
3. GitHub setup plan

### Discussion Summary

**Assessment 1**: All sections compiled and reviewed. Submitted via LearnJCU.

**System Design Kickoff**:
- Bowei presented initial database schema (users, items, reviews, transactions)
- Renxian presented React Native navigation structure
- Junliang started low-fidelity wireframes in Figma

**Tech Stack Decision**:
- FastAPI chosen over Django (async support, auto-Swagger)
- Expo chosen over bare React Native (easier build, OTA updates)
- Neon chosen over Supabase for PostgreSQL (larger free tier: 1 GB vs 500 MB)
- Firebase Firestore chosen for chat (free tier, real-time listeners)

### Action Items
| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Create GitHub repo | Bowei | W4 |
| 2 | Draft Technical Plan document | Bowei | W4 |
| 3 | Continue Figma wireframes | Junliang | W4 |
| 4 | Write API endpoint definitions | Bowei + Wang Xu | W4 |

---

## Week 4 Meeting — GitHub Setup & Presentation Prep

| Field | Detail |
|-------|--------|
| **Date** | Week 4, 2026 TR2 |
| **Time** | Wednesday 11:00 AM – 1:00 PM |
| **Location** | JCU Campus |
| **Attendees** | All 6 members |
| **Note-taker** | Jiahai Xiong |

### Agenda
1. GitHub repository setup verification
2. Presentation preparation
3. System design document review

### Discussion Summary

**GitHub Setup**: 
- Repository created: https://github.com/LuoX11a/SG_CampusSwap
- All members verified GitHub accounts are accessible
- Initial `README.md` pushed to `master` branch with: project overview, tech stack badges, project structure, setup guide, team roles, development workflow
- `.gitignore` ready for Python + Node.js
- Branch protection to be configured on `main`

**Presentation Preparation**:
- Prepared slides and speaking script for in-class presentation
- Assigned speaking parts among team members
- Due to class scheduling, presentation deferred to Week 5
- ⚠️ Speaking assignments may need adjustment in W5 based on attendance

**System Design Review**:
- Database schema: 5 core tables confirmed (users, items, item_images, reviews, transactions)
- API endpoints: 15 endpoints across 5 resource groups
- Frontend screens: 12 screens mapped in navigation tree
- Architecture diagram: FastAPI → PostgreSQL + Firebase + Cloudinary
- All documented in `SG_CampusSwap_Technical_Plan.md` and synced to `README.md`

**Code of Conduct**: All members reviewed and agreed to the Team Code of Conduct. Hard copy signed (see `Team Code of Conduct Agreement.pdf`).

### Action Items
| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Push README to GitHub | Bowei | Done (W4) |
| 2 | Prepare for W5 presentation (adjust if needed) | All | W5 |
| 3 | Create `develop` branch | Bowei | W5 |
| 4 | High-fidelity Figma mockups | Junliang | W5 |
| 5 | Start FastAPI project scaffold | Bowei | W5 |
| 6 | Start Expo project scaffold | Renxian | W5 |

---

## Week 5 Meeting — Presentation & Pre-Study Break

| Field | Detail |
|-------|--------|
| **Date** | Week 5, 2026 TR2 |
| **Time** | Wednesday 11:00 AM – 1:00 PM |
| **Location** | JCU Campus |
| **Attendees** | All 6 members |
| **Note-taker** | Wang Xu |

### Agenda
1. In-class presentation delivery
2. Development workflow confirmation
3. Study break (SW1–SW2) plan
4. Week 7 presentation preview

### Discussion Summary

**Presentation Delivered**: 
- Team presented project proposal, problem statement, tech stack, and timeline to the class
- All speaking parts delivered; attendance was full
- Instructor feedback: [To be filled]

**Development Workflow Confirmed**:
- Agile/Scrum methodology — no changes
- 2-week sprint cycles — no changes
- Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`) — no changes
- Branching: `main` → `develop` → `feature/*`, `fix/*` — no changes
- Code review: ≥1 approving review, within 24 hours — no changes

**Study Break Plan (SW1–SW2)**:
- Policy: Light work only — no new feature development
- Each member to focus on literature review contributions
- PM (Hongrui) to push progress forward: sprint backlog grooming, W7 presentation prep
- Devs may optionally familiarise with toolchains (React Native, FastAPI, Firebase) but no feature code expected

**Week 7 Presentation**: Another in-class presentation is scheduled for Week 7. PM to coordinate slides and speakers when class schedule is confirmed.

### Action Items
| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Literature review — find 2+ sources each during study break | All | End of SW2 |
| 2 | Sprint backlog grooming (review + prioritise W6–W8 tasks) | Hongrui | During SW1–SW2 |
| 3 | W7 presentation draft outline | Hongrui | SW2 |
| 4 | Resume full development velocity in W6 | All | W6 |
| 5 | FastAPI + Expo scaffolds pushed to `develop` | Bowei + Renxian | W6 (after break) |

---

## Study Week SW1–SW2 — Async Check-in

| Field | Detail |
|-------|--------|
| **Period** | Study Weeks 1–2 (after W5) |
| **Communication** | WeChat async only |
| **Activity** | Literature review + optional toolchain familiarisation |

### Member Check-ins (via WeChat)

| Member | SW1 Update | SW2 Update |
|--------|-----------|-----------|
| Hongrui (PM) | Sprint backlog updated | W7 agenda draft started |
| Renxian (FE) | Expo/React Native docs review | — |
| Bowei (BE) | Neon + Cloudinary account research | — |
| Jiahai (FE) | Firebase Firestore docs review | — |
| Wang Xu (BE) | Cloudinary upload API research | — |
| Junliang (QA) | Figma mockup refinement | Usability test plan draft |

> ⚠️ **PM Note (W7)**: Study break check-ins were light. No code was pushed during this period as per policy. Full development was expected to resume in W6. As of W7, code status in repo is unknown — **this is the #1 blocker** (see `blockers-issues-log.md`).

---

> **Minutes stored in**: Google Drive (link to be added) + `docs/meeting-minutes/`  
> **Next meeting**: Week 7 Wednesday 11:00 AM — see `docs/week7-meeting-agenda.md`
