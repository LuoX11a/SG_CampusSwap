# SG CampusSwap — Web Design Specifications (Week 8)

> **Designer**: Junliang Li (UI/UX) | **Date**: 2026-07-01 (Week 8)
> **Based on**: Figma Make prototype "Web-version-request"
> **Target**: Desktop-first web application (responsive to tablet)

---

## 1. Design Direction: Dark Sidebar + Light Content

The Figma Make prototype establishes a **split-panel layout**:

```
┌──────────┬─────────────────────────────────────────────┐
│          │                                             │
│  DARK    │         LIGHT CONTENT AREA                  │
│  SIDEBAR │         (background: #F3F4F6)              │
│  240px   │                                             │
│          │   ┌─────────────────────────────────────┐  │
│  ┌────┐  │   │  Search Bar                         │  │
│  │LOGO│  │   └─────────────────────────────────────┘  │
│  └────┘  │                                             │
│          │   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐    │
│  🏠 Home │   │ Card │ │ Card │ │ Card │ │ Card │    │
│  🔍 Brws │   └──────┘ └──────┘ └──────┘ └──────┘    │
│  💬 Chat │   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐    │
│  📦 List │   │ Card │ │ Card │ │ Card │ │ Card │    │
│  ⭐ Savd │   └──────┘ └──────┘ └──────┘ └──────┘    │
│  ⚙️ Sett │                                             │
│          │        (infinite scroll grid)              │
│  ──────  │                                             │
│  👤 User │                                             │
│          │                                             │
└──────────┴─────────────────────────────────────────────┘
```

---

## 2. Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| **Sidebar** | | |
| `sidebar-bg` | `#111827` (Gray 900) | Sidebar background |
| `sidebar-hover` | `#1F2937` (Gray 800) | Menu item hover |
| `sidebar-active` | `#374151` (Gray 700) | Active menu item |
| `sidebar-text` | `#D1D5DB` (Gray 300) | Menu item text |
| `sidebar-text-active` | `#FFFFFF` | Active menu text |
| `sidebar-icon` | `#9CA3AF` (Gray 400) | Menu icons |
| `sidebar-icon-active` | `#60A5FA` (Blue 400) | Active menu icon |
| **Content** | | |
| `bg-main` | `#F3F4F6` (Gray 100) | Main content background |
| `bg-card` | `#FFFFFF` | Card background |
| **Brand** | | |
| `primary` | `#3B82F6` (Blue 500) | Primary buttons, links |
| `primary-hover` | `#2563EB` (Blue 600) | Button hover |
| `accent` | `#F59E0B` (Amber 500) | Price, CTA highlights |
| `success` | `#10B981` (Green 500) | Success states |
| `error` | `#EF4444` (Red 500) | Error states |
| `warning` | `#F59E0B` (Amber 500) | Warning states |
| **Text** | | |
| `text-primary` | `#111827` (Gray 900) | Primary text |
| `text-secondary` | `#6B7280` (Gray 500) | Secondary text |
| `text-muted` | `#9CA3AF` (Gray 400) | Muted text, placeholders |
| **Border** | | |
| `border` | `#E5E7EB` (Gray 200) | Card borders, dividers |

> **Note**: Sidebar uses Gray 900 instead of the original Indigo 900. The prototype shows a neutral dark sidebar. The blue accent (`#3B82F6`) aligns with the icon highlight color in the prototype.

---

## 3. Typography

| Token | Font | Size | Weight | Line Height | Usage |
|-------|------|------|--------|-------------|-------|
| `display` | Inter | 32px | 700 | 40px | Page hero titles |
| `h1` | Inter | 24px | 700 | 32px | Page titles |
| `h2` | Inter | 20px | 600 | 28px | Section headers |
| `h3` | Inter | 16px | 600 | 24px | Card titles |
| `body-lg` | Inter | 16px | 400 | 24px | Large body text |
| `body` | Inter | 14px | 400 | 20px | Primary content |
| `body-sm` | Inter | 13px | 400 | 18px | Secondary info |
| `caption` | Inter | 12px | 400 | 16px | Timestamps, meta |
| `price` | Inter | 20px | 700 | 28px | Price display (accent color) |
| `sidebar-label` | Inter | 13px | 500 | 18px | Sidebar menu items |

---

## 4. Spacing System

| Token | Value | Usage |
|-------|-------|-------|
| `space-1` | 4px | Tight spacing within components |
| `space-2` | 8px | Item gaps, icon padding |
| `space-3` | 12px | Internal component padding |
| `space-4` | 16px | Card padding, standard gap |
| `space-5` | 20px | Section gaps |
| `space-6` | 24px | Page content padding |
| `space-8` | 32px | Section vertical spacing |
| `space-10` | 40px | Page-level separation |

---

## 5. Sidebar Component Spec

```
┌──────────────────────┐
│                      │  Width: 240px (fixed)
│  ┌────────────────┐  │  Background: #111827
│  │   LOGO (32px)  │  │  Height: 100vh (sticky)
│  │   SG CampusSwap │  │  Overflow-y: auto
│  └────────────────┘  │
│                      │
│  ─── NAVIGATION ─── │
│  ┌────────────────┐  │
│  │ 🏠  Home       │  │  Height: 44px per item
│  └────────────────┘  │  Padding: 12px 16px
│  ┌────────────────┐  │  Border-radius: 8px
│  │ 🔍  Browse     │  │  Icon: 20px, left-aligned
│  └────────────────┘  │  Label: 13px, Inter 500
│  ┌────────────────┐  │
│  │ 💬  Messages   │  │  Active state:
│  └────────────────┘  │    bg: #374151
│  ┌────────────────┐  │    text: #FFFFFF
│  │ 📦  My Listings│  │    icon: #60A5FA
│  └────────────────┘  │    left border: 3px #3B82F6
│  ┌────────────────┐  │
│  │ ⚙️  Settings   │  │  Hover state:
│  └────────────────┘  │    bg: #1F2937
│                      │
│  ─── USER ───────── │
│  ┌────────────────┐  │
│  │ 👤  Alex Chen  │  │  User section at bottom
│  │    NUS · UTown │  │
│  └────────────────┘  │
│                      │
└──────────────────────┘
```

---

## 6. Layout Breakpoints

| Breakpoint | Width | Columns | Sidebar |
|------------|-------|---------|---------|
| `sm` | < 768px | 1 col, sidebar → hamburger | Collapsed |
| `md` | 768px – 1024px | 2 columns | Visible (200px) |
| `lg` | 1024px – 1280px | 3 columns | Visible (240px) |
| `xl` | > 1280px | 4 columns | Visible (240px) |

---

## 7. Component Library Mapping

| Component | Implementation | Notes |
|-----------|---------------|-------|
| Sidebar | Custom (Tailwind) | Fixed left, 240px |
| Card Grid | CSS Grid `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))` | Responsive |
| ItemCard | Custom component | Thumbnail + title + price + rating |
| SearchBar | Custom input with magnifier icon | Sticky top, full width in content area |
| CategoryChips | Horizontal scroll flex row | Click to filter |
| Button (Primary) | Tailwind `bg-blue-500 hover:bg-blue-600` | 40px height |
| Button (Secondary) | Tailwind `border border-gray-300` | 40px height |
| Modal | Headless UI Dialog | Filter, confirmations |
| Image Carousel | Custom (swipeable) | Item detail page |
| Badge | Custom span | Success/warning/error |
| Rating Stars | Custom SVG component | 1–5 stars, display only (except review form) |
| Toast | React Hot Toast | Success/error notifications |

---

## 8. Screen Inventory (Web Adaptation)

| # | Screen | Original (Mobile) | Web Adaptation |
|---|--------|-------------------|----------------|
| 1 | Login | Full-screen form | Centered card (400px) with sidebar hidden |
| 2 | Register | Full-screen form | Centered card (480px) with sidebar hidden |
| 3 | Verify Email | Full-screen OTP | Centered card with sidebar hidden |
| 4 | Home | Single column list | Multi-column grid + sidebar |
| 5 | Search Results | Full screen with filter modal | Sidebar filter panel + grid results |
| 6 | Item Detail | Full screen scroll | Two-column: carousel left + info right |
| 7 | Create Listing | Full screen form | Two-column: form left + preview right |
| 8 | Chat List | Full screen list | Sidebar conversation list + preview pane |
| 9 | Chat Room | Full screen | Three-panel: sidebar + list + conversation |
| 10 | Profile | Full screen scroll | Centered max-width 640px |
| 11 | Edit Profile | Full screen form | Centered max-width 480px |
| 12 | Public Profile | Full screen | Centered max-width 640px |
| 13 | Reviews | Full screen list | Centered max-width 640px |
| 14 | My Listings | Full screen list | Grid layout with tabs (active/sold) |
| 15 | Settings | Full screen list | Centered max-width 560px |

---

## 9. States Coverage

**Every screen must handle:**
- **Loading**: Skeleton cards/rows (pulsing gray placeholders)
- **Empty**: Illustration + message + CTA (e.g. "No items yet. Be the first to sell!")
- **Error**: Inline error messages + retry button
- **Success**: Toast notification + state update

---

> **Handoff Status**: Ready for frontend development (Renxian + Jiahai)
> **Figma Prototype Reference**: `figma.com/make/oMmR33f4LFpNjfF8jRaEOS/Web-version-request`
