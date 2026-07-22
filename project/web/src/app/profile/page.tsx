'use client';

import { useEffect } from 'react';
import Link from 'next/link';
import { Settings, Star, Package, MessageSquare, ChevronRight, LogOut } from 'lucide-react';
import { useAuthStore } from '@/stores/auth-store';
import { useItemStore } from '@/stores/item-store';

export default function ProfilePage() {
  const { user, isAuthenticated, fetchMe, logout } = useAuthStore();
  const { items, fetchItems } = useItemStore();

  useEffect(() => { fetchMe(); }, []);
  useEffect(() => {
    if (user) fetchItems({ sort: 'newest' }, 1);
  }, [user]);

  if (!isAuthenticated || !user) {
    return (
      <div className="text-center py-20">
        <h2 className="text-xl font-semibold text-gray-900 mb-2">Not signed in</h2>
        <Link href="/login" className="text-blue-500 hover:text-blue-600 font-medium">Sign in to view your profile</Link>
      </div>
    );
  }

  const myItems = items.filter((i) => i.seller?.id === user.id).slice(0, 5);

  return (
    <div className="max-w-2xl mx-auto">
      {/* Profile Header */}
      <div className="bg-white rounded-lg border border-gray-200 p-6 text-center">
        <div className="relative inline-block">
          <div className="w-20 h-20 rounded-full bg-gray-300 flex items-center justify-center text-white text-2xl font-bold mx-auto">
            {user.username.charAt(0).toUpperCase()}
          </div>
          <Link href="/profile/edit"
            className="absolute bottom-0 right-0 text-xs bg-white border border-gray-200 rounded-full px-2 py-0.5 text-gray-600 hover:bg-gray-50 shadow-sm">
            Edit
          </Link>
        </div>
        <h1 className="text-xl font-bold text-gray-900 mt-3">{user.username}</h1>
        <p className="text-sm text-gray-500">{user.email}</p>
        <p className="text-sm text-gray-400 mt-0.5">{user.university} · {user.campus}</p>
        <div className="mt-3 flex items-center justify-center gap-1 text-amber-500">
          <Star size={18} className="fill-amber-400" />
          <span className="font-semibold">{user.ratingAvg?.toFixed(1) || '—'}</span>
          <span className="text-gray-400 text-sm">({user.ratingCount} reviews)</span>
        </div>
      </div>

      {/* My Listings */}
      {myItems.length > 0 && (
        <div className="mt-6">
          <div className="flex justify-between items-center mb-3">
            <h2 className="text-lg font-semibold text-gray-900">My Listings</h2>
            <Link href="/my-listings" className="text-sm text-blue-500 hover:text-blue-600">View all</Link>
          </div>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
            {myItems.map((item) => (
              <Link key={item.id} href={`/item/${item.id}`}
                className="bg-white rounded-lg border border-gray-200 overflow-hidden hover:shadow-sm transition-shadow">
                <div className="h-28 bg-gray-100 flex items-center justify-center">
                  {item.primaryImage ? (
                    <img src={item.primaryImage} alt={item.title} className="w-full h-full object-cover" />
                  ) : (
                    <span className="text-gray-400 text-2xl">📦</span>
                  )}
                </div>
                <div className="p-2">
                  <p className="text-sm font-medium text-gray-900 truncate">{item.title}</p>
                  <p className="text-sm font-bold text-amber-500">${(item.price / 100).toFixed(2)}</p>
                </div>
              </Link>
            ))}
          </div>
        </div>
      )}

      {/* Quick Links */}
      <div className="mt-6 bg-white rounded-lg border border-gray-200 divide-y divide-gray-100">
        <Link href="/my-listings" className="flex items-center justify-between p-4 hover:bg-gray-50 transition-colors">
          <span className="flex items-center gap-3 text-sm"><Package size={20} className="text-gray-400" /> My Listings</span>
          <ChevronRight size={18} className="text-gray-300" />
        </Link>
        <Link href="/reviews" className="flex items-center justify-between p-4 hover:bg-gray-50 transition-colors">
          <span className="flex items-center gap-3 text-sm"><Star size={20} className="text-gray-400" /> My Reviews</span>
          <ChevronRight size={18} className="text-gray-300" />
        </Link>
        <Link href="/messages" className="flex items-center justify-between p-4 hover:bg-gray-50 transition-colors">
          <span className="flex items-center gap-3 text-sm"><MessageSquare size={20} className="text-gray-400" /> Messages</span>
          <ChevronRight size={18} className="text-gray-300" />
        </Link>
        <Link href="/settings" className="flex items-center justify-between p-4 hover:bg-gray-50 transition-colors">
          <span className="flex items-center gap-3 text-sm"><Settings size={20} className="text-gray-400" /> Settings</span>
          <ChevronRight size={18} className="text-gray-300" />
        </Link>
      </div>

      {/* Logout */}
      <button onClick={logout}
        className="w-full mt-4 py-3 text-red-500 hover:text-red-600 text-sm font-medium bg-white rounded-lg border border-gray-200 hover:bg-red-50 transition-colors">
        <span className="flex items-center justify-center gap-2"><LogOut size={16} /> Log Out</span>
      </button>
    </div>
  );
}
