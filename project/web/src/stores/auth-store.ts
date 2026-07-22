/**
 * Auth Store — Zustand
 *
 * Manages authentication state across the app:
 * - Login / Register / Verify / Logout
 * - JWT token persistence
 * - Current user profile
 */

import { create } from 'zustand';

// Helper to extract a readable error message from API validation errors
function extractError(err: any, fallback: string): string {
  const detail = err?.response?.data?.detail;
  if (!detail) return fallback;
  if (Array.isArray(detail)) {
    return detail.map((e: any) => {
      const field = e.loc?.filter((l: string) => l !== 'body').join('.') || '';
      return field ? `${field}: ${e.msg}` : e.msg;
    }).join('; ');
  }
  return String(detail);
}
import apiClient, { setTokens, clearTokens, getAccessToken } from '@/lib/api-client';
import type { User, LoginRequest, RegisterRequest } from '@/lib/types';

interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;

  // Actions
  login: (data: LoginRequest) => Promise<void>;
  register: (data: RegisterRequest) => Promise<{ email: string }>;
  verifyEmail: (email: string, code: string) => Promise<void>;
  logout: () => Promise<void>;
  fetchMe: () => Promise<void>;
  clearError: () => void;
}

export const useAuthStore = create<AuthState>((set, get) => ({
  user: null,
  isAuthenticated: false,
  isLoading: false,
  error: null,

  login: async (data: LoginRequest) => {
    set({ isLoading: true, error: null });
    try {
      const res = await apiClient.post('/auth/login', data);
      setTokens(res.data.access_token, res.data.refresh_token);
      // Fetch user profile after login
      const meRes = await apiClient.get('/auth/me');
      set({
        user: {
          id: meRes.data.id,
          email: meRes.data.email,
          username: meRes.data.username,
          university: meRes.data.university,
          campus: meRes.data.campus,
          avatarUrl: meRes.data.avatar_url,
          ratingAvg: meRes.data.rating_avg,
          ratingCount: meRes.data.rating_count,
          isVerified: meRes.data.is_verified,
          memberSince: meRes.data.created_at || '',
        },
        isAuthenticated: true,
        isLoading: false,
      });
    } catch (err: any) {
      set({ isLoading: false, error: extractError(err, 'Login failed. Please try again.') });
      throw err;
    }
  },

  register: async (data: RegisterRequest) => {
    set({ isLoading: true, error: null });
    try {
      const res = await apiClient.post('/auth/register', data);
      set({ isLoading: false });
      return { email: res.data.email };
    } catch (err: any) {
      set({ isLoading: false, error: extractError(err, 'Registration failed.') });
      throw err;
    }
  },

  verifyEmail: async (email: string, code: string) => {
    set({ isLoading: true, error: null });
    try {
      await apiClient.post('/auth/verify', { email, code });
      set({ isLoading: false });
    } catch (err: any) {
      set({ isLoading: false, error: extractError(err, 'Verification failed.') });
      throw err;
    }
  },

  logout: async () => {
    try {
      const refreshToken = localStorage.getItem('sgcs_refresh_token');
      if (refreshToken) {
        await apiClient.post('/auth/logout', { refresh_token: refreshToken });
      }
    } catch {
      // Ignore logout errors
    } finally {
      clearTokens();
      set({ user: null, isAuthenticated: false });
    }
  },

  fetchMe: async () => {
    const token = getAccessToken();
    if (!token) return;

    set({ isLoading: true });
    try {
      const res = await apiClient.get('/auth/me');
      set({
        user: {
          id: res.data.id,
          email: res.data.email,
          username: res.data.username,
          university: res.data.university,
          campus: res.data.campus,
          avatarUrl: res.data.avatar_url,
          ratingAvg: res.data.rating_avg,
          ratingCount: res.data.rating_count,
          isVerified: res.data.is_verified,
          memberSince: res.data.created_at || '',
        },
        isAuthenticated: true,
        isLoading: false,
      });
    } catch {
      clearTokens();
      set({ user: null, isAuthenticated: false, isLoading: false });
    }
  },

  clearError: () => set({ error: null }),
}));
