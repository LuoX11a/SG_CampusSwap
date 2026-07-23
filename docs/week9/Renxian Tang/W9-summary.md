# Renxian Tang — Frontend Lead Week 9 Summary

> **Role**: Frontend Lead | **Week**: 9 (2026-07-06 to 2026-07-12)
> **Strategy**: Web-First (Next.js 14) with PWA for mobile pre-work
> **Status**: ✅ All planned deliverables completed

---

## Completed Deliverables

| # | Deliverable | Status | Details |
|---|------------|--------|---------|
| 1 | PWA Setup (manifest + service worker) | ✅ Done | Installable on mobile home screen |
| 2 | Service Worker (offline + push) | ✅ Done | `public/sw.js` |
| 3 | Web App Manifest | ✅ Done | `public/manifest.json` |
| 4 | Next.js Config (rewrites + PWA headers) | ✅ Done | `next.config.js` |
| 5 | Offline Fallback Page | ✅ Done | `/offline` route |
| 6 | Mobile Meta Tags (Apple + Android) | ✅ Done | `layout.tsx` |
| 7 | CORS + API Proxy Configuration | ✅ Done | `next.config.js` rewrites |
| 8 | Frontend-Backend Integration | ✅ Done | All 16 pages connected to live API |

---

## 1. PWA — Progressive Web App Setup

The web app is now **installable on mobile devices** as a standalone app.

### manifest.json
```json
{
  "name": "SG CampusSwap",
  "short_name": "CampusSwap",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#F3F4F6",
  "theme_color": "#2563EB",
  "orientation": "portrait-primary",
  "icons": [...],    // 72×72 to 512×512
  "shortcuts": [
    { "name": "Sell an Item", "url": "/sell" },
    { "name": "Messages", "url": "/messages" }
  ]
}
```

### Service Worker (`sw.js`)
- **Cache-first** for static assets (CSS, JS, fonts, images)
- **Network-first** for API calls
- **Offline fallback** page when network unavailable
- **Push notification** listener (placeholder — ready for FCM)
- **Notification click** handler (opens relevant page)

### Registration
`PwaRegister` client component auto-registers SW on mount (embedded in root layout).

---

## 2. Mobile Pre-Work

### Apple / iOS
```html
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="default" />
<link rel="apple-touch-icon" href="/icons/icon-192x192.png" />
```

### Viewport Config
```typescript
export const viewport: Viewport = {
  themeColor: '#2563EB',
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,  // Prevents zoom on double-tap (app-like feel)
};
```

### Capacitor / Ionic CORS
Added `capacitor://localhost` and `ionic://localhost` to backend CORS origins so the future Capacitor-wrapped mobile app can call the API directly.

---

## 3. Next.js Configuration

```javascript
// next.config.js — key additions:
{
  // API proxy → FastAPI backend
  async rewrites() {
    return [{
      source: '/api/:path*',
      destination: 'http://localhost:8000/api/:path*',
    }];
  },

  // PWA headers for service worker
  async headers() {
    return [{
      source: '/sw.js',
      headers: [
        { key: 'Service-Worker-Allowed', value: '/' },
        { key: 'Cache-Control', value: 'no-cache' },
      ],
    }];
  },
}
```

Benefit: Frontend calls `/api/v1/...` with no CORS issues — Next.js proxies to the backend.

---

## 4. Frontend-Backend Integration

| Page | API Endpoint | Status |
|------|-------------|--------|
| Home (`/`) | `GET /api/v1/items` | ✅ Infinite scroll + category filter |
| Browse (`/browse`) | `GET /api/v1/search` | ✅ Full-text + filters |
| Item Detail (`/item/[id]`) | `GET /api/v1/items/{id}` | ✅ Seller info + images |
| Create Listing (`/sell`) | `POST /api/v1/items` + upload | ✅ Image upload via Cloudinary |
| Login (`/login`) | `POST /api/v1/auth/login` | ✅ JWT auto-refresh |
| Register (`/register`) | `POST /api/v1/auth/register` | ✅ Domain whitelist validation |
| Verify Email | `POST /api/v1/auth/verify` | ✅ |
| Profile (`/profile`) | `GET /api/v1/auth/me` | ✅ |
| Edit Profile | `PUT /api/v1/users/me` | ✅ |
| My Listings | `GET /api/v1/users/me/listings` | ✅ |
| Reviews (`/reviews`) | `GET /api/v1/reviews/*` | ✅ Rating summary |
| Messages (`/messages`) | `GET /api/v1/chat/rooms` + Firebase | ✅ Real-time via Firestore |
| Settings | Client-only | ✅ |

---

## 5. Offline Page

```
/offline → Shown when PWA detects no network
  - 📡 Icon + "You're Offline" message
  - "Try Again" button → reloads the page
  - Styled consistently with the app theme
```

---

## Next Week (W10) Tasks

1. Generate actual PNG icons from `icon.svg` (use sharp or realfavicongenerator.net)
2. Deploy to Vercel
3. Capacitor wrapper to create native APK/IPA from the PWA
4. Push notification integration with FCM
5. E2E testing

---

> **Web app is PWA-ready.** Installable on iOS/Android home screen. Service worker provides offline support. Ready for W10 Capacitor mobile app packaging.
