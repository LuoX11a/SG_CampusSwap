// ─── User ────────────────────────────────────────────
export interface User {
  id: string;
  email: string;
  username: string;
  university: string;
  campus: string;
  avatarUrl: string | null;
  ratingAvg: number | null;
  ratingCount: number;
  isVerified: boolean;
  memberSince: string;
}

export interface UserProfile {
  id: string;
  username: string;
  university: string;
  campus: string;
  avatarUrl: string | null;
  ratingAvg: number | null;
  ratingCount: number;
  memberSince: string;
  activeListingsCount: number;
}

// ─── Auth ────────────────────────────────────────────
export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  username: string;
  email: string;
  university: string;
  campus: string;
  password: string;
  confirmPassword: string;
}

export interface TokenResponse {
  accessToken: string;
  refreshToken: string;
  tokenType: string;
  expiresIn: number;
}

// ─── Item ─────────────────────────────────────────────
export enum ItemCategory {
  TEXTBOOK = 'textbook',
  ELECTRONICS = 'electronics',
  FURNITURE = 'furniture',
  DAILY_ESSENTIALS = 'daily_essentials',
  OTHER = 'other',
}

export enum ItemCondition {
  LIKE_NEW = 'like_new',
  GOOD = 'good',
  FAIR = 'fair',
  WORN = 'worn',
}

export enum ItemStatus {
  AVAILABLE = 'available',
  RESERVED = 'reserved',
  SOLD = 'sold',
}

export interface SellerInfo {
  id: string;
  username: string;
  avatarUrl: string | null;
  university: string;
  campus: string;
  ratingAvg: number | null;
  ratingCount: number;
}

export interface Item {
  id: string;
  title: string;
  description: string;
  category: ItemCategory;
  price: number;
  condition: ItemCondition;
  courseCode: string | null;
  campusLocation: string;
  meetupPoint: string;
  status: ItemStatus;
  viewCount: number;
  createdAt: string;
  updatedAt: string;
  seller: SellerInfo;
  images: string[];
  primaryImage: string | null;
}

export interface ItemCreate {
  title: string;
  description: string;
  category: ItemCategory;
  price: number;
  condition: ItemCondition;
  courseCode?: string;
  campusLocation: string;
  meetupPoint: string;
  imageUrls: string[];
}

export interface ItemFilters {
  category?: ItemCategory;
  condition?: ItemCondition;
  campus?: string;
  minPrice?: number;
  maxPrice?: number;
  sort: 'newest' | 'oldest' | 'price_asc' | 'price_desc' | 'popular';
}

// ─── Search ───────────────────────────────────────────
export interface SearchResult {
  id: string;
  title: string;
  price: number;
  category: string;
  condition: string;
  campusLocation: string;
  status: string;
  createdAt: string;
  sellerName: string;
  sellerRating: number | null;
  primaryImage: string | null;
  relevance: number;
}

// ─── Reviews ──────────────────────────────────────────
export interface Review {
  id: string;
  reviewer: { id: string; username: string; avatarUrl: string | null };
  revieweeId: string;
  transactionId: string;
  rating: number; // 1-5
  comment: string;
  createdAt: string;
}

export interface RatingSummary {
  average: number;
  total: number;
  distribution: Record<string, number>;
}

// ─── Chat ─────────────────────────────────────────────
export interface ChatRoom {
  id: string;
  participants: string[];
  itemId?: string;
  itemTitle?: string;
  lastMessage: {
    text: string;
    senderId: string;
    sentAt: string;
  } | null;
}

export interface ChatMessage {
  id: string;
  senderId: string;
  text: string;
  imageUrl: string | null;
  sentAt: string;
  read: boolean;
}
