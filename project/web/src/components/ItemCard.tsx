'use client';

import Link from 'next/link';
import { MapPin, Star } from 'lucide-react';
import type { Item } from '@/lib/types';
import { formatPrice, timeAgo, formatCategory, formatCondition } from '@/lib/format';

interface ItemCardProps {
  item: Item;
}

const STATUS_BADGES: Record<string, { label: string; className: string }> = {
  sold: { label: 'SOLD', className: 'bg-gray-500 text-white' },
  reserved: { label: 'RESERVED', className: 'bg-amber-500 text-white' },
};

export default function ItemCard({ item }: ItemCardProps) {
  const badge = STATUS_BADGES[item.status];

  return (
    <Link
      href={`/item/${item.id}`}
      className="block bg-white rounded-lg border border-gray-200 shadow-sm hover:shadow-md hover:-translate-y-0.5 transition-all duration-150 overflow-hidden"
    >
      {/* Image */}
      <div className="relative h-48 bg-gray-100">
        {item.primaryImage ? (
          <img
            src={item.primaryImage}
            alt={item.title}
            className="w-full h-full object-cover"
            loading="lazy"
          />
        ) : (
          <div className="w-full h-full flex items-center justify-center text-gray-400">
            <svg className="w-12 h-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
          </div>
        )}

        {/* Status Badge */}
        {badge && (
          <span className={`absolute top-2 right-2 px-2 py-0.5 rounded text-xs font-semibold ${badge.className}`}>
            {badge.label}
          </span>
        )}
      </div>

      {/* Content */}
      <div className="p-4">
        {/* Price */}
        <p className="text-xl font-bold text-amber-500">${formatPrice(item.price)}</p>

        {/* Title */}
        <h3 className="mt-1 text-base font-semibold text-gray-900 line-clamp-2 leading-snug">
          {item.title}
        </h3>

        {/* Category + Condition */}
        <div className="mt-2 flex items-center gap-2">
          <span className="inline-flex px-2 py-0.5 rounded-full text-xs font-medium bg-blue-50 text-blue-700">
            {formatCategory(item.category)}
          </span>
          <span className="inline-flex px-2 py-0.5 rounded-full text-xs font-medium bg-green-50 text-green-700">
            {formatCondition(item.condition)}
          </span>
        </div>

        {/* Location + Rating */}
        <div className="mt-3 flex items-center justify-between text-sm text-gray-500">
          <span className="flex items-center gap-1 truncate">
            <MapPin size={14} />
            <span className="truncate">{item.campusLocation}</span>
          </span>
          {item.seller.ratingAvg != null && item.seller.ratingAvg > 0 && (
            <span className="flex items-center gap-1 shrink-0">
              <Star size={14} className="text-amber-400 fill-amber-400" />
              {item.seller.ratingAvg.toFixed(1)}
              <span className="text-gray-400">({item.seller.ratingCount})</span>
            </span>
          )}
        </div>

        {/* Timestamp */}
        <p className="mt-2 text-xs text-gray-400">{timeAgo(item.createdAt)}</p>
      </div>
    </Link>
  );
}
