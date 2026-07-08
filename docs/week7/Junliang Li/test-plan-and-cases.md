# SG CampusSwap — Test Plan & Test Cases

> **QA Lead**: Junliang Li | **Status**: Draft for W7 — cases ready; execution W8–W9  
> **Testing Levels**: Unit → Integration → Usability (3-tier strategy)

---

## 1. Testing Strategy

| Level | Scope | Tool | Owner | When |
|-------|-------|------|-------|------|
| **Unit Tests** | Individual functions, components | Pytest (BE), Jest + RNTL (FE) | Devs | W8 |
| **Integration Tests** | API endpoints + DB, screen flows | Pytest + httpx, Detox/RNTL | Devs + QA | W8–W9 |
| **Usability Testing** | End-to-end user tasks | Manual + observation | QA (Junliang) | W9 |

### Test Environment

| Environment | Details |
|-------------|---------|
| Backend | FastAPI test client, test PostgreSQL instance |
| Mobile (Android) | Expo Go on physical device (Samsung A54) + emulator (Pixel 7 API 34) |
| Mobile (iOS) | Expo Go on iPhone 13 + simulator (iPhone 15, iOS 18) |
| API Testing | Swagger UI + manual curl/Postman |

### Test Data Requirements

- 5 test users (1 per university domain) with verified emails
- 20 test items across all 5 categories
- 5 test chat conversations
- 10 test reviews (mix of ratings 1–5)

---

## 2. Backend Unit Test Cases (Pytest)

### 2.1 Auth Service — `test_auth_service.py`

| ID | Test Case | Input | Expected Output | Priority |
|----|-----------|-------|-----------------|----------|
| UT-A-01 | Register with valid university email | `{email: "test@u.nus.edu", password: "Pass1234", username: "testuser"}` | 201, user created, verification email sent | P0 |
| UT-A-02 | Register with non-university email | `{email: "test@gmail.com", ...}` | 400, "Please use university email" | P0 |
| UT-A-03 | Register with invalid domain (not in whitelist) | `{email: "test@unknown.edu", ...}` | 400, "Domain not in whitelist" | P0 |
| UT-A-04 | Register with duplicate email | Existing email | 409, "Email already registered" | P1 |
| UT-A-05 | Register with weak password (< 8 chars) | `{password: "abc"}` | 422, validation error | P1 |
| UT-A-06 | Register with missing fields | `{}` | 422, field-level errors | P1 |
| UT-A-07 | Verify email with correct code | `{email: "...", code: "123456"}` | 200, `is_verified: true` | P0 |
| UT-A-08 | Verify email with wrong code | `{code: "000000"}` | 400, "Invalid verification code" | P0 |
| UT-A-09 | Verify email with expired code | Code > 10 min old | 400, "Verification code expired" | P1 |
| UT-A-10 | Login with verified account | Valid email + password | 200, `{access_token, refresh_token}` | P0 |
| UT-A-11 | Login with unverified account | Valid email + password, not verified | 403, "Email not verified" | P0 |
| UT-A-12 | Login with wrong password | Valid email + wrong password | 401, "Invalid credentials" | P0 |
| UT-A-13 | Refresh token with valid refresh_token | Valid refresh token | 200, new access + refresh tokens | P1 |
| UT-A-14 | Refresh token with expired token | Expired refresh token | 401 | P1 |
| UT-A-15 | Access protected endpoint without token | No Authorization header | 401, "Not authenticated" | P0 |
| UT-A-16 | Access protected endpoint with invalid token | `Bearer invalid_token` | 401, "Invalid token" | P0 |

### 2.2 Item Service — `test_item_service.py`

| ID | Test Case | Input | Expected | Priority |
|----|-----------|-------|----------|----------|
| UT-I-01 | Create item with valid data | Full item payload | 201, item created with ID | P0 |
| UT-I-02 | Create item without auth | No token | 401 | P0 |
| UT-I-03 | Create item with missing required fields | No title | 422 | P1 |
| UT-I-04 | Create item with invalid price (negative) | `{price: -10}` | 422 | P1 |
| UT-I-05 | Create item with invalid category | `{category: "invalid"}` | 422 | P1 |
| UT-I-06 | Create item with course_code | `{course_code: "CS1010"}` | 201, course_code saved | P1 |
| UT-I-07 | Get item by ID (exists) | Valid item ID | 200, item details | P0 |
| UT-I-08 | Get item by ID (not exists) | Invalid UUID | 404 | P1 |
| UT-I-09 | List items (no filters) | `GET /items?page=1&size=20` | 200, paginated list | P0 |
| UT-I-10 | List items (filter by category) | `?category=textbook` | 200, only textbooks | P1 |
| UT-I-11 | List items (filter by campus) | `?campus=UTown` | 200, only UTown items | P1 |
| UT-I-12 | List items (price range) | `?min_price=10&max_price=100` | 200, items in range | P1 |
| UT-I-13 | List items (search by keyword) | `?q=laptop` | 200, items with "laptop" in title/desc | P0 |
| UT-I-14 | List items (search by course code) | `?q=CS1010` | 200, textbook items with CS1010 | P0 |
| UT-I-15 | List items (pagination page 2) | `?page=2&size=10` | 200, offset items | P2 |
| UT-I-16 | List items (empty result) | `?q=zzz_nonexistent` | 200, `{items: [], total: 0}` | P1 |
| UT-I-17 | Update own item | Valid update payload | 200, item updated | P0 |
| UT-I-18 | Update another user's item | Non-owner JWT | 403 | P0 |
| UT-I-19 | Delete own item | Valid item ID (owner) | 204 | P0 |
| UT-I-20 | Delete another user's item | Non-owner JWT | 403 | P0 |
| UT-I-21 | Mark item as sold | `{status: "sold"}` | 200, status updated | P1 |
| UT-I-22 | Filter by condition | `?condition=like_new` | 200, only like_new items | P1 |
| UT-I-23 | Sort by price ascending | `?sort=price_asc` | 200, cheapest first | P1 |
| UT-I-24 | Sort by newest | `?sort=newest` | 200, most recent first | P1 |

### 2.3 Review Service — `test_review_service.py`

| ID | Test Case | Expected | Priority |
|----|-----------|----------|----------|
| UT-R-01 | Create review after completed transaction | 201 | P0 |
| UT-R-02 | Create review without completed transaction | 400 | P1 |
| UT-R-03 | Create review with rating out of range (0 or 6) | 422 | P1 |
| UT-R-04 | Create duplicate review (same transaction) | 409 | P1 |
| UT-R-05 | Get user reviews | 200, list of reviews | P0 |
| UT-R-06 | User's rating_avg updates after new review | rating_avg recalculated correctly | P0 |

### 2.4 Upload Service — `test_upload_service.py`

| ID | Test Case | Expected | Priority |
|----|-----------|----------|----------|
| UT-U-01 | Upload valid image (< 5 MB, JPEG/PNG) | 200, Cloudinary URL returned | P0 |
| UT-U-02 | Upload file too large (> 5 MB) | 413 | P1 |
| UT-U-03 | Upload unsupported format (GIF, BMP) | 400 | P1 |
| UT-U-04 | Upload without auth | 401 | P0 |

---

## 3. Frontend Component Test Cases (Jest + RNTL)

| ID | Component | Test Case | Expected | Priority |
|----|-----------|-----------|----------|----------|
| FT-01 | ItemCard | Renders title, price, campus, rating | All fields visible | P0 |
| FT-02 | ItemCard | Tap navigates to ItemDetailScreen | Navigation triggered with item ID | P0 |
| FT-03 | ItemCard | Price formatted correctly | "$25.00" for `price: 25` | P1 |
| FT-04 | ItemCard | Rating shows "New" when 0 reviews | "New" badge instead of stars | P2 |
| FT-05 | SearchBar | Typing triggers search | Search callback fired with query | P0 |
| FT-06 | SearchBar | Clear button resets input | Query cleared, callback fires | P1 |
| FT-07 | FilterModal | Apply button fires with filters | Callback with filter object | P0 |
| FT-08 | FilterModal | Reset clears all filters | All chips unselected, sliders reset | P1 |
| FT-09 | FilterModal | Active filter count badge shows | Badge = number of active filters | P1 |
| FT-10 | ChatBubble | Received message left-aligned | Style: `alignSelf: flex-start` | P1 |
| FT-11 | ChatBubble | Sent message right-aligned | Style: `alignSelf: flex-end` | P1 |
| FT-12 | RatingStars | 5 stars rendered | 5 star icons visible | P0 |
| FT-13 | RatingStars | Half-star rendering for 4.5 | 4 full + 1 half star | P1 |
| FT-14 | ImageCarousel | Swipe changes image | Page indicator dot updates | P1 |
| FT-15 | EmptyState | Shows when items array empty | Illustration + message visible | P1 |

---

## 4. Integration Test Cases

### 4.1 API Integration (Pytest + httpx)

| ID | Test Case | Priority |
|----|-----------|----------|
| IT-01 | Full registration flow: register → verify → login → access protected route | P0 |
| IT-02 | Full item lifecycle: create → view → update → mark sold → delete | P0 |
| IT-03 | Search flow: create 10 items → search by keyword → verify results match | P0 |
| IT-04 | Filter flow: create items in different categories/campuses → filter → verify | P1 |
| IT-05 | Transaction + review flow: create item → mark sold → create review → verify rating_avg | P0 |
| IT-06 | Chat flow (Firebase): create chat → send messages → retrieve messages | P0 |
| IT-07 | Image upload + item creation: upload image → get URL → create item with image URL | P0 |
| IT-08 | Pagination: create 25 items → request page 1 (10) → request page 2 (10) → request page 3 (5) | P1 |

### 4.2 Screen Flow Integration (Manual + Detox)

| ID | User Flow | Steps | Expected | Priority |
|----|-----------|-------|----------|----------|
| IF-01 | Registration | LoginScreen → Register → fill form → submit → VerifyEmail → enter code → HomeScreen | Lands on HomeScreen, authenticated | P0 |
| IF-02 | Browse & Search | HomeScreen → scroll → tap SearchBar → type "CS1010" → see results → tap item → ItemDetailScreen | Full browse-to-detail flow | P0 |
| IF-03 | Create Listing | HomeScreen → tap Sell → fill form → add photo → Post → ItemDetailScreen (own item) | Item created, visible in My Listings | P0 |
| IF-04 | Chat Flow | ItemDetailScreen → Chat with Seller → type message → send → message appears | Real-time message delivery | P0 |
| IF-05 | Profile Edit | ProfileScreen → EditProfile → change username → Save → username updated | Profile updated, reflected in UI | P1 |
| IF-06 | Logout/Login | ProfileScreen → Logout → LoginScreen → login → HomeScreen | Session cleared, re-authenticated | P1 |
| IF-07 | Filter Items | SearchScreen → FilterModal → select Textbook + $10-$50 → Apply → filtered results | Only matching items shown | P0 |

---

## 5. Usability Test Cases (W9)

### 5.1 Test Structure

| Item | Detail |
|------|--------|
| **Method** | Moderated, in-person, think-aloud protocol |
| **Participants** | 10–15 Singapore university students (mix of unis, tech comfort 1–5) |
| **Duration** | 20–25 minutes per session |
| **Location** | JCU campus / online via Zoom |
| **Recording** | Screen recording + audio (with consent) |

### 5.2 Participant Screener

- [ ] Currently enrolled in a Singapore university
- [ ] Has bought or sold second-hand goods in the past 12 months (or would consider it)
- [ ] Uses a smartphone daily (iOS or Android)
- [ ] Mix of: tech-savvy (3–5), moderate (2), non-tech-savvy (1) — self-rated
- [ ] Mix of: experienced marketplace users (Carousell, etc.) vs newcomers
- [ ] NOT involved in the SG CampusSwap project

### 5.3 Task Script

| Task ID | Task | Screen(s) | Success Metric | Priority |
|---------|------|-----------|---------------|----------|
| US-01 | **Register an account** using your university email | Register → Verify → Home | Complete registration in ≤ 3 min, 0 errors | P0 |
| US-02 | **Find a textbook** for CS1010 | Home → Search → Results → Detail | Locate and open item detail in ≤ 60s | P0 |
| US-03 | **Filter items** to show only electronics under $100 | Search → Filter → Results | Apply 2+ filters in ≤ 45s | P0 |
| US-04 | **List an item for sale** with photo | Sell → fill form → Post | Complete listing in ≤ 3 min | P0 |
| US-05 | **Contact a seller** about an item | Detail → Chat → send message | Send first message in ≤ 30s | P0 |
| US-06 | **Check your messages** and reply | Chats → ChatScreen → reply | Find and reply to conversation in ≤ 30s | P1 |
| US-07 | **View your profile** and check your rating | Profile → scroll | Find rating and reviews section in ≤ 15s | P1 |
| US-08 | **Edit your profile** to change campus | Profile → Edit → change → Save | Complete edit in ≤ 60s | P1 |

### 5.4 Post-Task Questionnaire (SUS + Custom)

**System Usability Scale (SUS)** — 10 standard questions, 5-point Likert scale.

**Custom questions** (5-point Likert: Strongly Disagree → Strongly Agree):
1. The email verification process was clear and easy to follow.
2. I trust that only real students are on this platform.
3. Finding items near my campus was easy.
4. The chat feature worked as I expected.
5. I would use this app instead of Carousell for campus buying/selling.
6. The course code search helped me find relevant textbooks.

**Open-ended**:
- What was the most confusing part of the app?
- What feature did you wish existed?
- Any other feedback?

### 5.5 Usability Metrics Targets

| Metric | Target |
|--------|--------|
| Task completion rate | ≥ 90% (all tasks) |
| Time on task (first use) | Within 2× expert time |
| SUS score | ≥ 68 (above average) |
| Critical errors (data loss, crash) | 0 |
| Non-critical errors (recoverable) | ≤ 3 per session |
| "Would recommend" (NPS ≥ 8) | ≥ 70% |

---

## 6. Bug Severity Classification

| Severity | Definition | Examples | SLA |
|----------|-----------|----------|-----|
| **P0 — Critical** | Blocks core functionality, no workaround | App crashes on launch, cannot register, cannot login, data loss | Fix within 4 hours |
| **P1 — High** | Major feature broken, workaround exists | Search returns wrong results, chat messages not sending, image upload fails | Fix within 24 hours |
| **P2 — Medium** | Minor feature issue, cosmetic | Misaligned text, wrong color on button, missing loading state | Fix within 1 sprint |
| **P3 — Low** | Visual polish, enhancement | Animation stutter, inconsistent spacing, typo | Backlog, fix if time permits |

---

## 7. Test Execution Schedule

| Week | Activity | Owner |
|------|----------|-------|
| W7 | Write test cases (this document) | Junliang ✅ |
| W8 Mon–Wed | Backend unit tests executed | Bowei + Wang Xu |
| W8 Wed–Fri | Frontend component tests executed | Renxian + Jiahai |
| W8 Fri | Integration tests (API) executed | Wang Xu + Junliang |
| W9 Mon–Tue | Integration tests (screen flows) | Junliang + Jiahai |
| W9 Wed–Thu | Usability testing sessions (10–15 participants) | Junliang |
| W9 Fri | Bug triage + fix prioritisation | All |
| W10 Mon–Tue | Regression testing (critical paths only) | Junliang |

---

## 8. Test Deliverables Checklist

- [x] Test plan document (this file)
- [x] Unit test cases (BE: 50 cases, FE: 15 cases)
- [x] Integration test cases (API: 8, Screen flow: 7)
- [x] Usability test script (8 tasks + SUS + custom questions)
- [ ] Test execution report (after W9)
- [ ] Bug tracking report (after W9)
- [ ] Usability testing report (after W9)

---

> **Test Case Repository**: GitHub Issues (see `github-bug-report-template.md`)  
> **Test Data Script**: `backend/tests/seed_test_data.py` (to be created by Wang Xu)  
> **Next Review**: W8 team meeting — review test execution progress
