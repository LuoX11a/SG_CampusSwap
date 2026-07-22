'use client';

import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import { ChevronLeft, MapPin, Star, MessageCircle } from 'lucide-react';
import { useItemStore } from '@/stores/item-store';
import { useAuthStore } from '@/stores/auth-store';
import SkeletonCard from '@/components/SkeletonCard';
import { formatPriceDisplay, formatCategory, formatCondition, timeAgo } from '@/lib/format';

export default function ItemDetailPage() {
  const { id } = useParams<{ id: string }>();
  const { currentItem, isLoading, fetchItem } = useItemStore();
  const { user } = useAuthStore();
  const router = useRouter();
  const [activeImage, setActiveImage] = useState(0);

  useEffect(() => {
    if (id) fetchItem(id);
  }, [id]);

  if (isLoading || !currentItem) {
    return <div className="max-w-5xl mx-auto"><SkeletonCard /></div>;
  }

  const item = currentItem;
  const isOwner = user?.id === item.seller.id;

  return (
    <div className="max-w-5xl mx-auto">
      {/* Back */}
      <button onClick={() => router.back()} className="flex items-center gap-1 text-gray-500 hover:text-gray-700 mb-4 text-sm">
        <ChevronLeft size={18} /> Back
      </button>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {/* Image Gallery */}
        <div>
          <div className="bg-gray-100 rounded-lg overflow-hidden h-96 flex items-center justify-center">
            {item.images.length > 0 ? (
              <img src={item.images[activeImage]} alt={item.title} className="w-full h-full object-contain" />
            ) : (
              <span className="text-gray-400 text-6xl">📷</span>
            )}
          </div>
          {item.images.length > 1 && (
            <div className="flex gap-2 mt-3 overflow-x-auto">
              {item.images.map((img, i) => (
                <button key={i} onClick={() => setActiveImage(i)}
                  className={`shrink-0 w-16 h-16 rounded-lg border-2 overflow-hidden ${i === activeImage ? 'border-blue-500' : 'border-gray-200'}`}>
                  <img src={img} alt="" className="w-full h-full object-cover" />
                </button>
              ))}
            </div>
          )}
        </div>

        {/* Info */}
        <div>
          <h1 className="text-2xl font-bold text-gray-900">{item.title}</h1>
          <p className="text-3xl font-bold text-amber-500 mt-3">{formatPriceDisplay(item.price)}</p>

          <div className="flex gap-2 mt-3">
            <span className="px-3 py-1 rounded-full text-sm font-medium bg-blue-50 text-blue-700">{formatCategory(item.category)}</span>
            <span className="px-3 py-1 rounded-full text-sm font-medium bg-green-50 text-green-700">{formatCondition(item.condition)}</span>
          </div>

          <div className="mt-6">
            <h2 className="text-sm font-semibold text-gray-900 mb-2">Description</h2>
            <p className="text-gray-600 text-sm leading-relaxed whitespace-pre-wrap">{item.description}</p>
          </div>

          {item.courseCode && (
            <div className="mt-4">
              <span className="text-sm text-gray-500">Course Code:</span>
              <span className="ml-2 text-sm font-medium text-gray-900">{item.courseCode}</span>
            </div>
          )}

          <div className="mt-6 flex items-center gap-2 text-sm text-gray-500">
            <MapPin size={16} /> {item.campusLocation} · {item.meetupPoint}
          </div>

          <hr className="my-6" />

          {/* Seller */}
          <Link href={`/profile/${item.seller.id}`} className="flex items-center gap-3 p-3 rounded-lg hover:bg-gray-50 transition-colors -mx-3">
            <div className="w-12 h-12 rounded-full bg-gray-300 flex items-center justify-center text-white font-bold">
              {item.seller.username.charAt(0).toUpperCase()}
            </div>
            <div>
              <p className="font-medium text-gray-900">{item.seller.username}</p>
              <p className="text-sm text-gray-500">{item.seller.university} · {item.seller.campus}</p>
              {item.seller.ratingAvg && (
                <p className="text-sm flex items-center gap-1 text-amber-500">
                  <Star size={14} className="fill-amber-400" /> {item.seller.ratingAvg.toFixed(1)} ({item.seller.ratingCount} reviews)
                </p>
              )}
            </div>
          </Link>

          {/* CTA */}
          <div className="mt-6 space-y-3">
            {isOwner ? (
              <div className="flex gap-3">
                <button onClick={() => router.push(`/sell?edit=${item.id}`)}
                  className="flex-1 py-3 border border-gray-300 text-gray-700 rounded-lg font-medium hover:bg-gray-50 transition-colors">Edit</button>
                <button onClick={() => useItemStore.getState().markStatus(item.id, 'sold')}
                  className="flex-1 py-3 bg-green-500 text-white rounded-lg font-medium hover:bg-green-600 transition-colors">Mark as Sold</button>
              </div>
            ) : (
              <button onClick={() => router.push(`/messages?item=${item.id}&seller=${item.seller.id}`)}
                className="w-full py-3 bg-blue-500 text-white rounded-lg font-medium hover:bg-blue-600 transition-colors flex items-center justify-center gap-2">
                <MessageCircle size={20} /> Chat with Seller
              </button>
            )}
          </div>

          <p className="mt-4 text-xs text-gray-400">
            Listed {timeAgo(item.createdAt)} · {item.viewCount} views · Status: {item.status}
          </p>
        </div>
      </div>
    </div>
  );
}
