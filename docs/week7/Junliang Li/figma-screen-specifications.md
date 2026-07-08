# SG CampusSwap — Screen Design Specifications (High-Fidelity)

> **Designer**: Junliang Li (UI/UX) | **Tool**: Figma (Education Plan)  
> **Status**: All screens specified — ready for development handoff | **Last Updated**: Week 7  
> **Design System**: Material Design 3 (React Native Paper compatible)

---

## 1. Design System

### 1.1 Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `primary` | `#1A237E` (Indigo 900) | App bar, primary buttons, active tabs |
| `primary-light` | `#534BAE` | Secondary buttons, links |
| `accent` | `#FF6F00` (Amber 800) | Price text, CTA highlights, badges |
| `success` | `#2E7D32` | Sold badge, success messages |
| `error` | `#C62828` | Error messages, delete actions |
| `warning` | `#F57F17` | Reserved badge, warnings |
| `surface` | `#FFFFFF` | Card backgrounds |
| `background` | `#F5F5F5` | Screen background |
| `text-primary` | `#212121` | Primary text |
| `text-secondary` | `#757575` | Secondary text, captions |
| `text-hint` | `#BDBDBD` | Placeholders, hints |
| `divider` | `#E0E0E0` | Separators, borders |

### 1.2 Typography

| Style | Font | Size | Weight | Usage |
|-------|------|------|--------|-------|
| H1 | Inter | 24px | 700 | Screen titles |
| H2 | Inter | 20px | 600 | Section headers |
| H3 | Inter | 16px | 600 | Card titles |
| Body | Inter | 14px | 400 | Primary content |
| Caption | Inter | 12px | 400 | Secondary info, timestamps |
| Price | Inter | 18px | 700 | Price display (accent color) |

### 1.3 Spacing Grid

| Token | Value | Usage |
|-------|-------|-------|
| `xs` | 4px | Icon padding, tight spacing |
| `sm` | 8px | Item spacing within components |
| `md` | 16px | Card padding, list item padding |
| `lg` | 24px | Screen horizontal padding |
| `xl` | 32px | Section vertical spacing |

### 1.4 Components

| Component | Library | Notes |
|-----------|---------|-------|
| Text Input | React Native Paper `TextInput` | Outlined variant, 48px height |
| Button (Primary) | React Native Paper `Button` | Filled, primary color, 48px height |
| Button (Secondary) | React Native Paper `Button` | Outlined, 48px height |
| Card | Custom `TouchableOpacity` | 8px border-radius, surface color, drop shadow |
| Chip | React Native Paper `Chip` | For category/filter tags |
| Bottom Tabs | `@react-navigation/bottom-tabs` | 5 tabs (see navigation below) |
| Search Bar | React Native Paper `Searchbar` | Sticky header on HomeScreen |
| Image Picker | `react-native-image-picker` | Grid of selected images |
| Rating Stars | Custom component | 1–5 stars, tappable |
| Badge | Custom View | Success/warning/error colors |
| Modal | React Native `Modal` | Filter modal, campus picker |

---

## 2. Screen Specifications

### 2.1 Auth Stack

#### LoginScreen
```
┌──────────────────────────────────┐
│                                  │
│         ┌──────────┐             │  ← App Logo (120x120)
│         │   LOGO    │             │
│         └──────────┘             │
│                                  │
│    SG CampusSwap                 │  ← H1, primary color
│    Campus marketplace for you    │  ← Caption, text-secondary
│                                  │
│  ┌──────────────────────────┐   │
│  │ 📧  University email      │   │  ← TextInput, outlined
│  └──────────────────────────┘   │
│                                  │
│  ┌──────────────────────────┐   │
│  │ 🔒  Password              │   │  ← TextInput, secure, outlined
│  └──────────────────────────┘   │
│                                  │
│  ┌──────────────────────────┐   │
│  │        LOG IN             │   │  ← Button (Primary), full width
│  └──────────────────────────┘   │
│                                  │
│     Don't have an account?       │
│     ────  Register  ────         │  ← TextButton, primary-light
│                                  │
└──────────────────────────────────┘
```
**States**: Default, Loading (button spinner), Error (inline error message above button), Network Error (full-screen retry)

---

#### RegisterScreen
```
┌──────────────────────────────────┐
│  ← Back                          │  ← App Bar
├──────────────────────────────────┤
│  Create Account                  │  ← H1
│  Join the campus community       │  ← Caption
│                                  │
│  ┌──────────────────────────┐   │
│  │ 👤  Username              │   │
│  └──────────────────────────┘   │
│  ┌──────────────────────────┐   │
│  │ 📧  University email      │   │  ← Domain whitelist hint below
│  └──────────────────────────┘   │
│     e.g. e0123456@u.nus.edu     │  ← Caption hint
│  ┌──────────────────────────┐   │
│  │ 🏫  University             │   │  ← Dropdown picker
│  └──────────────────────────┘   │
│  ┌──────────────────────────┐   │
│  │ 📍  Campus                 │   │  ← Dropdown picker
│  └──────────────────────────┘   │
│  ┌──────────────────────────┐   │
│  │ 🔒  Password              │   │
│  └──────────────────────────┘   │
│  ┌──────────────────────────┐   │
│  │ 🔒  Confirm password      │   │
│  └──────────────────────────┘   │
│                                  │
│  ┌──────────────────────────┐   │
│  │        REGISTER           │   │
│  └──────────────────────────┘   │
│                                  │
│  By registering, you agree to   │
│  Terms of Service & Privacy     │
└──────────────────────────────────┘
```
**Validation**: Email domain whitelist check (client-side hint + server-side enforcement), password ≥8 chars with 1 uppercase + 1 digit, username 3–20 chars

---

#### EmailVerificationScreen
```
┌──────────────────────────────────┐
│  ← Back                          │
├──────────────────────────────────┤
│  Verify Your Email               │  ← H1
│                                  │
│  ┌──────────────────────────┐   │
│  │     📧  Envelope Icon     │   │  ← Large centered icon
│  │                            │   │
│  │  We sent a 6-digit code   │   │  ← Body, centered
│  │  to e0123456@u.nus.edu    │   │  ← Body, bold email
│  └──────────────────────────┘   │
│                                  │
│  ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐│  ← 6 individual digit inputs
│  │  │ │  │ │  │ │  │ │  │ │  ││     auto-advancing
│  └──┘ └──┘ └──┘ └──┘ └──┘ └──┘│
│                                  │
│     Didn't receive the code?     │
│     ────  Resend (30s)  ────     │  ← TextButton with countdown
│                                  │
└──────────────────────────────────┘
```
**States**: Empty, Partial fill, Loading (auto-verify on 6th digit), Success → navigate to Home, Error (shake animation + "Invalid code"), Resend cooldown (30s timer)

---

### 2.2 Main Tab Navigator

```
┌─────────────────────────────────────────────┐
│  Tab Bar (bottom, 56px height)              │
│  ┌────────┬────────┬────────┬────────┬────┐ │
│  │ 🏠     │ 🔍     │ ➕      │ 💬      │ 👤 │ │
│  │ Home   │ Search │ Sell   │ Chats   │ Me │ │
│  └────────┴────────┴────────┴────────┴────┘ │
│  Active tab: primary color icon + label     │
│  Inactive tab: text-secondary icon only     │
│  Center "Sell" button: FAB, accent color,   │
│  elevated (56x56 circle)                    │
└─────────────────────────────────────────────┘
```

---

#### HomeScreen (Tab 1: Home)
```
┌──────────────────────────────────┐
│  SG CampusSwap     🏫 NUS ▼     │  ← Top bar: title + campus picker
├──────────────────────────────────┤
│  ┌──────────────────────────┐   │
│  │ 🔍  Search items...       │   │  ← SearchBar, sticky
│  └──────────────────────────┘   │
│                                  │
│  ┌──────┐ ┌──────┐ ┌──────┐    │
│  │ All  │ │Textbk│ │Electr│    │  ← Horizontal chip scroll
│  └──────┘ └──────┘ └──────┘    │     (category quick filter)
│                                  │
│  ┌────────────────────────────┐ │
│  │ ┌────────┐                 │ │
│  │ │  IMG   │  Textbook Title │ │  ← Item Card (repeating)
│  │ │        │  $25            │ │     ┌ Thumbnail (100x100)
│  │ └────────┘  NUS · UTown   │ │     ├ Title (H3, max 2 lines)
│  │            ⭐ 4.5 (12)     │ │     ├ Price (accent, H2)
│  └────────────────────────────┘ │     ├ Campus · 1d ago
│                                  │     └ Rating stars + count
│  ┌────────────────────────────┐ │
│  │ ┌────────┐                 │ │  ← Item Card 2
│  │ │  IMG   │  Laptop for sale│ │
│  │ │        │  $450           │ │
│  │ └────────┘  NTU · NorthSpn │ │
│  │            ⭐ 4.8 (34)     │ │
│  └────────────────────────────┘ │
│                                  │
│  ┌────────────────────────────┐ │
│  │ ┌────────┐                 │ │  ← Item Card 3...
│  │ │  IMG   │  Desk Lamp      │ │
│  └────────────────────────────┘ │
│         (infinite scroll)        │
└──────────────────────────────────┘
```
**States**: Loading (skeleton cards ×5), Empty ("No items yet. Be the first to sell!"), Error (retry), Pull-to-refresh

---

#### SearchResultsScreen (Tab 2: Search)
```
┌──────────────────────────────────┐
│  ┌──────────────────────────┐   │
│  │ 🔍  CS1010               │   │  ← SearchBar, auto-focused
│  └──────────────────────────┘   │     with clear button
├──────────────────────────────────┤
│  Results for "CS1010" (12)      │  ← Body, text-secondary
│                                  │
│  ┌────────────────────────────┐ │
│  │ ┌────────┐                 │ │  ← Result cards (same as Home)
│  │ │  IMG   │  CS1010 Textbook │ │
│  └────────────────────────────┘ │
│         (scrollable list)        │
│                                  │
│  ┌──────────────────────────┐   │
│  │    🔽  Filter (2)         │   │  ← Filter button, shows active count
│  └──────────────────────────┘   │     opens FilterModal
└──────────────────────────────────┘
```

---

#### FilterModal (overlay on SearchResults)
```
┌──────────────────────────────────┐
│  Filters                    ✕    │  ← Header + close button
├──────────────────────────────────┤
│  Category                        │
│  ┌──────┐ ┌──────┐ ┌──────┐    │
│  │ All  │ │Textbk│ │Electr│    │  ← Multi-select chips
│  │  ✓  │ │      │ │      │    │     (only one selected = "All")
│  └──────┘ └──────┘ └──────┘    │
│  ┌──────┐ ┌──────┐ ┌──────┐    │
│  │Furnit│ │Daily │ │ Other│    │
│  └──────┘ └──────┘ └──────┘    │
│                                  │
│  Campus                          │
│  ┌──────────────────────────┐   │
│  │ All Campuses         ▼   │   │  ← Single-select dropdown
│  └──────────────────────────┘   │
│                                  │
│  Price Range                     │
│  $0 ───────●──────── $500+      │  ← Range slider (dual handle)
│       $10 — $200                │     with text labels
│                                  │
│  Condition                       │
│  ┌──────┐ ┌──────┐ ┌──────┐    │
│  │LikeNew│ │ Good │ │ Fair │    │  ← Multi-select chips
│  └──────┘ └──────┘ └──────┘    │
│  ┌──────┐                      │
│  │ Worn │                      │
│  └──────┘                      │
│                                  │
│  Sort By                         │
│  ○ Newest first                  │  ← Radio buttons
│  ○ Price: Low to High            │
│  ○ Price: High to Low            │
│  ○ Nearest campus                │
│                                  │
│  ┌──────────┐  ┌──────────────┐ │
│  │  Reset   │  │  Apply (12)  │ │  ← Two buttons
│  └──────────┘  └──────────────┘ │     Reset = outlined
└──────────────────────────────────┘                     Apply = filled primary
```
**States**: Default (no filters), Active filters (badge count on Filter button), Reset confirmation

---

#### CreateListingScreen (Tab 3: Sell)
```
┌──────────────────────────────────┐
│  ← Cancel     New Listing  Post  │  ← App Bar (Post disabled until valid)
├──────────────────────────────────┤
│                                  │
│  Add Photos                      │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐   │
│  │ 📷 │ │    │ │    │ │    │   │  ← Image grid (max 5)
│  │ +  │ │    │ │    │ │    │   │     tap + to open picker
│  └────┘ └────┘ └────┘ └────┘   │
│                                  │
│  ┌──────────────────────────┐   │
│  │ What are you selling?     │   │  ← Title TextInput
│  └──────────────────────────┘   │
│                                  │
│  ┌──────────────────────────┐   │
│  │ Category           ▼     │   │  ← Dropdown
│  └──────────────────────────┘   │
│                                  │
│  ┌──────────────────────────┐   │
│  │ Description...            │   │  ← Multiline TextInput
│  │                           │   │     min 3 lines, max 10
│  │                           │   │
│  └──────────────────────────┘   │
│                                  │
│  ┌──────────────────┐ ┌──────┐ │
│  │ Course Code       │ │ $0.00│ │  ← Row: course code (optional)
│  │ (for textbooks)   │ │Price │ │     + price (required)
│  └──────────────────┘ └──────┘ │
│                                  │
│  ┌──────────────────────────┐   │
│  │ Condition          ▼     │   │  ← Dropdown
│  └──────────────────────────┘   │
│                                  │
│  ┌──────────────────────────┐   │
│  │ Meetup Point       ▼     │   │  ← Dropdown, campus-dependent
│  └──────────────────────────┘   │
│                                  │
└──────────────────────────────────┘
```
**States**: Empty form, Partially filled (Post button enabled when: ≥1 photo + title + category + price + condition), Submitting (button spinner), Success → navigate to ItemDetail, Validation errors (inline red text)

---

#### ItemDetailScreen
```
┌──────────────────────────────────┐
│  ← Back              ⋮ (More)   │  ← App Bar (More = Edit/Delete if owner)
├──────────────────────────────────┤
│  ┌────────────────────────────┐ │
│  │                            │ │
│  │      Image Carousel        │ │  ← FlatList horizontal, paging
│  │      ● ○ ○ ○  (dots)      │ │     swipeable, pinch-to-zoom
│  │                            │ │
│  └────────────────────────────┘ │
│                                  │
│  $25.00                     📍  │  ← Price (H1, accent) + Map icon
│                                  │
│  CS1010 Programming Methodology │  ← Title H1
│                                  │
│  ┌──────────┐  ┌──────────┐    │
│  │ Textbook │  │ Like New │    │  ← Category + Condition chips
│  └──────────┘  └──────────┘    │
│                                  │
│  ────────────────────────────── │
│  Description                     │  ← Section header
│  Barely used, bought last sem.  │  ← Body text
│  No highlights or annotations.  │
│  ────────────────────────────── │
│                                  │
│  👤 Seller Info                  │
│  ┌────────────────────────────┐ │
│  │ ┌────┐                     │ │
│  │ │AVTR│  Alex Chen          │ │  ← Tappable → Seller profile
│  │ └────┘  NUS · UTown       │ │
│  │         ⭐ 4.5 (12 reviews)│ │
│  └────────────────────────────┘ │
│                                  │
│  📍 Meetup Point                 │
│  ┌────────────────────────────┐ │
│  │ 📍  UTown Starbucks         │ │  ← Tappable → Open in maps
│  └────────────────────────────┘ │
│                                  │
│  ────────────────────────────── │
│  Listed 2 days ago · 128 views  │  ← Caption
│                                  │
│  ┌────────────────────────────┐ │
│  │      💬  CHAT WITH SELLER  │ │  ← Primary CTA button, full width
│  └────────────────────────────┘ │
│                                  │
└──────────────────────────────────┘
```
**Navigation from here**: Chat with seller → ChatScreen (pre-populated with item info), Seller avatar → PublicProfileScreen, Map icon → meetup point on map

---

#### ChatListScreen (Tab 4: Chats)
```
┌──────────────────────────────────┐
│  Messages                        │  ← App Bar
├──────────────────────────────────┤
│  ┌────────────────────────────┐ │
│  │ ┌────┐                     │ │
│  │ │AVTR│  Sarah Lim          │ │  ← Chat Row (repeating)
│  │ └────┘  Is this still avail?│ │     ┌ Avatar (48x48 circle)
│  │         2m ago         🔵   │ │     ├ Name (H3)
│  └────────────────────────────┘ │     ├ Last message preview (Body, text-secondary, 1 line)
│                                  │     ├ Timestamp (Caption, right-aligned)
│  ┌────────────────────────────┐ │     └ Unread dot (accent, 8px)
│  │ ┌────┐                     │ │
│  │ │AVTR│  Jason Tan          │ │
│  │ └────┘  Sure, meet at...   │ │
│  │         1h ago             │ │
│  └────────────────────────────┘ │
│                                  │
│         (scrollable list)        │
│                                  │
│  ─── Empty State ───             │
│  💬                              │
│  No messages yet                 │  ← When no chats exist
│  Start a conversation from       │
│  an item listing                 │
└──────────────────────────────────┘
```
**Real-time**: Firebase Firestore listeners update last message + timestamp automatically

---

#### ChatScreen
```
┌──────────────────────────────────┐
│  ← Back   Sarah Lim              │  ← App Bar
│            CS1010 Textbook · $25 │  ← Item reference (tappable)
├──────────────────────────────────┤
│                                  │
│  ┌────────────────────────────┐ │
│  │ Is this still available?   │ │  ← Received message bubble
│  │ 2:15 PM                    │ │     ┌ Left-aligned, surface color
│  └────────────────────────────┘ │     └ Timestamp below (Caption)
│                                  │
│                ┌──────────────┐ │
│                │ Yes! Are you │ │  ← Sent message bubble
│                │ at UTown?   │ │     ┌ Right-aligned, primary-light bg
│                │ 2:18 PM     │ │     └ White text
│                └──────────────┘ │
│                                  │
│  ┌────────────────────────────┐ │
│  │ I'm at the library now.    │ │  ← Received
│  │ Can meet at Starbucks?     │ │
│  │ 2:20 PM                    │ │
│  └────────────────────────────┘ │
│                                  │
│         (scrollable, auto-scroll │
│          to bottom on new msg)   │
│                                  │
├──────────────────────────────────┤
│  ┌──────────────────────┐  📎   │  ← Input bar (56px)
│  │ Type a message...     │  📷   │     TextInput + attachment icons
│  └──────────────────────┘  ▶️   │     Send button (primary, disabled when empty)
└──────────────────────────────────┘
```
**Real-time**: Messages appear instantly via Firestore `onSnapshot`

---

#### ProfileScreen (Tab 5: Me)
```
┌──────────────────────────────────┐
│  Profile                     ⚙️  │  ← App Bar + Settings gear
├──────────────────────────────────┤
│  ┌────────────────────────────┐ │
│  │     ┌────────┐             │ │
│  │     │ AVATAR │  Edit       │ │  ← Avatar (80x80 circle) + Edit link
│  │     │ 80x80  │             │ │
│  │     └────────┘             │ │
│  │                            │ │
│  │     Alex Chen              │ │  ← Username H1, centered
│  │     e0123456@u.nus.edu     │ │  ← Email Caption
│  │     NUS · UTown            │ │  ← University + campus
│  │                            │ │
│  │  ⭐ 4.5 (12 reviews)       │ │  ← Rating (stars + count)
│  └────────────────────────────┘ │
│                                  │
│  ─── My Listings ───             │
│  ┌────────────────────────────┐ │
│  │ ┌────────┐                 │ │  ← Active listings (scrollable)
│  │ │  IMG   │  CS1010 Textbook│ │     horizontally within card
│  │ └────────┘  $25 · Available│ │
│  └────────────────────────────┘ │
│  ┌────────────────────────────┐ │
│  │ ┌────────┐                 │ │
│  │ │  IMG   │  Desk Lamp      │ │
│  │ └────────┘  $10 · Reserved │ │
│  └────────────────────────────┘ │
│                                  │
│  ─── Quick Links ───             │
│  ┌──────────────────────────┐   │
│  │ 📦  My Listings       >  │   │  ← Tappable row items
│  │ ⭐  My Reviews        >  │   │
│  │ 🔒  Account Settings  >  │   │
│  │ ❓  Help & Feedback   >  │   │
│  └──────────────────────────┘   │
│                                  │
│  ┌──────────────────────────┐   │
│  │        LOG OUT            │   │  ← Destructive button (error color)
│  └──────────────────────────┘   │
└──────────────────────────────────┘
```

---

#### EditProfileScreen
```
┌──────────────────────────────────┐
│  ← Back     Edit Profile   Save  │
├──────────────────────────────────┤
│          ┌────────┐              │
│          │ AVATAR │              │  ← Tappable → image picker
│          │ 100x100│              │
│          │ Change │              │
│          └────────┘              │
│                                  │
│  Username                        │
│  ┌──────────────────────────┐   │
│  │ Alex Chen                 │   │
│  └──────────────────────────┘   │
│                                  │
│  University                      │
│  ┌──────────────────────────┐   │
│  │ NUS                  ▼   │   │
│  └──────────────────────────┘   │
│                                  │
│  Campus                          │
│  ┌──────────────────────────┐   │
│  │ UTown                ▼   │   │
│  └──────────────────────────┘   │
└──────────────────────────────────┘
```

---

#### PublicProfileScreen (viewing another user)
```
┌──────────────────────────────────┐
│  ← Back                          │
├──────────────────────────────────┤
│     ┌────────┐                   │
│     │ AVATAR │                   │
│     └────────┘                   │
│     Sarah Lim                    │
│     NUS · UTown                  │
│     ⭐ 4.8 (34 reviews)          │
│     Member since May 2026        │
│                                  │
│  ─── Reviews ───                 │
│  ┌────────────────────────────┐ │
│  │ ⭐⭐⭐⭐⭐  "Great seller!..."  │ │  ← Review cards
│  │ By: Jason T. · 2 weeks ago │ │
│  └────────────────────────────┘ │
│  ┌────────────────────────────┐ │
│  │ ⭐⭐⭐⭐  "Item as described" │ │
│  │ By: Mei L. · 1 month ago  │ │
│  └────────────────────────────┘ │
│                                  │
│  ─── Active Listings ───         │
│  (item cards, same as HomeScreen)│
└──────────────────────────────────┘
```

---

#### ReviewsScreen
```
┌──────────────────────────────────┐
│  ← Back     My Reviews           │
├──────────────────────────────────┤
│  Rating Summary                  │
│  ┌────────────────────────────┐ │
│  │      ⭐ 4.5                 │ │
│  │      12 reviews            │ │
│  │                            │ │
│  │  5★  ████████████  8      │ │  ← Bar chart
│  │  4★  ██████  3             │ │
│  │  3★  ██  1                 │ │
│  │  2★  ░  0                  │ │
│  │  1★  ░  0                  │ │
│  └────────────────────────────┘ │
│                                  │
│  ┌────────────────────────────┐ │
│  │ From: Jason Tan            │ │  ← Review cards
│  │ ⭐⭐⭐⭐⭐  "Very friendly..."  │ │
│  │ 2 weeks ago                │ │
│  │ Re: CS1010 Textbook       │ │
│  └────────────────────────────┘ │
│         (scrollable list)        │
└──────────────────────────────────┘
```

---

#### SettingsScreen
```
┌──────────────────────────────────┐
│  ← Back     Settings             │
├──────────────────────────────────┤
│  Account                         │
│  ┌──────────────────────────┐   │
│  │ 👤  Edit Profile      >  │   │
│  │ 🔒  Change Password   >  │   │
│  │ 📧  Email Settings    >  │   │
│  └──────────────────────────┘   │
│                                  │
│  Notifications                   │
│  ┌──────────────────────────┐   │
│  │ 🔔  Push Notifications [─]│   │  ← Toggle switches
│  │ 💬  Chat Messages     [─]│   │
│  │ 📦  Listing Updates   [─]│   │
│  └──────────────────────────┘   │
│                                  │
│  About                           │
│  ┌──────────────────────────┐   │
│  │ ℹ️  About SG CampusSwap > │   │
│  │ 📄  Privacy Policy    >  │   │
│  │ 📝  Terms of Service  >  │   │
│  │ 🗑️  Delete Account    >  │   │  ← Destructive, requires confirmation
│  └──────────────────────────┘   │
│                                  │
│  App Version 1.0.0               │  ← Caption, centered
└──────────────────────────────────┘
```

---

## 3. Navigation Flow Diagram

```
                    ┌─────────────┐
                    │  Splash     │
                    │  (Auto      │
                    │   check JWT)│
                    └──────┬──────┘
                           │
              ┌────────────┴────────────┐
              │ JWT valid?              │
         ┌────┴────┐              ┌────┴────┐
         │   YES    │              │   NO     │
         └────┬────┘              └────┬────┘
              │                        │
    ┌─────────┴──────────┐    ┌───────┴────────┐
    │   MainTabNavigator  │    │  AuthStack     │
    │  ┌────────────────┐ │    │ ┌────────────┐ │
    │  │ HomeScreen     │ │    │ │LoginScreen │ │
    │  │ SearchScreen   │ │    │ │RegisterScr │ │
    │  │ CreateListing  │ │    │ │VerifyEmail │ │
    │  │ ChatListScreen │ │    │ └────────────┘ │
    │  │ ProfileScreen  │ │    └────────────────┘
    │  └────────────────┘ │
    └─────────┬──────────┘
              │
    ┌─────────┼──────────────────────────┐
    │         │                          │
    ▼         ▼                          ▼
┌───────┐ ┌────────────┐  ┌──────────────┐
│ItemDet│ │ChatScreen   │  │EditProfile   │
│ailScr │ │(from ChatList│  │Screen        │
│       │ │ or ItemDet) │  │(from Profile)│
└───┬───┘ └────────────┘  └──────────────┘
    │
    ├──► PublicProfileScreen (tap seller avatar)
    ├──► ChatScreen (tap "Chat with Seller")
    └──► MapScreen (tap meetup point)
```

---

## 4. Handoff Checklist

- [ ] All screens designed in Figma at **375×812** (iPhone 13/14 frame) and **360×800** (Android reference)
- [ ] Design tokens exported as JSON (colors, typography, spacing)
- [ ] Component variants specified (default, hover, active, disabled, error)
- [ ] Micro-interactions noted (button press scale 0.97, swipe gestures, skeleton shimmer)
- [ ] Image assets exported: logo (5 sizes), empty state illustrations, onboarding illustrations
- [ ] Loading states designed: skeleton screens (Home, Search, Chats, Profile)
- [ ] Error states designed: network error (full screen), inline errors, 404 not found
- [ ] Empty states designed: no items, no search results, no messages, no reviews
- [ ] Accessibility: minimum 4.5:1 contrast ratio on all text, 48px minimum touch targets
- [ ] Prototype linked for usability testing (navigable click-through)

---

> **Figma file link**: [Insert Figma share link]  
> **Design review**: All screens reviewed by team on [Date TBD]  
> **Next update**: Post-usability testing refinements in W9
