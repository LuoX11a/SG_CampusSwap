# SG CampusSwap — Updated Gantt Chart (Week 7 Perspective)

> **Original**: W3 snapshot showing plan | **This version**: W7 reality check  
> **Progress**: ~40% of timeline elapsed (5 teaching weeks + 2 study weeks of 12)  
> **Overall Status**: 🟡 Behind schedule — Foundation code not yet in repository

---

## Timeline Overview

```
Week:   W1    W2    W3    W4    W5    SW1   SW2   W6    W7    W8    W9    W10
        ████████████████████████████████████████████████████████████████████████
        ████████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        

Legend:  █ = Completed   ▓ = In Progress / Partial   ░ = Not Started   ▒ = Study Break
```

---

## Stage-by-Stage Status

### ✅ Stage 1: Initiation & Requirements (W1–W2)
```
W1 ████████  W2 ████████  W3 ████░░░░  W4–W10 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```
| Task | Plan | Actual | Status |
|------|------|--------|--------|
| Project Proposal | W1–W2 | W1–W2 | ✅ Done |
| User Survey & Research | W1–W2 | W1–W2 | ✅ Done |
| Requirements Document | W2–W3 | W2–W3 | ✅ Done (Assessment 1) |

### ✅ Stage 2: System Design (W3–W4)
```
W1–W2 ░░░░░░░░  W3 ████████  W4 ████████  W5 ████░░░░  W6–W10 ░░░░░░░░░░░░░░
```
| Task | Plan | Actual | Status |
|------|------|--------|--------|
| Wireframes (Figma) | W3–W4 | W3–W4 | ✅ Done |
| UI Prototype (Hi-fi) | W4–W5 | W4–W5 (partial) | ⚠️ Verify with Junliang |
| Database Design | W3–W4 | W3–W4 | ✅ Done |
| API Design | W3–W4 | W3–W4 | ✅ Done |
| GitHub Repo Setup | W4 | W4 | ✅ Done |

### 🔴 Stage 3: Foundation Development (W5–W6)
```
W1–W4 ░░░░░░░░░░░░░░░░  W5 ░░░░░░░░  SW1 ▒▒  SW2 ▒▒  W6 ░░░░░░░░  W7 ░░░░░░
                         ↑ Planned start          ↑ Should be done by now
                         
ACTUAL:  W5 ████░░░░ (Presentation only) → SW1–SW2 study break → W6–W7: ??? (no code)
```
| Task | Plan | Actual | Status |
|------|------|--------|--------|
| FastAPI project scaffold | W5 | ? | 🔴 No evidence in repo |
| PostgreSQL + Neon deploy | W5 | ? | 🔴 No config in repo |
| Auth module (JWT + whitelist + email) | W5–W6 | ? | 🔴 No code in repo |
| Expo project scaffold + nav | W5–W6 | ? | 🔴 No code in repo |
| CI/CD pipeline | W5–W6 | ? | 🔴 No workflow files |
| AWS EC2 + Nginx + HTTPS | W6 | ? | 🔴 Status unknown |

### ⚪ Stage 4: Core Feature Development (W6–W8) — DEPENDENT ON STAGE 3
```
W1–W5 ░░░░░░░░░░░░░░░░░░░░  W6 ░░░░░░  W7 ←WE ARE HERE  W8 ░░░░░░  W9–W10 ░
                             ↑ Should have started W6
                             
ACTUAL: Cannot start until Stage 3 deliverables exist.
```
| Task | Plan | Status |
|------|------|--------|
| Item CRUD API | W6–W7 | 🔴 Blocked by Stage 3 |
| Search & Filter API | W7 | 🔴 Blocked by Stage 3 |
| Firebase Chat Module | W7–W8 | 🔴 Blocked by Stage 3 |
| HomeScreen + ItemDetail | W6–W7 | 🔴 Blocked by Stage 3 |
| Chat UI | W7 | 🔴 Blocked by Stage 3 |
| User Profile screens | W7–W8 | 🔴 Blocked by Stage 3 |

### ⚪ Stage 5: Testing & QA (W8–W9)
```
W1–W7 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  W8 ░░░░░░  W9 ░░░░░░  W10 ░░░░░░░░░░░░
```
### ⚪ Stage 6: Deployment & Final (W9–W10)
```
W1–W8 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  W9 ░░░░░░  W10 ░░░░░░░░░░░░
```

### 🔵 Ongoing: Literature Review (W1–W10)
```
W1 ██  W2 ██  W3 ██  W4 ██  W5 ██  SW1 █  SW2 █  W6–W10 ░░░░░░░░░░░░░░░░░░░░
```

---

## Critical Path Analysis (Week 7)

```
Stage 3           Stage 4              Stage 5       Stage 6
Foundation ──────► Core Features ─────► Testing ────► Deploy
(should be done)   (W6–W8)             (W8–W9)       (W9–W10)
    │
    │  DELAYED
    │
    ▼
  🔴 GAP ─────────► Everything downstream is compressed
```

**If Stage 3 is not complete by end of W7:**
- Stage 4 shrinks from 3 weeks → 2 weeks (W8 only)
- Stage 5 shrinks from 2 weeks → 1 week (W9 only)
- Stage 6 gets 1 week (W10) — no buffer for issues

---

## Recovery Plan

### Scenario A: Stage 3 complete by end of W7 (best case)
- W8: Core features at full velocity
- W9: Testing + bug fixes
- W10: Deployment + report → **On time**

### Scenario B: Stage 3 complete by mid-W8 (tight)
- W8 (2nd half): Core features at maximum velocity
- W9: Core complete + Testing compressed
- W10: Bug fixes + Deployment + Report → **Tight but possible**

### Scenario C: Stage 3 not complete until end of W8 (⚠️ at risk)
- W9: Core features only (skip some)
- W10 (1st half): Testing (minimum)
- W10 (2nd half): Deployment + Report → **MVP scope must be cut**

### Recommended Actions (Scenario A target)
1. **This Wednesday (W7 meeting)**: Confirm all Stage 3 work status
2. **Friday W7 5PM**: Hard deadline for backend scaffold + mobile scaffold in repo
3. **Saturday W7 AM**: PM verifies repo — if no code, escalate to team + instructor
4. **Monday W8**: All hands on Core Features. No new tasks until Foundation is in repo.

---

> **Next Gantt update**: After W7 Sprint Review (Friday)  
> **Prepared by**: Huang Hongrui (PM), 2026-06-24
