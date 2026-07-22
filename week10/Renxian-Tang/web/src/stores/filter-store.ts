import { create } from 'zustand';
import type { ItemFilters, ItemCategory, ItemCondition } from '@/lib/types';

interface FilterState {
  filters: ItemFilters;
  setCategory: (category?: ItemCategory) => void;
  setCondition: (condition?: ItemCondition) => void;
  setCampus: (campus?: string) => void;
  setPriceRange: (min?: number, max?: number) => void;
  setSort: (sort: ItemFilters['sort']) => void;
  resetFilters: () => void;
  activeCount: number;
}

const DEFAULT_FILTERS: ItemFilters = { sort: 'newest' };

export const useFilterStore = create<FilterState>((set, get) => ({
  filters: { ...DEFAULT_FILTERS },

  setCategory: (category) =>
    set((s) => ({ filters: { ...s.filters, category } })),

  setCondition: (condition) =>
    set((s) => ({ filters: { ...s.filters, condition } })),

  setCampus: (campus) =>
    set((s) => ({ filters: { ...s.filters, campus } })),

  setPriceRange: (min, max) =>
    set((s) => ({ filters: { ...s.filters, minPrice: min, maxPrice: max } })),

  setSort: (sort) =>
    set((s) => ({ filters: { ...s.filters, sort } })),

  resetFilters: () => set({ filters: { ...DEFAULT_FILTERS } }),

  get activeCount() {
    const f = get().filters;
    let count = 0;
    if (f.category) count++;
    if (f.condition) count++;
    if (f.campus) count++;
    if (f.minPrice != null || f.maxPrice != null) count++;
    return count;
  },
}));
