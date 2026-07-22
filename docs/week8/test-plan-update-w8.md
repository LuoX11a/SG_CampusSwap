# SG CampusSwap — Updated Test Plan (Web Adaptation, Week 8)

> **QA Lead**: Junliang Li | **Updated**: 2026-07-04
> **Original**: 80 test cases (mobile) → **Updated**: 85 test cases (web)

---

## Changes from Mobile to Web

| Aspect | Mobile (W7) | Web (W8) |
|--------|-------------|----------|
| Navigation | Bottom Tabs (5) | Sidebar (5 items) |
| Layout | Single column | Multi-column Grid (1–4 cols) |
| Auth pages | Full-screen | Centered card (auth pages hide sidebar) |
| Filter | Full-screen modal | Side panel / modal |
| Chat | Full-screen | Three-panel (sidebar + list + conversation) |
| Image picker | Camera/gallery native | File input + drag & drop |
| Touch targets | 48px min | 40px min (mouse-friendly) |
| Responsive | 375–812px fixed | 320px – 1440px+ fluid |

---

## Test Cases (Updated)

### AUTH (9 cases)

| ID | Test | Type | Steps | Expected |
|----|------|------|-------|----------|
| A01 | Login with valid credentials | E2E | Enter email + password → click Login | Redirect to Home, sidebar + grid visible |
| A02 | Login with invalid password | Unit | Enter wrong password | Inline error: "Invalid email or password" |
| A03 | Login with non-edu email | Unit | Enter gmail.com email | Domain hint: "Please use university email" |
| A04 | Register with valid .edu email | E2E | Fill all fields → Register | Redirect to Verify Email screen |
| A05 | Register with weak password | Unit | "abc123" | Error: "Password must be ≥8 chars with 1 uppercase + 1 digit" |
| A06 | Register with mismatched passwords | Unit | Different confirm password | Error: "Passwords do not match" |
| A07 | Verify email with correct code | E2E | Enter 6-digit code → auto-submit | Toast "Email verified" → redirect to Home |
| A08 | Verify email with wrong code | Unit | Enter wrong code | Shake animation + "Invalid code" |
| A09 | Resend verification code | Unit | Click "Resend" → wait 30s | Cooldown timer, button disabled for 30s |

### HOME / LISTING (12 cases)

| ID | Test | Type | Steps | Expected |
|----|------|------|-------|----------|
| H01 | Home page loads items | Integration | Visit / | Grid of item cards visible, sidebar present |
| H02 | Infinite scroll | E2E | Scroll to bottom | Next page loads, URL updates `?page=2` |
| H03 | Empty state | Unit | Visit with 0 items | "No items yet. Be the first to sell!" + CTA |
| H04 | Category chip filter | E2E | Click "Textbooks" chip | Grid updates, chip highlighted blue, URL `?category=textbook` |
| H05 | Clear category filter | E2E | Click active chip again | Grid shows all, chip unselected |
| H06 | Search by keyword | Integration | Type "CS1010" in search bar | Results filtered, debounced 300ms |
| H07 | Item card skeleton loading | Unit | Slow network (throttle) | 8 skeleton cards pulse, then replaced by content |
| H08 | Pull-to-refresh | Unit | Click refresh button | Loading spinner → grid reloads |
| H09 | Error state — API down | Unit | Kill backend | Error message + "Retry" button |
| H10 | Responsive grid: desktop | UI | Viewport > 1280px | 4 columns |
| H11 | Responsive grid: tablet | UI | Viewport 768–1024px | 2 columns |
| H12 | Responsive sidebar: mobile | UI | Viewport < 768px | Hamburger menu, sidebar as drawer |

### ITEM DETAIL (8 cases)

| ID | Test | Type | Steps | Expected |
|----|------|------|-------|----------|
| D01 | View item detail | E2E | Click item card | Image carousel + title + price + seller info + CTA |
| D02 | Image carousel swipe | UI | Click arrow / swipe | Next/prev image, dots update |
| D03 | Image fullscreen | UI | Click image | Lightbox overlay, click outside to close |
| D04 | Seller info card | UI | Scroll to seller section | Avatar + name + university + rating |
| D05 | Navigate to seller profile | E2E | Click seller avatar | `/profile/[id]` page loads |
| D06 | Chat with seller CTA | E2E | Click "Chat with Seller" | Opens chat room with pre-populated item info |
| D07 | Meetup point map link | UI | Click meetup point | Opens Google Maps in new tab |
| D08 | Owner actions (Edit/Delete) | E2E | View own listing | "..." menu shows Edit + Delete options |

### CREATE LISTING (8 cases)

| ID | Test | Type | Steps | Expected |
|----|------|------|-------|----------|
| C01 | Create listing with all fields | E2E | Fill form → Post | Toast "Listed!" → redirect to ItemDetail |
| C02 | Image upload (drag & drop) | UI | Drag image onto dropzone | Preview appears, upload progress bar |
| C03 | Image upload (file picker) | UI | Click "Add Photos" → select file | Same as above |
| C04 | Max 5 images | Unit | Try to add 6th image | Error: "Maximum 5 photos" |
| C05 | Required field validation | Unit | Submit empty form | Inline errors on: title, category, price, condition |
| C06 | Price validation | Unit | Enter negative price | Error: "Price must be positive" |
| C07 | Image size validation | Unit | Upload 20MB image | Error: "Image must be under 5MB" |
| C08 | Submit button disabled until valid | UI | Watch button state | Grayed out until ≥1 photo + title + category + price + condition |

### SEARCH & FILTER (7 cases)

| ID | Test | Type | Steps | Expected |
|----|------|------|-------|----------|
| F01 | Search results page | E2E | Search "laptop" → view results | Results grid with count "Results for 'laptop' (5)" |
| F02 | Price range filter | Integration | Set slider to $10–$50 | Results update, only items in range |
| F03 | Condition filter | Integration | Select "Like New" + "Good" | Multi-select chips, results update |
| F04 | Campus filter | Integration | Select "NUS" | Only NUS items shown |
| F05 | Sort: Price Low→High | Integration | Select sort option | Results reorder ascending by price |
| F06 | Sort: Newest First | Integration | Select sort option | Results reorder by created_at DESC |
| F07 | Reset filters | UI | Click "Reset" | All filters cleared, full results restored |

### CHAT (10 cases)

| ID | Test | Type | Steps | Expected |
|----|------|------|-------|----------|
| CH01 | Chat list loads | Integration | Visit /messages | List of conversations, sorted by last message time |
| CH02 | Unread indicator | UI | Have unread message | Blue dot on conversation row |
| CH03 | Empty chat list | Unit | No conversations | "No messages yet" + "Browse items to start chatting" |
| CH04 | Open chat room | E2E | Click conversation | Messages load, auto-scroll to bottom |
| CH05 | Send text message | E2E | Type message → Enter | Message appears instantly (optimistic), bubble right-aligned |
| CH06 | Receive message (real-time) | Integration | Another user sends message | Appears in real-time without refresh |
| CH07 | Image attachment | UI | Click 📎 → select image | Image preview in chat bubble |
| CH08 | Item reference card | UI | View chat from item detail | Item info card above messages |
| CH09 | Typing indicator | Integration | Other user types | "..." indicator at bottom |
| CH10 | Chat list auto-update | Integration | Receive message while on list | Conversation moves to top, last message updates |

### PROFILE & SETTINGS (10 cases)

| ID | Test | Type | Steps | Expected |
|----|------|------|-------|----------|
| P01 | View own profile | E2E | Sidebar user → click | Avatar, stats, active listings, quick links |
| P02 | Edit profile | E2E | "Edit" → change username → Save | Toast "Profile updated" |
| P03 | Change avatar | UI | Click avatar → select image | Cropper → upload → avatar updates |
| P04 | View public profile | E2E | Click seller avatar on item | Public profile with reviews + listings |
| P05 | My Listings tab | E2E | Sidebar → My Listings | Grid with Active + Sold tabs |
| P06 | Delete listing | E2E | "..." → Delete → confirm | Listing removed, toast "Listing deleted" |
| P07 | Mark as sold | E2E | "..." → Mark as Sold | Status badge changes to "SOLD" |
| P08 | Notification toggles | UI | Settings → toggle Push off | Toggle changes, preference saved |
| P09 | Logout | E2E | Settings → Log Out → confirm | JWT cleared, redirect to Login |
| P10 | Delete account | UI | Settings → Delete Account → confirm | Account deleted, redirect to Register |

### REVIEWS (7 cases)

| ID | Test | Type | Steps | Expected |
|----|------|------|-------|----------|
| RV01 | View reviews | E2E | Profile → My Reviews | Rating summary bar chart + review cards |
| RV02 | Create review | E2E | After transaction → "Write Review" | Star rating + comment form |
| RV03 | Rating star interaction | UI | Hover over stars | Stars fill up to hovered position |
| RV04 | Submit review | E2E | Select 5★ + write comment → Submit | Toast "Review submitted" |
| RV05 | Rating summary update | Integration | New review submitted | Bar chart recalculates, average updates |
| RV06 | Cannot review without transaction | Unit | Try to review random user | Error: "You can only review users you've transacted with" |
| RV07 | One review per transaction | Unit | Try to review same transaction twice | Error: "You've already reviewed this transaction" |

### EDGE CASES & ACCESSIBILITY (14 cases)

| ID | Test | Type | Steps | Expected |
|----|------|------|-------|----------|
| E01 | Expired JWT token | Integration | Wait 30 min → navigate | Auto-refresh or redirect to login |
| E02 | Concurrent editing | Unit | Two tabs edit same listing | Second save shows "Item was modified" warning |
| E03 | XSS in item title | Security | Create item with `<script>alert(1)</script>` | Escaped as text, not executed |
| E04 | SQL injection in search | Security | Search `'; DROP TABLE items;--` | No effect, parameterized queries |
| E05 | Large image upload | Unit | Upload 50MB file | Rejected client-side AND server-side |
| E06 | Network offline | UI | Disconnect → navigate | Offline indicator, queued actions |
| E07 | Keyboard navigation | A11y | Tab through all elements | Logical tab order, visible focus rings |
| E08 | Screen reader: item card | A11y | VoiceOver/NVDA on card | Reads: "CS1010 Textbook, $25, 4.5 stars, 12 reviews" |
| E09 | Color contrast | A11y | Audit with axe DevTools | All text ≥ 4.5:1 contrast ratio |
| E10 | Browser back button | UI | Navigate deep → press Back | Correct previous page, scroll position restored |
| E11 | Deep link to item | Integration | Direct URL `/item/[id]` | Item loads correctly (SSR or CSR) |
| E12 | 404 page | UI | Visit `/nonexistent` | "Page not found" + link to Home |
| E13 | Rate limiting | Security | 10 login attempts in 1 min | "Too many attempts. Try again in 5 minutes." |
| E14 | Session persistence | Integration | Close tab → reopen | Still logged in (JWT in localStorage/httpOnly cookie) |

---

## Test Summary

| Category | Count |
|----------|-------|
| Auth | 9 |
| Home / Listing | 12 |
| Item Detail | 8 |
| Create Listing | 8 |
| Search & Filter | 7 |
| Chat | 10 |
| Profile & Settings | 10 |
| Reviews | 7 |
| Edge Cases & A11y | 14 |
| **Total** | **85** |

---

> **Test execution**: Starts W9. Priority: E2E > Integration > Unit > UI > A11y.
> **Tools**: Jest (unit), React Testing Library (component), Cypress (E2E), axe (a11y).
