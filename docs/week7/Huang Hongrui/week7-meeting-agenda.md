# SG CampusSwap — Week 7 Team Meeting Agenda

> **Date**: Wednesday, Week 7, 11:00 AM – 1:00 PM  
> **Location**: Face-to-face (team gathering slot)  
> **Chair**: Huang Hongrui (PM) | **Note-taker**: Rotating (TBD)

---

## 1. Stand-up Round (15 min)

Each member answers 3 questions:

| Member | What did you do? | What will you do? | Any blockers? |
|--------|-----------------|-------------------|---------------|
| Hongrui (PM) | | | |
| Renxian (FE Lead) | | | |
| Bowei (BE Lead) | | | |
| Jiahai (FE Dev) | | | |
| Wang Xu (BE Dev) | | | |
| Junliang (UI/QA) | | | |

---

## 2. Critical Discussion: Code Gap (20 min)

**The Problem**: GitHub repo has zero application code as of Week 7. Stage 3 Foundation (W5–W6) deliverables are not visible.

**Questions to resolve**:
- [ ] Has any code been written offline (not pushed)?
- [ ] What is the status of: FastAPI scaffold? Auth module? Expo project? Database schema?
- [ ] Have cloud accounts been created (AWS, Neon, Cloudinary, Firebase, SendGrid)?
- [ ] What happened during study weeks (SW1–SW2)?

**Expected outcome**:
- [ ] `develop` branch created before this meeting ends
- [ ] Concrete push deadline: backend scaffold + mobile scaffold by **Friday W7 5:00 PM**
- [ ] PM to verify repo status Saturday morning

---

## 3. Week 7 Presentation Prep (15 min)

- [ ] Confirm presentation date/time this week
- [ ] Assign speaking roles (adjust based on attendance)
- [ ] Content outline: progress update, demo (if any), risks, next steps
- [ ] Maximum 2 hours prep time per person

**Decision**: Who presents? What slides are needed?

---

## 4. Sprint Backlog for W7–W8 (25 min)

Review each task, confirm owner, set deadline:

### Backend (Bowei + Wang Xu)
| Task | Owner | Deadline | Status |
|------|-------|----------|--------|
| FastAPI scaffold + project structure | Bowei | Fri W7 | ☐ |
| PostgreSQL schema (Alembic migrations) | Bowei | Fri W7 | ☐ |
| Auth module (JWT + domain whitelist + email code) | Bowei | Mon W8 | ☐ |
| Item CRUD API | Wang Xu | Wed W8 | ☐ |
| Search & filter API | Wang Xu | Wed W8 | ☐ |
| Image upload API (Cloudinary) | Wang Xu | Fri W8 | ☐ |
| Firebase chat backend | Wang Xu | Fri W8 | ☐ |
| CI/CD (GitHub Actions) | Bowei | Fri W8 | ☐ |
| AWS EC2 + Nginx + HTTPS | Bowei | Fri W8 | ☐ |

### Frontend (Renxian + Jiahai)
| Task | Owner | Deadline | Status |
|------|-------|----------|--------|
| Expo project scaffold + navigation | Renxian | Fri W7 | ☐ |
| HomeScreen (item feed + infinite scroll) | Renxian | Wed W8 | ☐ |
| ItemDetailScreen | Renxian | Wed W8 | ☐ |
| CreateListingScreen + image picker | Renxian | Fri W8 | ☐ |
| SearchResultsScreen + FilterModal | Jiahai | Wed W8 | ☐ |
| ChatListScreen + ChatScreen | Jiahai | Fri W8 | ☐ |
| ProfileScreen + EditProfile + ReviewsScreen | Jiahai | Fri W8 | ☐ |
| API client setup + Zustand stores | Renxian | Mon W8 | ☐ |

### Design & QA (Junliang)
| Task | Owner | Deadline | Status |
|------|-------|----------|--------|
| Final Figma mockups (all screens) | Junliang | Wed W7 | ☐ |
| Test case document (draft) | Junliang | Fri W8 | ☐ |
| GitHub Issues bug template + labels | Junliang | Wed W7 | ☐ |
| Recruit 10–15 usability testers | Junliang | Fri W8 | ☐ |

### All Members
| Task | Owner | Deadline | Status |
|------|-------|----------|--------|
| Literature review (ongoing) | All | W10 | 🔵 |
| Week 7 presentation | All | This week | 🔴 |

---

## 5. Risk Review (10 min)

Review [risk-register.md](risk-register.md):
- 🔴 **BLOCK-001**: Zero code — action plan above
- 🔴 **BLOCK-002**: No CI/CD — Bowei to start W7
- 🔴 **BLOCK-003**: Cloud accounts unconfirmed — Bowei to report today
- 🟡 Firebase complexity — Wang Xu + Jiahai pair strategy

---

## 6. Any Other Business (5 min)

- [ ] Next Sprint Review date: Friday W7, 5:00–6:00 PM
- [ ] Sprint Retrospective: after Review, 30–45 min
- [ ] Literature review Google Doc link — share in WeChat

---

## 7. Action Items Summary

| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Create `develop` branch | Bowei | During meeting |
| 2 | Push backend scaffold + auth | Bowei | Fri W7 5PM |
| 3 | Push mobile scaffold + navigation | Renxian | Fri W7 5PM |
| 4 | Report cloud account status | Bowei | During meeting |
| 5 | Share Figma mockup status | Junliang | During meeting |
| 6 | Prepare W7 presentation slides | Hongrui | Thu W7 |
| 7 | Create GitHub Issues template | Junliang | Wed W7 |
| 8 | Verify repo status | Hongrui | Sat W7 AM |

---

> **Minutes taker**: Rotating schedule — check WeChat for this week's assigned note-taker.  
> **Minutes due**: Within 24 hours of meeting end, uploaded to Google Drive.
