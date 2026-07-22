'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { useAuthStore } from '@/stores/auth-store';
import apiClient from '@/lib/api-client';
import { formatPriceDisplay } from '@/lib/format';
import clsx from 'clsx';
import type { Item } from '@/lib/types';

interface ListingItem {
  id: string; title: string; price: number; status: string;
  primary_image: string | null; created_at: string; view_count: number;
}

export default function MyListingsPage() {
  const { user } = useAuthStore();
  const [listings, setListings] = useState<ListingItem[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<'active' | 'sold'>('active');

  const fetchMyListings = () => {
    setIsLoading(true);
    setError(null);
    apiClient.get('/users/me/listings', { params: { page_size: 50 } })
      .then(res => setListings(res.data.items || []))
      .catch(() => setError('Failed to load your listings.'))
      .finally(() => setIsLoading(false));
  };

  useEffect(() => { fetchMyListings(); }, []);
  useEffect(() => { fetchMyListings(); }, [activeTab]);

  const filtered = activeTab === 'active'
    ? listings.filter((i) => i.status === 'available' || i.status === 'reserved')
    : listings.filter((i) => i.status === 'sold');

  const handleDelete = async (id: string) => {
    if (confirm('Delete this listing?')) {
      await apiClient.delete(`/items/${id}`);
      setListings(prev => prev.filter(i => i.id !== id));
    }
  };

  const handleMarkSold = async (id: string) => {
    await apiClient.patch(`/items/${id}/status`, null, { params: { new_status: 'sold' } });
    setListings(prev => prev.map(i => i.id === id ? { ...i, status: 'sold' } : i));
  };

  return (
    <div className="max-w-5xl mx-auto">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">My Listings</h1>

      {/* Tabs */}
      <div className="flex gap-1 mb-6 bg-gray-100 rounded-lg p-1 w-fit">
        {(['active', 'sold'] as const).map((tab) => (
          <button key={tab} onClick={() => setActiveTab(tab)}
            className={clsx('px-4 py-1.5 rounded-md text-sm font-medium transition-colors capitalize',
              activeTab === tab ? 'bg-white text-gray-900 shadow-sm' : 'text-gray-500 hover:text-gray-700')}>
            {tab}
          </button>
        ))}
      </div>

      {isLoading ? (
        <div className="space-y-3">
          {Array.from({ length: 3 }).map((_, i) => (
            <div key={i} className="bg-white rounded-lg border border-gray-200 p-4 animate-pulse">
              <div className="flex gap-4"><div className="w-32 h-24 bg-gray-200 rounded" /><div className="flex-1 space-y-2"><div className="h-4 bg-gray-200 rounded w-2/3" /><div className="h-5 bg-gray-100 rounded w-1/3" /></div></div>
            </div>
          ))}
        </div>
      ) : error ? (
        <div className="text-center py-20">
          <div className="text-5xl mb-4">⚠️</div><p className="text-gray-500">{error}</p>
          <button onClick={fetchMyListings} className="mt-4 px-4 py-2 bg-blue-500 text-white rounded-lg text-sm">Retry</button>
        </div>
      ) : filtered.length === 0 ? (
        <div className="text-center py-20 bg-white rounded-lg border border-gray-200">
          <div className="text-6xl mb-4">📦</div>
          <h2 className="text-xl font-semibold text-gray-900 mb-2">
            {activeTab === 'active' ? 'No active listings' : 'No sold items'}
          </h2>
          <p className="text-gray-500 mb-4">
            {activeTab === 'active' ? 'Post your first listing to start selling!' : 'Items you mark as sold will appear here.'}
          </p>
          {activeTab === 'active' && (
            <Link href="/sell" className="inline-flex px-6 py-2.5 bg-blue-500 text-white rounded-lg font-medium hover:bg-blue-600 transition-colors">
              Create Listing
            </Link>
          )}
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {filtered.map((item) => (
            <div key={item.id} className="bg-white rounded-lg border border-gray-200 overflow-hidden">
              <div className="h-44 bg-gray-100 flex items-center justify-center relative">
                {item.primary_image ? (
                  <img src={item.primary_image} alt={item.title} className="w-full h-full object-cover" loading="lazy" />
                ) : (
                  <span className="text-gray-400 text-3xl">📦</span>
                )}
                <span className={clsx('absolute top-2 right-2 px-2 py-0.5 rounded text-xs font-semibold text-white',
                  item.status === 'available' ? 'bg-green-500' : item.status === 'reserved' ? 'bg-amber-500' : 'bg-gray-500')}>
                  {item.status.toUpperCase()}
                </span>
              </div>
              <div className="p-4">
                <Link href={`/item/${item.id}`} className="font-semibold text-gray-900 hover:text-blue-500 line-clamp-1">{item.title}</Link>
                <p className="text-lg font-bold text-amber-500 mt-1">{formatPriceDisplay(item.price)}</p>
                <div className="flex gap-2 mt-3">
                  <Link href={`/item/${item.id}`}
                    className="flex-1 text-center py-1.5 border border-gray-200 rounded text-sm text-gray-600 hover:bg-gray-50 transition-colors">
                    View
                  </Link>
                  {item.status !== 'sold' && (
                    <button onClick={() => handleMarkSold(item.id)}
                      className="flex-1 py-1.5 bg-green-500 text-white rounded text-sm hover:bg-green-600 transition-colors">
                      Mark Sold
                    </button>
                  )}
                  <button onClick={() => handleDelete(item.id)}
                    className="py-1.5 px-3 border border-red-200 text-red-500 rounded text-sm hover:bg-red-50 transition-colors">
                    Delete
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
