'use client';

import { useState } from 'react';
import { X } from 'lucide-react';
import { useFilterStore } from '@/stores/filter-store';
import clsx from 'clsx';

const CATEGORIES: { value: string; label: string }[] = [
  { value: 'textbook', label: '📚 Textbook' },
  { value: 'electronics', label: '💻 Electronics' },
  { value: 'furniture', label: '🪑 Furniture' },
  { value: 'daily', label: '🧴 Daily' },
  { value: 'other', label: '📦 Other' },
];

const CONDITIONS: { value: string; label: string }[] = [
  { value: 'like_new', label: 'Like New' },
  { value: 'good', label: 'Good' },
  { value: 'fair', label: 'Fair' },
  { value: 'worn', label: 'Worn' },
];

const SORT_OPTIONS = [
  { value: 'newest' as const, label: 'Newest First' },
  { value: 'price_asc' as const, label: 'Price: Low to High' },
  { value: 'price_desc' as const, label: 'Price: High to Low' },
  { value: 'popular' as const, label: 'Most Popular' },
];

interface FilterModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function FilterModal({ isOpen, onClose }: FilterModalProps) {
  const { filters, setCategory, setCondition, setPriceRange, setSort, resetFilters, activeCount } = useFilterStore();
  const [localMin, setLocalMin] = useState(filters.minPrice?.toString() || '');
  const [localMax, setLocalMax] = useState(filters.maxPrice?.toString() || '');

  if (!isOpen) return null;

  const handleApply = () => {
    setPriceRange(
      localMin ? parseInt(localMin) : undefined,
      localMax ? parseInt(localMax) : undefined,
    );
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-end">
      {/* Overlay */}
      <div className="absolute inset-0 bg-black/50" onClick={onClose} />

      {/* Panel */}
      <div className="relative w-full max-w-sm h-full bg-white shadow-xl overflow-y-auto">
        <div className="sticky top-0 bg-white border-b border-gray-200 px-6 py-4 flex items-center justify-between">
          <h2 className="text-lg font-semibold text-gray-900">Filters</h2>
          <button onClick={onClose} className="text-gray-400 hover:text-gray-600"><X size={20} /></button>
        </div>

        <div className="p-6 space-y-6">
          {/* Category */}
          <div>
            <h3 className="text-sm font-semibold text-gray-900 mb-3">Category</h3>
            <div className="flex flex-wrap gap-2">
              <button onClick={() => setCategory(undefined)}
                className={clsx('px-3 py-1.5 rounded-full text-sm font-medium transition-colors',
                  !filters.category ? 'bg-blue-500 text-white' : 'bg-gray-100 text-gray-600 hover:bg-gray-200')}>
                All
              </button>
              {CATEGORIES.map((c) => (
                <button key={c.value} onClick={() => setCategory(filters.category === c.value ? undefined : c.value)}
                  className={clsx('px-3 py-1.5 rounded-full text-sm font-medium transition-colors',
                    filters.category === c.value ? 'bg-blue-500 text-white' : 'bg-gray-100 text-gray-600 hover:bg-gray-200')}>
                  {c.label}
                </button>
              ))}
            </div>
          </div>

          {/* Condition */}
          <div>
            <h3 className="text-sm font-semibold text-gray-900 mb-3">Condition</h3>
            <div className="flex flex-wrap gap-2">
              {CONDITIONS.map((c) => (
                <button key={c.value} onClick={() => setCondition(filters.condition === c.value ? undefined : c.value)}
                  className={clsx('px-3 py-1.5 rounded-full text-sm font-medium transition-colors',
                    filters.condition === c.value ? 'bg-blue-500 text-white' : 'bg-gray-100 text-gray-600 hover:bg-gray-200')}>
                  {c.label}
                </button>
              ))}
            </div>
          </div>

          {/* Price Range */}
          <div>
            <h3 className="text-sm font-semibold text-gray-900 mb-3">Price Range (SGD)</h3>
            <div className="flex items-center gap-3">
              <input type="number" value={localMin} onChange={(e) => setLocalMin(e.target.value)}
                placeholder="Min" min="0"
                className="w-full h-10 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
              <span className="text-gray-400">—</span>
              <input type="number" value={localMax} onChange={(e) => setLocalMax(e.target.value)}
                placeholder="Max" min="0"
                className="w-full h-10 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
            </div>
          </div>

          {/* Sort */}
          <div>
            <h3 className="text-sm font-semibold text-gray-900 mb-3">Sort By</h3>
            <div className="space-y-2">
              {SORT_OPTIONS.map((opt) => (
                <label key={opt.value} className="flex items-center gap-3 cursor-pointer">
                  <input type="radio" name="sort" checked={filters.sort === opt.value}
                    onChange={() => setSort(opt.value)}
                    className="w-4 h-4 text-blue-500 focus:ring-blue-500" />
                  <span className="text-sm text-gray-700">{opt.label}</span>
                </label>
              ))}
            </div>
          </div>
        </div>

        {/* Actions */}
        <div className="sticky bottom-0 bg-white border-t border-gray-200 px-6 py-4 flex gap-3">
          <button onClick={resetFilters}
            className="flex-1 py-2.5 border border-gray-300 text-gray-700 rounded-lg font-medium text-sm hover:bg-gray-50 transition-colors">
            Reset
          </button>
          <button onClick={handleApply}
            className="flex-1 py-2.5 bg-blue-500 text-white rounded-lg font-medium text-sm hover:bg-blue-600 transition-colors">
            Apply {activeCount > 0 ? `(${activeCount})` : ''}
          </button>
        </div>
      </div>
    </div>
  );
}
