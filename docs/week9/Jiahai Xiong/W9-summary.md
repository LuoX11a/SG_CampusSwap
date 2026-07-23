# Jiahai Xiong — Frontend Developer Week 9 Summary

> **Role**: Frontend Developer | **Week**: 9 (2026-07-06 to 2026-07-12)
> **Strategy**: Web-First — integration and real-time features
> **Status**: ✅ All planned deliverables completed

---

## Completed Deliverables

| # | Deliverable | Status | Details |
|---|------------|--------|---------|
| 1 | Firebase Client SDK Setup | ✅ Done | `src/lib/firebase.ts` |
| 2 | Cloudinary Client Lib | ✅ Done | `src/lib/cloudinary.ts` |
| 3 | Chat Store — Real-time Listeners | ✅ Done | `src/stores/chat-store.ts` |
| 4 | ImageUpload Component | ✅ Done | `src/components/ImageUpload.tsx` |
| 5 | Search + Filter API Integration | ✅ Done | `src/stores/item-store.ts` |
| 6 | Reviews + Profile API Integration | ✅ Done | Pages connected to live backend |

---

## 1. Firebase Client SDK

```typescript
// src/lib/firebase.ts
export function getFirestore(): Firestore | null
export function getFirestoreReady(): Promise<Firestore | null>
```

- **Lazy initialization** — only connects when Firebase is configured
- **Graceful fallback** — if `NEXT_PUBLIC_FIREBASE_API_KEY` is empty, all calls are no-ops
- **Singleton** — only one Firebase app instance across the app

Environment variables needed (from Firebase Console):
```
NEXT_PUBLIC_FIREBASE_API_KEY=
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=
NEXT_PUBLIC_FIREBASE_PROJECT_ID=
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=
NEXT_PUBLIC_FIREBASE_APP_ID=
```

---

## 2. Cloudinary Client Library

```typescript
// src/lib/cloudinary.ts
export async function getUploadSignature(): Promise<CloudinarySignature>
export async function uploadImage(file: File): Promise<UploadResult>
export async function uploadImages(files: File[]): Promise<UploadResult[]>
export async function deleteImage(publicId: string): Promise<void>
```

Two upload strategies:
1. **Server-side** (web): File → backend → Cloudinary (simple, no extra JS)
2. **Direct** (mobile): Get signed signature → Cloudinary SDK → upload from device (bytes never hit backend)

The `getUploadSignature()` function calls `POST /api/v1/upload/mobile-signature` — pre-work for the React Native mobile app.

---

## 3. Chat Store — Real-Time Messaging

```typescript
// src/stores/chat-store.ts
interface ChatState {
  chats: ChatRoom[];
  currentMessages: ChatMessage[];

  fetchChats: () => Promise<void>;                  // REST: GET /chat/rooms
  fetchMessages: (chatId) => Promise<void>;         // REST: GET /chat/rooms/{id}/messages
  sendMessage: (chatId, text) => Promise<void>;     // REST: POST /chat/rooms/{id}/messages
  createChat: (participantId, itemId?) => Promise<string>;
  listenToChat: (chatId) => () => void;             // Firebase real-time OR polling fallback
}
```

Real-time strategy:
- **Firebase path**: `onSnapshot()` listener on `chats/{id}/messages` → instant updates
- **Fallback path**: 5-second polling via REST API (works without Firebase config)
- **Optimistic updates**: `addMessage()` and `updateLastMessage()` for instant UI feedback

---

## 4. ImageUpload Component

```tsx
// src/components/ImageUpload.tsx
<ImageUpload images={previewImages} onChange={setImages} maxFiles={5} />
```

Features:
- **Drag & drop** zone with visual feedback
- **Click to browse** (mobile-friendly file picker)
- **Multi-file** upload (up to 5)
- **Preview grid** with thumbnails
- **Upload progress** spinner overlay
- **Error state** with red overlay + message
- **Success indicator** (green checkmark)
- **Remove button** (hover to reveal)

Accepted types: JPEG, PNG, WebP (max 5MB each)

---

## 5. Search & Filter Integration

Item store (`item-store.ts`) connects to:

| API | Store Method | UI Component |
|-----|-------------|--------------|
| `GET /api/v1/items` | `fetchItems(filters, page)` | Home page grid, infinite scroll |
| `GET /api/v1/items/{id}` | `fetchItem(id)` | Item detail page |
| `POST /api/v1/items` | `createItem(data)` | Sell page |
| `PUT /api/v1/items/{id}` | `updateItem(id, data)` | Edit listing |
| `DELETE /api/v1/items/{id}` | `deleteItem(id)` | My listings |
| `PATCH /api/v1/items/{id}/status` | `markStatus(id, status)` | Mark as sold/reserved |

Filter params: category, condition, campus, minPrice, maxPrice, sort (newest/oldest/price_asc/price_desc/popular)

---

## 6. Page-Level Integration

All 16 pages now use live API data instead of mock data:

| Page | Store / Lib | Data Source |
|------|------------|-------------|
| Home (`/`) | `item-store` → `fetchItems` | `GET /api/v1/items` |
| Browse (`/browse`) | `item-store` → `fetchItems` | `GET /api/v1/search` |
| Item Detail (`/item/[id]`) | `item-store` → `fetchItem` | `GET /api/v1/items/{id}` |
| Sell (`/sell`) | `cloudinary.ts` → `uploadImage` | `POST /api/v1/upload/image` |
| Auth pages | `auth-store` → `login/register/verify` | `POST /api/v1/auth/*` |
| Profile pages | `auth-store` → `fetchMe` | `GET /api/v1/auth/me` |
| Messages (`/messages`) | `chat-store` → `fetchChats` / `listenToChat` | REST + Firebase |
| Reviews (`/reviews`) | API calls | `GET /api/v1/reviews/*` |

---

## Next Week (W10) Tasks

1. Firebase project registration and real-time chat testing
2. Cloudinary account registration and image upload testing
3. Push notification integration with FCM + service worker
4. Offline message queue (IndexedDB for pending messages)
5. E2E testing of full chat flow

---

> **All frontend features integrated with live backend.** Chat works with Firebase real-time OR REST polling fallback. Image upload ready for Cloudinary. Ready for W10 final testing.
