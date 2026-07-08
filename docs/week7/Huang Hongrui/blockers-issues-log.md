# SG CampusSwap — Blockers & Issues Log

> **Last Updated**: 2026-06-24 (Week 7) | **Owner**: Huang Hongrui (PM)

---

## 🔴 Active Blockers

### BLOCK-001: No code in repository
| Field | Detail |
|-------|--------|
| **Severity** | 🔴 Critical |
| **Opened** | Week 7 |
| **Owner** | Bowei (BE Lead) + Renxian (FE Lead) |
| **Description** | GitHub repository contains only `README.md` on `master` branch. Zero application code. No `develop` branch. No feature branches. Stage 3 Foundation (W5–W6) has no visible output. |
| **Impact** | Blocks all Stage 4 Core Feature work. Frontend cannot integrate with backend. Chat module has no API to connect to. |
| **Resolution** | 1. Create `develop` branch immediately. 2. Bowei pushes backend scaffold (FastAPI + auth + DB) by Friday W7. 3. Renxian pushes mobile scaffold (Expo + navigation) by Friday W7. 4. PM verifies by Saturday W7. |
| **Status** | 🔴 Open |

### BLOCK-002: No CI/CD pipeline
| Field | Detail |
|-------|--------|
| **Severity** | 🟡 High |
| **Opened** | Week 7 |
| **Owner** | Bowei (BE Lead) |
| **Description** | `.github/workflows/` directory does not exist. No automated linting, testing, or deployment configured. Per plan, CI/CD should have been set up in W5–W6. |
| **Impact** | Manual testing only; risk of broken code on `main`; no deployment automation for W10 go-live. |
| **Resolution** | Set up GitHub Actions: lint (Flake8/ESLint) → test (Pytest/Jest) → deploy (SSH to EC2). Minimum: lint + test by W8. |
| **Status** | 🔴 Open |

### BLOCK-003: Cloud service accounts not confirmed
| Field | Detail |
|-------|--------|
| **Severity** | 🟡 High |
| **Opened** | Week 7 |
| **Owner** | Bowei (BE Lead) |
| **Description** | Free-tier deployment checklist (Technical Plan §10) includes: AWS account, Neon PostgreSQL, Cloudinary, Firebase, SendGrid. Status of these accounts is unknown — no configuration files in repo. |
| **Impact** | Backend cannot connect to database. Chat cannot use Firestore. Images cannot upload. Auth emails cannot send. |
| **Resolution** | Bowei to report account status by Wednesday W7 meeting. Create shared team credential document (Google Drive, access-restricted). |
| **Status** | 🔴 Open |

---

## 🟡 Open Issues

| ID | Issue | Owner | Opened | Status |
|----|-------|-------|--------|--------|
| ISS-001 | Figma high-fidelity mockup status unknown — all screens needed for FE development | Junliang | W7 | 🟡 Open |
| ISS-002 | Week 7 presentation content not prepared | Hongrui | W7 | 🟡 Open |
| ISS-003 | User testing recruitment (10–15 students) not started — needed W8–W9 | Junliang | W7 | 🟡 Open |
| ISS-004 | Literature review progress unknown — shared Google Doc needed | All | W7 | 🟡 Open |
| ISS-005 | `develop` branch not created — violates branching strategy from Code of Conduct | Bowei/Hongrui | W7 | 🟡 Open |
| ISS-006 | Study break (SW1–SW2) activity unclear — no progress report from team | All | W7 | 🟡 Open |

---

## ✅ Resolved

| ID | Issue | Resolved | Resolution |
|----|-------|----------|------------|
| BLK-000 | W4 presentation scheduling conflict | W5 | Presented in W5 instead |

---

## Weekly Resolution Target

| Week | Target |
|------|--------|
| **W7 (this week)** | BLOCK-001 resolved (code in repo), BLOCK-002 started, BLOCK-003 verified, ISS-001 through ISS-006 cleared |
| W8 | All blockers closed. CI passing. Feature branches active. |
