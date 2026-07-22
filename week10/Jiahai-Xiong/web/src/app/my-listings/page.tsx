'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { useItemStore } from '@/stores/item-store';
import { useAuthStore } from '@/stores/auth-store';
import { formatPriceDisplay } from '@/lib/format';
import clsx from 'clsx';

export default function MyListingsPage() {
  const { user } = useAuthStore();
  const { items, fetchItems, deleteItem, markStatus } = useItemStore();
  const [activeTab, setActiveTab] = useState<'active' | 'sold'>('active');

  useEffect(() => {
    fetchItems({ sort: 'newest' });
  }, []);

  const myItems = items.filter((i) => i.seller?.id === user?.id);
  const filtered = activeTab === 'active'
    ? myItems.filter((i) => i.status === 'available' || i.status === 'reserved')
    : myItems.filter((i) => i.status === 'sold');

  const handleDelete = async (id: string) => {
    if (confirm('Delete this listing?')) {
      await deleteItem(id);
    }
  };

  const handleMarkSold = async (id: string) => {
    await markStatus(id, 'sold');
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

      {filtered.length === 0 ? (
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
                {item.primaryImage ? (
                  <img src={item.primaryImage} alt={item.title} className="w-full h-full object-cover" />
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
