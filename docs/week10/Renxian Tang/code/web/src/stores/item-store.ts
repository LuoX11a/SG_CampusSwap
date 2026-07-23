/**
 * Item Store �?Zustand
 *
 * Manages item listing data:
 * - Item list with pagination
 * - Current item detail
 * - Loading/error states
 */

import { create } from 'zustand';
import apiClient from '@/lib/api-client';
import type { Item, ItemCreate, ItemFilters } from '@/lib/types';

interface ItemState {
  items: Item[];
  currentItem: Item | null;
  total: number;
  page: number;
  hasNext: boolean;
  isLoading: boolean;
  error: string | null;

  // Actions
  fetchItems: (filters?: ItemFilters, page?: number) => Promise<void>;
  fetchItem: (id: string) => Promise<void>;
  createItem: (data: ItemCreate) => Promise<Item>;
  updateItem: (id: string, data: Partial<ItemCreate>) => Promise<void>;
  deleteItem: (id: string) => Promise<void>;
  markStatus: (id: string, status: string) => Promise<void>;
  appendItems: (filters?: ItemFilters) => Promise<void>; // Infinite scroll
}

export const useItemStore = create<ItemState>((set, get) => ({
  items: [],
  currentItem: null,
  total: 0,
  page: 1,
  hasNext: false,
  isLoading: false,
  error: null,

  fetchItems: async (filters?: ItemFilters, page = 1) => {
    set({ isLoading: true, error: null });
    try {
      const params: Record<string, any> = { page, page_size: 20 };
      if (filters?.category) params.category = filters.category;
      if (filters?.condition) params.condition = filters.condition;
      if (filters?.campus) params.campus = filters.campus;
      if (filters?.minPrice != null) params.min_price = filters.minPrice;
      if (filters?.maxPrice != null) params.max_price = filters.maxPrice;
      if (filters?.sort) params.sort = filters.sort;

      const res = await apiClient.get('/items', { params });
      set({
        items: res.data.items.map(mapItem),
        total: res.data.total,
        page: res.data.page,
        hasNext: res.data.has_next,
        isLoading: false,
      });
    } catch (err: any) {
      set({ isLoading: false, error: err.response?.data?.detail || 'Failed to load items' });
    }
  },

  appendItems: async (filters?: ItemFilters) => {
    const { page, hasNext, isLoading, items } = get();
    if (!hasNext || isLoading) return;

    set({ isLoading: true });
    try {
      const nextPage = page + 1;
      const params: Record<string, any> = { page: nextPage, page_size: 20 };
      if (filters?.category) params.category = filters.category;
      if (filters?.sort) params.sort = filters.sort;

      const res = await apiClient.get('/items', { params });
      set({
        items: [...items, ...res.data.items.map(mapItem)],
        total: res.data.total,
        page: res.data.page,
        hasNext: res.data.has_next,
        isLoading: false,
      });
    } catch {
      set({ isLoading: false });
    }
  },

  fetchItem: async (id: string) => {
    set({ isLoading: true, error: null });
    try {
      const res = await apiClient.get(`/items/${id}`);
      set({ currentItem: mapItem(res.data), isLoading: false });
    } catch (err: any) {
      set({ isLoading: false, error: 'Item not found' });
    }
  },

  createItem: async (data: ItemCreate) => {
    const res = await apiClient.post('/items', {
      title: data.title,
      description: data.description,
      category: data.category,
      price: data.price,
      condition: data.condition,
      course_code: data.courseCode,
      campus_location: data.campusLocation,
      meetup_point: data.meetupPoint,
      image_urls: data.imageUrls,
    });
    return mapItem(res.data);
  },

  updateItem: async (id: string, data: Partial<ItemCreate>) => {
    await apiClient.put(`/items/${id}`, data);
    get().fetchItem(id);
  },

  deleteItem: async (id: string) => {
    await apiClient.delete(`/items/${id}`);
    set((state) => ({ items: state.items.filter((i) => i.id !== id) }));
  },

  markStatus: async (id: string, status: string) => {
    await apiClient.patch(`/items/${id}/status?new_status=${status}`);
    get().fetchItem(id);
  },
}));

// ─── Helper ────────────────────────────────────────────

function mapItem(raw: any): Item {
  return {
    id: raw.id,
    title: raw.title,
    description: raw.description,
    category: raw.category,
    price: raw.price,
    condition: raw.condition,
    courseCode: raw.course_code,
    campusLocation: raw.campus_location,
    meetupPoint: raw.meetup_point,
    status: raw.status,
    viewCount: raw.view_count,
    createdAt: raw.created_at,
    updatedAt: raw.updated_at,
    seller: {
      id: raw.seller?.id,
      username: raw.seller?.username,
      avatarUrl: raw.seller?.avatar_url,
      university: raw.seller?.university,
      campus: raw.seller?.campus,
      ratingAvg: raw.seller?.rating_avg,
      ratingCount: raw.seller?.rating_count,
    },
    images: raw.images || [],
    primaryImage: raw.primary_image,
  };
}
