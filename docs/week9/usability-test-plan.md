# SG CampusSwap — Usability Testing Plan

> **QA Lead**: Junliang Li | **Date**: 2026-07-12 (Week 9)
> **Execution**: W10 Wed-Fri (2026-07-15 to 2026-07-17)

---

## 1. Objectives

Evaluate the SG CampusSwap web application with real university students to:
1. Identify usability issues before final delivery
2. Measure task completion rates for 5 core flows
3. Collect subjective satisfaction scores (SUS + NPS)
4. Prioritize fixes for v2 roadmap

---

## 2. Participant Recruitment

| Criteria | Details |
|----------|---------|
| Target count | 10-15 students |
| Demographics | University students (NUS, NTU, SMU, SUTD, SUSS, SIT) |
| Tech comfort | Mix of tech-savvy and non-tech-savvy |
| Recruitment channels | WhatsApp class groups, campus posters, personal network |
| Incentive | $10 GrabFood voucher per participant |
| Session duration | 30 minutes per participant |

---

## 3. Test Environment

- **Device**: Participant's own laptop/desktop (real-world usage)
- **Browser**: Any modern browser (Chrome, Safari, Firefox, Edge)
- **Network**: Participant's own WiFi (real-world conditions)
- **Recording**: Screen recording via Zoom (with consent)
- **Moderator**: Junliang Li (QA Lead)

---

## 4. Test Tasks (5 Core Flows)

### Task 1: Register & Verify Email
```
Scenario: You're a new NTU student who wants to buy second-hand textbooks.
Task: Create an account and verify your email.
Steps:
  1. Go to the homepage
  2. Click "Sign Up" / navigate to Register
  3. Fill in your details (use provided test email)
  4. Submit the form
  5. Enter the verification code
Expected: Account created, redirected to home page, sidebar visible.
Success criteria: User completes all steps without moderator help.
```

### Task 2: Browse & Search for an Item
```
Scenario: You need a CS1010 textbook for next semester.
Task: Find a CS1010 textbook listed for under $50.
Steps:
  1. From the home page, locate the search bar
  2. Type "CS1010" and press Enter
  3. Use the price filter to set max $50
  4. Browse results and find a suitable listing
Expected: Filtered search results showing CS1010 textbooks under $50.
Success criteria: User applies at least one filter and identifies a relevant result.
```

### Task 3: Create a Listing
```
Scenario: You want to sell your used calculator.
Task: Create a new listing with photos.
Steps:
  1. Click "Sell" in the sidebar
  2. Fill in title, description, category, price, condition
  3. Upload at least 1 photo
  4. Set campus location and meetup point
  5. Submit the listing
Expected: Listing created, redirected to item detail page.
Success criteria: Task completed in ≤ 3 minutes without errors.
```

### Task 4: Chat with a Seller
```
Scenario: You want to ask the seller a question about the CS1010 textbook.
Task: Start a conversation with the seller.
Steps:
  1. Open the CS1010 textbook listing you found earlier
  2. Click "Chat with Seller"
  3. Type a message: "Hi, is this the latest edition?"
  4. Send the message
Expected: Chat opens, message sent, message appears on screen.
Success criteria: Message appears in chat without page refresh.
```

### Task 5: Check Seller Reputation
```
Scenario: Before buying, you want to check if the seller is reliable.
Task: View the seller's profile and reviews.
Steps:
  1. From the item detail page, click the seller's avatar/name
  2. View their profile page (stats, active listings)
  3. Check their rating and reviews
Expected: Profile page shows rating average, review count, and active listings.
Success criteria: User can locate and interpret the seller's rating.
```

---

## 5. Metrics & Measurement

| Metric | Target | How Measured |
|--------|--------|-------------|
| Task 1 completion rate | ≥ 80% | Observer checklist |
| Task 2 completion rate | ≥ 90% | Observer checklist |
| Task 3 completion rate | ≥ 70% | Observer checklist |
| Task 4 completion rate | ≥ 85% | Observer checklist |
| Task 5 completion rate | ≥ 85% | Observer checklist |
| Task 3 time-on-task | ≤ 3 min | Stopwatch |
| SUS score | ≥ 68 (above average) | Post-test questionnaire |
| NPS | ≥ 30 | "How likely to recommend?" (0-10) |

---

## 6. Post-Test Questionnaire

### System Usability Scale (SUS) — 10 items
1. I think I would like to use SG CampusSwap frequently.
2. I found SG CampusSwap unnecessarily complex.
3. I thought SG CampusSwap was easy to use.
4. I think I would need technical support to use SG CampusSwap.
5. I found the various functions were well integrated.
6. I thought there was too much inconsistency.
7. I imagine most people would learn to use SG CampusSwap quickly.
8. I found SG CampusSwap very cumbersome to use.
9. I felt very confident using SG CampusSwap.
10. I needed to learn a lot before I could get going.

(5-point Likert scale: Strongly Disagree → Strongly Agree)

### Open-Ended Questions
- What was the hardest part of using SG CampusSwap?
- What feature did you find most useful?
- What would you change or add?
- Would you use this app instead of Carousell for campus items? Why/why not?

---

## 7. Data Analysis Plan

1. **Quantitative**: Calculate completion rates, SUS scores, NPS, task times
2. **Qualitative**: Thematic analysis of open-ended responses
3. **Severity rating** for each finding:
   - **Critical**: Prevents task completion
   - **High**: Causes significant delay or confusion
   - **Medium**: Minor annoyance, workaround available
   - **Low**: Cosmetic or preference

---

## 8. Schedule

| Day | Activity |
|-----|----------|
| W10 Mon | Finalize test script, prepare test accounts |
| W10 Tue | Dry run with 1 team member |
| W10 Wed | Test sessions: 5 participants (30 min each) |
| W10 Thu | Test sessions: 5 participants (30 min each) |
| W10 Fri AM | Test sessions: 5 participants (30 min each) |
| W10 Fri PM | Compile report, present findings to team |

---

> **Deliverable**: Usability Test Report with findings, severity ratings, and prioritized fix recommendations (W10 Fri).
