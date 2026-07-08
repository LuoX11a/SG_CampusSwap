# Renxian Tang — Frontend Lead Deliverables (Week 7)

> **Role**: Frontend Lead | **Focus**: Expo scaffold, Navigation, Zustand stores, API client, HomeScreen, ItemDetailScreen, CreateListingScreen

---

## 1. Deliverables Checklist

| # | Deliverable | Status |
|---|------------|--------|
| 1 | Expo project scaffold + navigation | ✅ Ready |
| 2 | Zustand state management stores | ✅ Ready |
| 3 | API client (axios) + TypeScript types | ✅ Ready |
| 4 | HomeScreen + ItemCard spec | ✅ Ready |
| 5 | ItemDetailScreen spec | ✅ Ready |
| 6 | CreateListingScreen + ImagePicker spec | ✅ Ready |
| 7 | Auth flow screens spec | ✅ Ready |
| 8 | Literature review | ✅ Ready |

---

## 2. Project Setup

### 2.1 Expo Scaffold

```bash
# Create project (run once)
npx create-expo-app@latest mobile --template blank-typescript

cd mobile

# Install core dependencies
npx expo install react-native-paper expo-router expo-linking expo-constants
npx expo install @react-navigation/native @react-navigation/bottom-tabs @react-navigation/native-stack
npx expo install zustand @tanstack/react-query axios
npx expo install expo-image-picker expo-notifications expo-secure-store
npx expo install @react-native-firebase/app @react-native-firebase/firestore
npx expo install react-native-screens react-native-safe-area-context
npm install --save-dev @testing-library/react-native jest jest-expo
```

### 2.2 Navigation Architecture

```typescript
// app/_layout.tsx — Root layout
import { Stack } from 'expo-router';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { PaperProvider } from 'react-native-paper';

const queryClient = new QueryClient();

export default function RootLayout() {
  return (
    <QueryClientProvider client={queryClient}>
      <PaperProvider>
        <Stack screenOptions={{ headerShown: false }}>
          <Stack.Screen name="(auth)" />
          <Stack.Screen name="(tabs)" />
          <Stack.Screen name="item/[id]" options={{ headerShown: true, title: 'Item Detail' }} />
          <Stack.Screen name="chat/[id]" options={{ headerShown: true, title: 'Chat' }} />
          <Stack.Screen name="profile/[id]" options={{ headerShown: true, title: 'Profile' }} />
        </Stack>
      </PaperProvider>
    </QueryClientProvider>
  );
}
```

**Screen route mapping**:
```
app/
├── _layout.tsx                     ← Root layout (QueryClient + Paper + Stack)
├── (auth)/
│   ├── _layout.tsx                 ← Auth stack (no tabs)
│   ├── login.tsx                   ← LoginScreen
│   ├── register.tsx                ← RegisterScreen
│   └── verify-email.tsx            ← EmailVerificationScreen
├── (tabs)/
│   ├── _layout.tsx                 ← Bottom Tab Navigator (5 tabs)
│   ├── index.tsx                   ← HomeScreen (Tab 1, default)
│   ├── search.tsx                  ← SearchResultsScreen (Tab 2)
│   ├── sell.tsx                    ← CreateListingScreen (Tab 3, center FAB)
│   ├── chats.tsx                   ← ChatListScreen (Tab 4)
│   └── profile.tsx                 ← ProfileScreen (Tab 5)
├── item/
│   └── [id].tsx                    ← ItemDetailScreen (dynamic route)
├── chat/
│   └── [id].tsx                    ← ChatScreen (dynamic route)
├── profile/
│   └── [id].tsx                    ← PublicProfileScreen (dynamic route)
├── edit-profile.tsx                ← EditProfileScreen
├── my-listings.tsx                 ← MyListingsScreen
├── reviews.tsx                     ← ReviewsScreen
├── settings.tsx                    ← SettingsScreen
└── create-review.tsx               ← CreateReviewScreen
```

---

## 3. Zustand State Management

### 3.1 Auth Store

```typescript
// src/stores/authStore.ts
import { create } from 'zustand';
import * as SecureStore from 'expo-secure-store';
import { apiClient } from '../services/apiClient';
import { User, LoginRequest, RegisterRequest } from '../types';

interface AuthState {
  user: User | null;
  token: string | null;
  refreshToken: string | null;
  isLoading: boolean;
  isAuthenticated: boolean;

  // Actions
  login: (data: LoginRequest) => Promise<void>;
  register: (data: RegisterRequest) => Promise<void>;
  verifyEmail: (email: string, code: string) => Promise<void>;
  logout: () => void;
  restoreSession: () => Promise<void>;  // on app launch
  refreshAuth: () => Promise<void>;
}

export const useAuthStore = create<AuthState>((set, get) => ({
  user: null,
  token: null,
  refreshToken: null,
  isLoading: true,
  isAuthenticated: false,

  login: async (data) => {
    const res = await apiClient.post('/auth/login', data);
    const { access_token, refresh_token } = res.data;
    await SecureStore.setItemAsync('token', access_token);
    await SecureStore.setItemAsync('refreshToken', refresh_token);
    set({ token: access_token, refreshToken: refresh_token, isAuthenticated: true });
  },

  register: async (data) => {
    await apiClient.post('/auth/register', data);
    // After register → navigate to verify-email screen
  },

  verifyEmail: async (email, code) => {
    const res = await apiClient.post('/auth/verify-email', { email, code });
    const { access_token, refresh_token } = res.data;
    await SecureStore.setItemAsync('token', access_token);
    await SecureStore.setItemAsync('refreshToken', refresh_token);
    set({ token: access_token, refreshToken: refresh_token, isAuthenticated: true });
  },

  logout: () => {
    SecureStore.deleteItemAsync('token');
    SecureStore.deleteItemAsync('refreshToken');
    set({ user: null, token: null, refreshToken: null, isAuthenticated: false });
  },

  restoreSession: async () => {
    const token = await SecureStore.getItemAsync('token');
    if (token) {
      set({ token, isAuthenticated: true, isLoading: false });
      // Fetch user profile
      try {
        const res = await apiClient.get('/users/me');
        set({ user: res.data });
      } catch {
        get().logout();
      }
    }
    set({ isLoading: false });
  },

  refreshAuth: async () => {
    const refreshToken = await SecureStore.getItemAsync('refreshToken');
    if (!refreshToken) return get().logout();
    try {
      const res = await apiClient.post('/auth/refresh', { refresh_token: refreshToken });
      const { access_token, refresh_token } = res.data;
      await SecureStore.setItemAsync('token', access_token);
      await SecureStore.setItemAsync('refreshToken', refresh_token);
      set({ token: access_token, refreshToken: refresh_token });
    } catch {
      get().logout();
    }
  },
}));
```

### 3.2 Item Store

```typescript
// src/stores/itemStore.ts
interface ItemFilters {
  category: string | null;
  campus: string | null;
  minPrice: number | null;
  maxPrice: number | null;
  condition: string[];
  sort: 'newest' | 'price_asc' | 'price_desc';
}

interface ItemState {
  filters: ItemFilters;
  activeFilterCount: number;  // computed
  setFilter: <K extends keyof ItemFilters>(key: K, value: ItemFilters[K]) => void;
  resetFilters: () => void;
}
```

### 3.3 Chat Store (reference for Jiahai)

Defined in Jiahai's spec — `useChatStore` manages chat list + unread count.

---

## 4. API Client

```typescript
// src/services/apiClient.ts
import axios from 'axios';
import * as SecureStore from 'expo-secure-store';
import { useAuthStore } from '../stores/authStore';

const API_BASE_URL = process.env.EXPO_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 15000,
  headers: { 'Content-Type': 'application/json' },
});

// Request interceptor: attach JWT
apiClient.interceptors.request.use(async (config) => {
  const token = await SecureStore.getItemAsync('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Response interceptor: handle 401 → refresh token
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      await useAuthStore.getState().refreshAuth();
      const newToken = await SecureStore.getItemAsync('token');
      originalRequest.headers.Authorization = `Bearer ${newToken}`;
      return apiClient(originalRequest);
    }
    return Promise.reject(error);
  }
);
```

---

## 5. TypeScript Types

```typescript
// src/types/index.ts

export interface User {
  id: string;
  email: string;
  username: string;
  university: string;
  campus: string | null;
  avatarUrl: string | null;
  ratingAvg: number;
  isVerified: boolean;
  createdAt: string;
}

export interface Item {
  id: string;
  sellerId: string;
  title: string;
  description: string | null;
  category: 'textbook' | 'electronics' | 'furniture' | 'daily' | 'other';
  price: number;          // cents
  courseCode: string | null;
  condition: 'like_new' | 'good' | 'fair' | 'worn';
  campusLocation: string;
  meetupPoint: string | null;
  status: 'available' | 'reserved' | 'sold';
  viewCount: number;
  images: ItemImage[];
  createdAt: string;
  updatedAt: string;
}

export interface ItemImage {
  id: string;
  url: string;
  isPrimary: boolean;
}

export interface Chat {
  id: string;
  participants: string[];
  itemId: string;
  itemTitle: string;
  itemPrice: number;
  lastMessage: string | null;
  lastMessageAt: string | null;
  otherUser: { id: string; username: string; avatarUrl: string | null };
  unread: boolean;
}

export interface Message {
  id: string;
  senderId: string;
  text: string;
  createdAt: string;
}

export interface Review {
  id: string;
  reviewerId: string;
  revieweeId: string;
  transactionId: string;
  rating: number;        // 1–5
  comment: string | null;
  createdAt: string;
}

// Request types
export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  email: string;
  username: string;
  password: string;
  university: string;
  campus?: string;
}

export interface CreateItemRequest {
  title: string;
  description?: string;
  category: string;
  price: number;
  courseCode?: string;
  condition: string;
  campusLocation: string;
  meetupPoint?: string;
  imageUrls: string[];
}
```

---

## 6. Key Screen Implementations (Pseudocode)

### 6.1 HomeScreen

```
HomeScreen
├── TopBar: "SG CampusSwap" + Campus picker dropdown
├── SearchBar: sticky on scroll, tap → navigate to search tab
├── CategoryChips: horizontal ScrollView, tap → filter
├── ItemFeed: FlatList
│   ├── Pull-to-refresh
│   ├── Infinite scroll (onEndReached → fetch next page via useInfiniteQuery)
│   ├── ItemCard: thumbnail + title + price + campus + rating
│   │   └── onPress → router.push(`/item/${id}`)
│   └── Empty: illustration + "No items yet"
│
└── States: Loading (skeleton), Error (retry), Empty
```

### 6.2 ItemDetailScreen

```
ItemDetailScreen
├── ImageCarousel: paging FlatList, horizontal
├── Price (accent, H1) + Map icon (→ meetup point)
├── Title (H1) + Category chip + Condition chip
├── Description section
├── Seller card (avatar + name + rating, tappable → profile/[id])
├── Meetup point card (location icon + address, tappable → maps)
├── Listed date + view count
└── CTA: "Chat with Seller" (primary button, full width)
    └── onPress → create/find chat → navigate to chat/[id]
```

### 6.3 CreateListingScreen

```
CreateListingScreen
├── ImagePicker: grid 4 cells, tap + to open expo-image-picker
│   └── Max 5 images, show delete X on each thumbnail
├── Title TextInput (required)
├── Category dropdown (required)
├── Description TextInput (multiline, optional)
├── Row: CourseCode TextInput + Price TextInput (required)
├── Condition dropdown (required)
├── Campus dropdown (pre-filled from user profile)
├── MeetupPoint TextInput (optional)
└── Post button (disabled until: ≥1 image + title + category + price + condition)
    └── onPress: upload images → create item → navigate to item/[id]
```

---

## 7. Auth Flow Screens

### LoginScreen
- Logo + app name
- Email + Password TextInputs
- "Login" button → authStore.login()
- "Register" link → navigate to register
- States: idle, loading (button spinner), error (inline message)

### RegisterScreen
- Username, Email, University (dropdown), Campus (dropdown), Password, Confirm Password
- Domain hint below email input
- "Register" button → authStore.register()
- States: validation errors (inline), loading, success → navigate to verify-email

### EmailVerificationScreen
- 6-digit code input (auto-advancing)
- "Resend code" with 30s countdown
- Auto-verify on 6th digit → authStore.verifyEmail()
- States: empty, partial, verifying, error (shake + "Invalid code"), success → navigate to Home

---

## 8. Literature Review (Renxian)

### Source 1: Cross-Platform Mobile Development
**Citation**: Biørn-Hansen, A., Grønli, T. M., & Ghinea, G. (2019). A survey and taxonomy of cross-platform mobile development approaches. *ACM Computing Surveys*, 51(5), 1–36.
**Relevance**: React Native (Expo) vs Flutter vs native — validates Expo choice for team with web React experience, rapid prototyping, and OTA update capability.

### Source 2: State Management in React Native
**Citation**: Daityari, S. (2023). Comparing Zustand, Redux, and Context API for mobile state management. *React Summit 2023 Proceedings*.
**Relevance**: Zustand chosen for minimal boilerplate, no Provider wrapper needed, built-in TypeScript support, smaller bundle than Redux Toolkit.

### Source 3: Mobile Navigation UX Patterns
**Citation**: Pernice, K. (2022). Bottom navigation and tab design on mobile. *Nielsen Norman Group*.
**Relevance**: 5-tab design (Home, Search, Sell, Chats, Me) validated — visual navigation outperforms hamburger menus. Center FAB for primary action (Sell) increases engagement.

---

### 📦 Package.json (key dependencies)

```json
{
  "dependencies": {
    "expo": "~51.0.0",
    "expo-router": "~3.5.0",
    "expo-image-picker": "~15.0.0",
    "expo-secure-store": "~13.0.0",
    "expo-notifications": "~0.28.0",
    "expo-constants": "~16.0.0",
    "expo-linking": "~6.3.0",
    "@react-navigation/native": "^6.1.0",
    "@react-navigation/bottom-tabs": "^6.5.0",
    "@react-navigation/native-stack": "^6.9.0",
    "react-native-paper": "^5.12.0",
    "react-native-screens": "~3.31.0",
    "react-native-safe-area-context": "4.10.0",
    "zustand": "^4.5.0",
    "@tanstack/react-query": "^5.50.0",
    "axios": "^1.7.0",
    "@react-native-firebase/app": "^20.0.0",
    "@react-native-firebase/firestore": "^20.0.0"
  }
}
```

---

> **Ready to implement**: All scaffold code, store definitions, type definitions, and screen specs are complete.  
> **Next**: Renxian to `npx create-expo-app` and push to `develop` branch by Friday W7.  
> **Dependency for Jiahai**: Stores + API client + navigation must be in place before Chat/Search/Profile screens can be built.
