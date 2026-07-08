# SG CampusSwap — Week 8 Progress Report

> **Period**: 2026-06-29 to 2026-07-05 (Week 8)
> **Author**: Huang Hongrui (PM)
> **Status**: 🟢 ON TRACK — 27/27 tasks completed

---

## Executive Summary

Week 8 marked a strategic pivot from mobile-first to web-first development, enabled by a Figma Make prototype ("Web-version-request") providing clear design direction. The team achieved 100% of planned Sprint 4 tasks, delivering a fully functional web application with dark sidebar navigation, complete backend API, and Firebase real-time chat.

**Key Achievement**: Web app is feature-complete — all 15+ screens implemented, API endpoints operational, chat working with real-time sync.

---

## Completed Deliverables

### Backend (Bowei + Wang Xu) — 10 tasks ✅

| Deliverable | Details |
|-------------|---------|
| Auth API | Register (domain whitelist), Verify Email (6-digit code), Login (JWT access + refresh tokens) |
| Item CRUD | Full REST: Create, Read (with pagination), Update, Delete, with ownership checks |
| Search & Filter | Keyword search, category filter, price range, condition, campus, sort options |
| Image Upload | Cloudinary integration: upload, resize, delete; max 5 images per item |
| User Profiles | Get/Update profile, avatar upload, university/campus management |
| Reviews | Create review (linked to transaction), rating aggregation, review history |
| Chat Service | Firebase Firestore: create chat, send message, real-time listener |
| Database Migrations | Alembic: initial schema + all enum types + indexes |
| API Docs | Swagger UI auto-generated at `/docs` |
| Docker Setup | Dockerfile + docker-compose (FastAPI + PostgreSQL) |

### Frontend — Web (Renxian + Jiahai) — 16 tasks ✅

| Deliverable | Details |
|-------------|---------|
| Project Scaffold | Next.js 14 App Router, TypeScript strict, Tailwind CSS |
| Sidebar Navigation | Dark (#111827) sidebar, 6 nav items with icons, active state |
| API Client | Axios instance with JWT interceptor, auto-refresh, error handling |
| State Management | 4 Zustand stores: auth, items, filter, chat |
| Home Page | Grid layout (1-4 cols responsive), search bar, category chips, infinite scroll |
| ItemDetail Page | Image carousel, seller info card, meetup point, "Chat with Seller" CTA |
| CreateListing Page | Image picker (5 max), form validation, Cloudinary upload |
| Auth Pages | Login, Register (with domain hint), Email Verification (6-digit OTP) |
| SearchResults Page | Real-time search, filter modal with chips + range slider + sort |
| ChatList Page | Real-time (Firebase), unread dots, last message preview |
| ChatRoom Page | Message bubbles, auto-scroll, image attachment, typing indicator |
| Profile Page | Avatar, stats, active listings, quick links |
| EditProfile Page | Username, university/campus dropdown, avatar change |
| Settings Page | Notification toggles, account management, app version |
| Reviews Page | Rating summary bar chart, review cards with item reference |
| MyListings Page | Active/sold tabs, edit/delete actions, status badges |

### PM & Design (Hongrui + Junliang) — 5 tasks ✅

| Deliverable | Details |
|-------------|---------|
| Sprint Backlog Update | Reflecting web-first strategy, Sprint 4 task list |
| W8 Meeting Agenda | Full agenda with 7 discussion items |
| W8 Progress Report | This document |
| Web Design Specs | Dark sidebar design system, component specs, color tokens |
| Updated Test Cases | 80 cases adapted for web (from mobile) |

---

## Metrics

| Metric | Value |
|--------|-------|
| Sprint 4 tasks completed | 27 / 27 (100%) |
| API endpoints implemented | 22 |
| Frontend pages/screens | 16 |
| Lines of backend code | ~3,200 |
| Lines of frontend code | ~5,800 |
| TypeScript interfaces | 11 |
| Database tables | 6 |
| Zustand stores | 4 |

---

## Risks Update

| Risk | Previous | Current | Trend |
|------|----------|---------|-------|
| Timeline delay | HIGH | MEDIUM | ↓ Web dev faster than RN |
| Cloud account setup | HIGH | LOW | ↓ All accounts created |
| Firebase chat complexity | MEDIUM | LOW | ↓ Simpler than expected |
| Mobile app timing | — | HIGH | 🆕 Compressed timeline |

---

## Next Week (W9) Plan

1. Deploy backend to AWS EC2 (Bowei)
2. Deploy frontend to Vercel (Renxian)
3. Begin testing: backend unit tests + frontend component tests
4. Integration testing (end-to-end flows)
5. Bug fixes based on test results
6. Prepare for W10 final delivery

---

> **Conclusion**: Week 8 was highly productive. The strategic pivot to web-first has paid off with faster-than-expected development velocity. The team is on track for W10 final delivery.
