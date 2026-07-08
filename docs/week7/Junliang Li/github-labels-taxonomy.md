# SG CampusSwap — GitHub Labels Taxonomy

> **Owner**: Junliang Li (QA) | **Setup by**: W7 Wednesday meeting  
> **Apply to**: GitHub Issues and Pull Requests

---

## Label Categories

### Type (what kind of work is this?)

| Label | Color | Description |
|-------|-------|-------------|
| `bug` | `#D73A4A` 🔴 | Something isn't working |
| `enhancement` | `#A2EEEF` 🔵 | New feature or improvement |
| `documentation` | `#0075CA` 🔷 | Documentation changes |
| `question` | `#D876E3` 🟣 | Discussion or question |

### Priority (how urgent?)

| Label | Color | Description |
|-------|-------|-------------|
| `priority: critical` | `#B60205` 🔴 | Must fix immediately (P0) |
| `priority: high` | `#FF6F00` 🟠 | Must fix this sprint (P1) |
| `priority: medium` | `#FBCA04` 🟡 | Should fix (P2) |
| `priority: low` | `#0E8A16` 🟢 | Nice to have (P3) |

### Status (where is this in the workflow?)

| Label | Color | Description |
|-------|-------|-------------|
| `status: needs-triage` | `#B60205` 🔴 | New, not yet reviewed |
| `status: confirmed` | `#0E8A16` 🟢 | Reproduced and confirmed |
| `status: in-progress` | `#FBCA04` 🟡 | Someone is working on it |
| `status: blocked` | `#D93F0B` 🟠 | Blocked by another issue |
| `status: ready-for-review` | `#1D76DB` 🔵 | PR open, awaiting review |
| `status: wont-fix` | `#CCCCCC` ⚪ | Decided not to fix |

### Component (which part of the app?)

| Label | Color | Description |
|-------|-------|-------------|
| `component: auth` | `#C5DEF5` | Login, register, email verification |
| `component: items` | `#C5DEF5` | Item listing, detail, CRUD |
| `component: search` | `#C5DEF5` | Search, filter, sort |
| `component: chat` | `#D4C5F9` | Chat list, chat screen, Firebase |
| `component: profile` | `#C5DEF5` | User profile, edit profile, reviews |
| `component: upload` | `#D4C5F9` | Image upload, Cloudinary |
| `component: navigation` | `#C5DEF5` | Tab navigator, stack navigator |
| `component: ui` | `#F9D0C4` | Design, styling, layout |

### Layer (which part of the stack?)

| Label | Color | Description |
|-------|-------|-------------|
| `backend` | `#006B75` | FastAPI, database, API |
| `frontend` | `#2B67C6` | React Native, Expo, screens |
| `devops` | `#E99695` | CI/CD, AWS, deployment |
| `design` | `#FB82B4` | Figma, UI/UX, mockups |
| `qa` | `#5319E7` | Testing, bug tracking |

### Sprint

| Label | Color | Description |
|-------|-------|-------------|
| `sprint: current` | `#0E8A16` | Planned for current sprint |
| `sprint: next` | `#1D76DB` | Planned for next sprint |
| `sprint: backlog` | `#CCCCCC` | Future, not yet scheduled |

---

## Quick Reference: Issue Label Combinations

| Issue Type | Labels |
|------------|--------|
| Critical production bug | `bug` + `priority: critical` + `status: needs-triage` + component |
| UI visual bug | `bug` + `priority: medium` + `component: ui` + `frontend` |
| New feature for future | `enhancement` + `priority: low` + `sprint: backlog` |
| Feature for this sprint | `enhancement` + `priority: high` + `sprint: current` |
| Backend API change | `enhancement` + `backend` + component + priority |
| Test failure | `bug` + `qa` + `priority: high` |
| Documentation update | `documentation` + priority |
| Deployment issue | `bug` + `devops` + `priority: critical` |

---

## Setup Instructions (GitHub)

1. Go to: https://github.com/LuoX11a/SG_CampusSwap/issues/labels
2. Create each label with the name, color, and description from the tables above
3. Set up Issue Templates: copy `bug-report.md` and `feature-request.md` to `.github/ISSUE_TEMPLATE/`
4. Enable Issues in repo Settings → General → Features

---

> **Labels to create**: 28 labels total  
> **Maintenance**: Review labels each sprint retrospective — archive unused, add as needed
