'use client';

import { useEffect, useRef, useCallback } from 'react';
import { useItemStore } from '@/stores/item-store';
import { useFilterStore } from '@/stores/filter-store';
import ItemCard from '@/components/ItemCard';
import SearchBar from '@/components/SearchBar';
import CategoryChips from '@/components/CategoryChips';
import SkeletonCard from '@/components/SkeletonCard';

const CATEGORIES = [
  { key: null, label: 'All' },
  { key: 'textbook', label: 'Textbooks' },
  { key: 'electronics', label: 'Electronics' },
  { key: 'furniture', label: 'Furniture' },
  { key: 'daily_essentials', label: 'Daily' },
  { key: 'other', label: 'Other' },
];

export default function HomePage() {
  const { items, total, hasNext, isLoading, fetchItems, appendItems } = useItemStore();
  const { filters, setCategory } = useFilterStore();
  const sentinelRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    fetchItems(filters);
  }, [filters]);

  // Infinite scroll
  const handleIntersect = useCallback(
    (entries: IntersectionObserverEntry[]) => {
      if (entries[0].isIntersecting && hasNext && !isLoading) {
        appendItems(filters);
      }
    },
    [hasNext, isLoading, appendItems, filters],
  );

  useEffect(() => {
    const observer = new IntersectionObserver(handleIntersect, { rootMargin: '200px' });
    if (sentinelRef.current) observer.observe(sentinelRef.current);
    return () => observer.disconnect();
  }, [handleIntersect]);

  return (
    <div className="max-w-7xl mx-auto">
      {/* Page Header */}
      <div className="mb-6">
        <h1 className="text-2xl font-bold text-gray-900">Discover Items</h1>
        <p className="text-gray-500 mt-1">
          {total > 0 ? `${total} items available near your campus` : 'Loading items...'}
        </p>
      </div>

      {/* Search Bar + Categories */}
      <div className="space-y-4 mb-6">
        <SearchBar />
        <CategoryChips
          categories={CATEGORIES}
          active={filters.category || null}
          onChange={(key) => setCategory(key as any)}
        />
      </div>

      {/* Item Grid */}
      {isLoading && items.length === 0 ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          {Array.from({ length: 8 }).map((_, i) => (
            <SkeletonCard key={i} />
          ))}
        </div>
      ) : items.length === 0 ? (
        <div className="text-center py-20">
          <div className="text-6xl mb-4">📦</div>
          <h2 className="text-xl font-semibold text-gray-900 mb-2">No items yet</h2>
          <p className="text-gray-500 mb-6">Be the first to sell something on your campus!</p>
          <a
            href="/sell"
            className="inline-flex px-6 py-3 bg-blue-500 text-white rounded-lg font-medium hover:bg-blue-600 transition-colors"
          >
            Post Your First Listing
          </a>
        </div>
      ) : (
        <>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
            {items.map((item) => (
              <ItemCard key={item.id} item={item} />
            ))}
          </div>

          {/* Infinite scroll sentinel */}
          <div ref={sentinelRef} className="h-10 mt-4">
            {isLoading && (
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
                {Array.from({ length: 4 }).map((_, i) => (
                  <SkeletonCard key={i} />
                ))}
              </div>
            )}
          </div>
        </>
      )}
    </div>
  );
}
