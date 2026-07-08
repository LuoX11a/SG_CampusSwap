# SG CampusSwap — Risk Register (Updated Week 7)

> **Last Updated**: 2026-06-24 (Week 7) | **Owner**: Huang Hongrui (PM)  
> **Review Cadence**: Every Wednesday team meeting

---

## Active Risks

### 🔴 CRITICAL: Zero Code in Repository (NEW)
| Field | Detail |
|-------|--------|
| **Identified** | Week 7 |
| **Likelihood** | Certain (already happened) |
| **Impact** | Critical — 4 weeks to W10 delivery |
| **Description** | GitHub repo (`LuoX11a/SG_CampusSwap`) has only `master` branch with a single `README.md` commit. No `develop` branch, no `feature/*` branches, no backend or mobile code. Stage 3 (Foundation Development, W5–W6) has produced zero code commits. |
| **Root Cause** | Study break momentum loss; task ownership gaps; no branch protection or CI enforcement |
| **Mitigation** | 1. **Immediately** create `develop` branch from `master`. 2. Bowei pushes FastAPI scaffold + Auth module by end of W7. 3. Renxian pushes Expo project scaffold + basic navigation by end of W7. 4. Daily code commits required — PM checks repo each morning. |
| **Fallback** | Reduce MVP scope: drop push notifications, simplify chat (no real-time indicators), limit to 3 categories |

### 🟡 HIGH: Week 7 Presentation Consuming Dev Time (UPDATED)
| Field | Detail |
|-------|--------|
| **Identified** | Week 5 |
| **Likelihood** | High |
| **Impact** | Medium — 1–2 days lost to slide prep + rehearsal |
| **Description** | A second in-class presentation is due in Week 7. Team members diverted from coding to prepare slides. |
| **Mitigation** | Reuse W5 presentation as base, add only progress updates. PM drafts slides; team reviews async. Max 2 hours per member on prep. |
| **Fallback** | One speaker presents on behalf of entire team |

### 🟡 HIGH: Firebase Chat Complexity (ORIGINAL)
| Field | Detail |
|-------|--------|
| **Identified** | Week 3 (design phase) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Description** | Firebase Firestore real-time chat is the most technically complex feature. If not started by W7, it will not be ready for W8 testing. |
| **Mitigation** | Wang Xu (BE) + Jiahai (FE) pair on chat module. Start with minimal viable chat (send/receive text only), defer typing indicators and read receipts to post-MVP. |
| **Fallback** | Ship without real-time indicators; use polling-based message refresh |

### 🟡 HIGH: App Not Completed on Time (ORIGINAL)
| Field | Detail |
|-------|--------|
| **Identified** | Week 1 |
| **Likelihood** | Medium → **Elevated** (due to code gap) |
| **Impact** | High |
| **Description** | MVP features may not all be complete by W10 submission deadline. |
| **Mitigation** | MVP-first prioritisation. Feature freeze after W4 already in effect. Weekly progress review. PM to maintain burn-down chart from W7 onward. |
| **Fallback** | Demo-able subset: auth + item listing + search + basic profile; defer chat if necessary |

---

## 🟢 MONITORING (under control)

| Risk | Likelihood | Impact | Current Status |
|------|-----------|--------|---------------|
| Team member illness/withdrawal | M | H | All 6 members active. Cross-training notes in progress. |
| Low user testing participation | L | M | Junliang to recruit testers by W8; 10–15 target, 5 minimum. |
| App store rejection | L | M | Fallback: direct APK download + QR code. No dependency on store approval. |
| PDPA compliance | L | H | Storing only university email + username. No NRIC, no address. |
| Scope creep | M | M | Feature freeze W4 enforced. New ideas go to Future Version backlog on GitHub Issues. |
| AWS free tier limits exceeded | L | M | EC2 t2.micro within 750 hrs/month. CloudWatch billing alarm set (if deployed). |
| Neon free tier exceeded | L | L | 1 GB cap. Clean up test data periodically. |

---

## Risk Burn-Down Summary

| Date | Critical | High | Medium | Low |
|------|----------|------|--------|-----|
| W3 (Plan) | 0 | 2 | 4 | 2 |
| **W7 (Now)** | **1** | **3** | **3** | **1** |

> **Trend**: Risk level has increased since W3 baseline. The code gap is the primary driver. If resolved by end of W7, risk profile returns to baseline.

---

## Next Risk Review
- **When**: Wednesday W8 team meeting (11:00 AM)
- **Agenda**: Verify code gap closed, re-assess Firebase and schedule risks
