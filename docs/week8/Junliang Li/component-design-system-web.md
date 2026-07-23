# SG CampusSwap — Web Component Design System

> **Designer**: Junliang Li | **Week 8** | **Framework**: Next.js + Tailwind CSS

---

## 1. Design Tokens (CSS Variables)

```css
:root {
  /* Sidebar */
  --sidebar-bg: #111827;
  --sidebar-hover: #1F2937;
  --sidebar-active: #374151;
  --sidebar-text: #D1D5DB;
  --sidebar-text-active: #FFFFFF;
  --sidebar-icon: #9CA3AF;
  --sidebar-icon-active: #60A5FA;
  --sidebar-width: 240px;

  /* Content */
  --bg-main: #F3F4F6;
  --bg-card: #FFFFFF;

  /* Brand */
  --color-primary: #3B82F6;
  --color-primary-hover: #2563EB;
  --color-accent: #F59E0B;
  --color-success: #10B981;
  --color-error: #EF4444;
  --color-warning: #F59E0B;

  /* Text */
  --text-primary: #111827;
  --text-secondary: #6B7280;
  --text-muted: #9CA3AF;

  /* Border & Shadow */
  --border-color: #E5E7EB;
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);

  /* Spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;
}
```

---

## 2. Component Specifications

### 2.1 Sidebar

```
Props:
  - activeRoute: string
  - user: { name, email, university, campus, avatarUrl }

States:
  - Default: all items visible, active item highlighted
  - Collapsed (mobile): hamburger trigger → overlay drawer
  - Loading: user section shows skeleton

Items:
  1. Home (🏠) → /
  2. Browse (🔍) → /browse
  3. Messages (💬) → /messages (badge: unread count)
  4. My Listings (📦) → /my-listings
  5. Settings (⚙️) → /settings

Dimensions:
  - Width: 240px (desktop), 100% (mobile drawer)
  - Item height: 44px
  - Padding: 12px 16px
  - Gap between groups: 24px
  - Logo section: padding 20px 16px, height 64px
  - User section: border-top, padding 16px, position bottom
```

### 2.2 ItemCard

```
Props:
  - item: { id, title, price, thumbnailUrl, category, condition,
            campus, rating, reviewCount, createdAt }
  - variant: 'grid' | 'list'

States:
  - Default: thumbnail + title + price + rating
  - Loading: skeleton rectangle (280x200)
  - Sold: overlay badge "SOLD" at top-right
  - Reserved: overlay badge "RESERVED" at top-right

Grid Variant:
  ┌──────────────────────┐
  │ ┌──────────────────┐ │
  │ │   THUMBNAIL      │ │  280px width
  │ │   200px height    │ │  200px image height
  │ └──────────────────┘ │
  │                      │
  │  $25.00              │  Price: 20px, bold, accent color
  │  CS1010 Textbook     │  Title: 16px, 600 weight, 2-line clamp
  │                      │
  │  🏷️ Textbook  ✨ New │  Category + Condition chips
  │                      │
  │  📍 NUS · UTown      │  Campus + meetup
  │  ⭐ 4.5 (12)         │  Rating stars + count
  │  2 days ago          │  Timestamp
  └──────────────────────┘

  - Border: 1px solid var(--border-color)
  - Border-radius: var(--radius-md)
  - Background: var(--bg-card)
  - Shadow: var(--shadow-sm)
  - Hover: shadow-md + translateY(-2px)
  - Transition: 150ms ease
```

### 2.3 SearchBar

```
Props:
  - value: string
  - onChange: (value: string) => void
  - placeholder: string
  - onClear: () => void

States:
  - Empty: placeholder visible, magnifier icon
  - Typing: text + clear button (✕) at right
  - Focused: blue ring (2px, #3B82F6)
  - Loading: spinner at right (debounced search)

Dimensions:
  - Height: 44px
  - Padding: 0 16px
  - Icon: 20px, left 12px
  - Border-radius: var(--radius-md)
  - Background: white
  - Border: 1px solid var(--border-color)
```

### 2.4 CategoryChips

```
Props:
  - categories: { key, label }[]
  - active: string | null
  - onChange: (key: string | null) => void

Layout:
  - Horizontal scroll, no scrollbar
  - Gap: 8px between chips
  - Padding: 4px 12px per chip
  - Height: 32px
  - Border-radius: var(--radius-full)

States:
  - Inactive: bg-gray-100, text-gray-600
  - Active: bg-blue-500, text-white
  - Hover (inactive): bg-gray-200
```

### 2.5 FilterModal

```
Layout:
  ┌──────────────────────────────────┐
  │  Filters                    ✕    │
  ├──────────────────────────────────┤
  │  Category                        │
  │  [All] [Textbook] [Electronics]  │
  │  [Furniture] [Daily] [Other]     │
  │                                  │
  │  Price Range                     │
  │  $0 ├────────●──────┤ $500+     │
  │       $10 — $200                 │
  │                                  │
  │  Condition                       │
  │  [Like New] [Good] [Fair] [Worn] │
  │                                  │
  │  Campus                          │
  │  [All Campuses        ▼]        │
  │                                  │
  │  Sort By                         │
  │  ○ Newest First                  │
  │  ○ Price: Low → High             │
  │  ○ Price: High → Low             │
  │  ○ Nearest                       │
  │                                  │
  │  [Reset]       [Apply (12)]      │
  └──────────────────────────────────┘

  - Width: 400px (fixed)
  - Max-height: 90vh
  - Border-radius: var(--radius-lg)
  - Background: white
  - Overlay: bg-black/50
```

### 2.6 ChatBubble

```
Props:
  - message: { id, text, senderId, timestamp, type }
  - isOwn: boolean

Received (left-aligned):
  ┌────────────────────────────┐
  │ Is this still available?   │  bg: gray-100
  │ 2:15 PM                    │  text: gray-900
  └────────────────────────────┘  radius: 12px (top-left: 4px)

Sent (right-aligned):
              ┌──────────────────┐
              │ Yes! Are you at  │  bg: blue-500
              │ UTown?          │  text: white
              │ 2:18 PM         │  radius: 12px (top-right: 4px)
              └──────────────────┘

Image attachment:
  - Max-width: 240px
  - Border-radius: 8px
  - Click to view full-size modal
```

### 2.7 RatingStars

```
Props:
  - value: number (0–5)
  - size: 'sm' (16px) | 'md' (20px) | 'lg' (24px)
  - interactive?: boolean

Display mode:
  ⭐⭐⭐⭐⭐  (filled: amber-400, empty: gray-200)
  - Half-star supported: ⭐⭐⭐⭐½

Interactive mode (review form):
  - Hover: fill stars up to hovered position
  - Click: set value
  - Active: amber-400 fill
```

### 2.8 Skeleton Loading

```
Home Page Grid Skeleton:
  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
  │ ████  │ │ ████  │ │ ████  │ │ ████  │
  │ ████  │ │ ████  │ │ ████  │ │ ████  │
  │ ██    │ │ ██    │ │ ██    │ │ ██    │
  │ ████  │ │ ████  │ │ ████  │ │ ████  │
  └──────┘ └──────┘ └──────┘ └──────┘

  - 4 cards × 2 rows = 8 skeletons
  - Gray-200 background with pulse animation
  - Matches exact card dimensions (280×320)
```

---

## 3. Interaction Patterns

| Pattern | Behavior |
|---------|----------|
| Card click | Navigate to `/item/[id]` |
| Card hover | Shadow increase + slight lift (2px) |
| Button press | Scale to 0.97 for 100ms |
| Sidebar item hover | Background transition 150ms |
| Modal open | Fade-in overlay (150ms) + slide-up panel (200ms) |
| Toast notification | Slide-in from top-right, auto-dismiss 4s |
| Pull-to-refresh (mobile) | Not applicable (web) — manual Refresh button |
| Infinite scroll | IntersectionObserver on sentinel div at grid bottom |
| Image carousel swipe | Drag or arrow buttons |

---

> **Implementation**: Tailwind CSS classes map directly to these specs.
> **Handoff**: Ready for Renxian (Frontend Lead) to implement in Next.js.
