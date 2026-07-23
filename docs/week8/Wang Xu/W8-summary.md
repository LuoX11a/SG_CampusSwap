# Wang Xu — Backend Developer Week 8 Summary

> **Role**: Backend Developer | **Week**: 8 (2026-06-29 to 2026-07-05)
> **Status**: ✅ All planned deliverables completed

---

## Completed Deliverables

| # | Deliverable | Status | File(s) |
|---|------------|--------|---------|
| 1 | Item CRUD API (full REST) | ✅ Done | `backend/app/api/v1/items.py` |
| 2 | Search & Filter API | ✅ Done | `backend/app/api/v1/search.py` |
| 3 | Image Upload API (Cloudinary) | ✅ Done | `backend/app/api/v1/upload.py` |
| 4 | User Profile API | ✅ Done | `backend/app/api/v1/users.py` |
| 5 | Reviews API (with rating aggregation) | ✅ Done | `backend/app/api/v1/reviews.py` |
| 6 | Firebase Chat Service | ✅ Done | `backend/app/services/chat_service.py` |
| 7 | Item Business Logic Service | ✅ Done | `backend/app/services/item_service.py` |
| 8 | Cloudinary Upload Service | ✅ Done | `backend/app/services/upload_service.py` |

---

## API Endpoints Implemented

| # | Method | Path | Description |
|---|--------|------|-------------|
| 1 | GET | `/api/v1/items` | List items (paginated, filtered) |
| 2 | POST | `/api/v1/items` | Create listing |
| 3 | GET | `/api/v1/items/{id}` | Item detail + view counter |
| 4 | PUT | `/api/v1/items/{id}` | Update listing (owner only) |
| 5 | DELETE | `/api/v1/items/{id}` | Delete listing (owner only) |
| 6 | PATCH | `/api/v1/items/{id}/status` | Mark as sold/reserved/available |
| 7 | GET | `/api/v1/search` | Full-text search + filters |
| 8 | POST | `/api/v1/upload/image` | Upload single image |
| 9 | POST | `/api/v1/upload/images` | Upload up to 5 images |
| 10 | DELETE | `/api/v1/upload/image` | Delete image |
| 11 | GET | `/api/v1/users/{id}` | Public user profile |
| 12 | PUT | `/api/v1/users/me` | Update own profile |
| 13 | GET | `/api/v1/users/me/listings` | My listings |
| 14 | GET | `/api/v1/users/{id}/listings` | User's public listings |
| 15 | GET | `/api/v1/reviews/user/{id}` | User's reviews |
| 16 | POST | `/api/v1/reviews` | Create review (post-transaction) |
| 17 | GET | `/api/v1/reviews/me` | My received reviews |
| 18 | GET | `/api/v1/reviews/rating-summary/{id}` | Rating distribution chart |

**Total: 18 endpoints** across 5 route modules.

---

## Key Implementation Decisions

| Decision | Rationale |
|----------|-----------|
| Price in cents (INTEGER) | Avoids floating-point rounding issues |
| Soft delete consideration | MVP uses hard delete; v2 will use soft delete |
| Image max 5 per listing | Cloudinary free tier management |
| Chat as separate service | Firebase Firestore provides real-time sync natively |
| Rating recalculation on write | Avoids stale aggregate data |
| Search with ILIKE (not full-text) | Simple for MVP; PostgreSQL full-text search for v2 |
| UUIDs for all PKs | Security + distributed-friendly |

---

## Dependencies Added

```
cloudinary>=1.41.0
firebase-admin>=6.5.0
google-cloud-firestore>=2.16.0
python-multipart>=0.0.9    # For file upload
```

---

## Next Week (W9) Tasks

1. Write unit tests for all endpoints (pytest + httpx)
2. Integration tests (test DB + real API calls)
3. Add input sanitization middleware
4. Performance optimization (N+1 query fixes, pagination tuning)

---

> **All code in** `week8/Wang Xu/backend/`. Ready for integration with frontend by Renxian & Jiahai.
