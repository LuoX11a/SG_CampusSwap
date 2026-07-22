'use client';

import { useEffect, useState, Suspense } from 'react';
import { useSearchParams } from 'next/navigation';
import apiClient from '@/lib/api-client';
import ItemCard from '@/components/ItemCard';
import SearchBar from '@/components/SearchBar';
import SkeletonCard from '@/components/SkeletonCard';
import type { Item } from '@/lib/types';

export default function BrowsePage() {
  return (
    <Suspense fallback={<div className="p-4">Loading...</div>}>
      <BrowseContent />
    </Suspense>
  );
}

function BrowseContent() {
  const searchParams = useSearchParams();
  const query = searchParams.get('q') || '';
  const [results, setResults] = useState<Item[]>([]);
  const [total, setTotal] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!query) return;
    setIsLoading(true);
    setError(null);
    apiClient.get('/search', { params: { q: query, page_size: 24 } })
      .then((res) => {
        setResults(res.data.results.map(mapSearchItem));
        setTotal(res.data.total);
      })
      .catch((err) => {
        setError(err.response?.data?.detail || 'Search failed. Please try again.');
        setResults([]);
      })
      .finally(() => setIsLoading(false));
  }, [query]);

  return (
    <div className="max-w-7xl mx-auto">
      <div className="mb-6">
        <SearchBar initialValue={query} />
      </div>

      <h1 className="text-2xl font-bold text-gray-900 mb-1">
        {query ? `Results for "${query}"` : 'Browse All Items'}
      </h1>
      <p className="text-gray-500 mb-6">{total} items found</p>

      {error ? (
        <div className="text-center py-20">
          <div className="text-5xl mb-4">⚠️</div>
          <h2 className="text-xl font-semibold text-gray-900 mb-2">Search failed</h2>
          <p className="text-gray-500 mb-4">{error}</p>
          <button onClick={() => window.location.reload()} className="px-4 py-2 bg-blue-500 text-white rounded-lg text-sm hover:bg-blue-600">Retry</button>
        </div>
      ) : isLoading ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          {Array.from({ length: 8 }).map((_, i) => <SkeletonCard key={i} />)}
        </div>
      ) : results.length === 0 ? (
        <div className="text-center py-20">
          <h2 className="text-xl font-semibold text-gray-900 mb-2">No results found</h2>
          <p className="text-gray-500">Try a different search term or browse categories.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          {results.map((item) => <ItemCard key={item.id} item={item} />)}
        </div>
      )}
    </div>
  );
}

function mapSearchItem(raw: any): Item {
  return {
    id: raw.id, title: raw.title, description: '', category: raw.category,
    price: raw.price, condition: raw.condition, courseCode: null,
    campusLocation: raw.campus_location, meetupPoint: '', status: raw.status,
    viewCount: 0, createdAt: raw.created_at, updatedAt: '',
    seller: { id: '', username: raw.seller_name, avatarUrl: null, university: '', campus: '', ratingAvg: raw.seller_rating, ratingCount: 0 },
    images: raw.primary_image ? [raw.primary_image] : [],
    primaryImage: raw.primary_image,
  };
}
