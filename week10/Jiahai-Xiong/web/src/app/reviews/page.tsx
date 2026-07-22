'use client';

import { useState } from 'react';
import { Star } from 'lucide-react';
import type { Review, RatingSummary } from '@/lib/types';
import { timeAgo } from '@/lib/format';

const MOCK_SUMMARY: RatingSummary = { average: 4.5, total: 12, distribution: { '5': 8, '4': 3, '3': 1, '2': 0, '1': 0 } };
const MOCK_REVIEWS: Review[] = [
  { id: 'r1', reviewer: { id: 'u1', username: 'Jason Tan', avatarUrl: null }, revieweeId: 'me', transactionId: 't1', rating: 5, comment: 'Very friendly and punctual. Item exactly as described!', createdAt: new Date(Date.now() - 1209600000).toISOString() },
  { id: 'r2', reviewer: { id: 'u2', username: 'Mei Ling', avatarUrl: null }, revieweeId: 'me', transactionId: 't2', rating: 4, comment: 'Good seller, item was in decent condition. Would buy again.', createdAt: new Date(Date.now() - 2592000000).toISOString() },
  { id: 'r3', reviewer: { id: 'u3', username: 'Ryan Goh', avatarUrl: null }, revieweeId: 'me', transactionId: 't3', rating: 3, comment: 'Item was okay but had some wear not mentioned in listing.', createdAt: new Date(Date.now() - 5184000000).toISOString() },
];

export default function ReviewsPage() {
  const [summary] = useState<RatingSummary>(MOCK_SUMMARY);

  return (
    <div className="max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">My Reviews</h1>

      {/* Rating Summary */}
      <div className="bg-white rounded-lg border border-gray-200 p-6 mb-6">
        <div className="flex items-center gap-6">
          <div className="text-center">
            <p className="text-4xl font-bold text-gray-900">{summary.average.toFixed(1)}</p>
            <div className="flex items-center justify-center gap-0.5 mt-1 text-amber-400">
              {Array.from({ length: 5 }).map((_, i) => (
                <Star key={i} size={16} className={i < Math.round(summary.average) ? 'fill-amber-400' : 'text-gray-200'} />
              ))}
            </div>
            <p className="text-xs text-gray-400 mt-1">{summary.total} reviews</p>
          </div>
          <div className="flex-1 space-y-1">
            {[5, 4, 3, 2, 1].map((rating) => {
              const count = summary.distribution[String(rating)] || 0;
              const pct = summary.total > 0 ? (count / summary.total) * 100 : 0;
              return (
                <div key={rating} className="flex items-center gap-2 text-xs">
                  <span className="w-4 text-right text-gray-500">{rating}</span>
                  <Star size={12} className="text-amber-400 fill-amber-400" />
                  <div className="flex-1 h-2 bg-gray-100 rounded-full overflow-hidden">
                    <div className="h-full bg-amber-400 rounded-full transition-all" style={{ width: `${pct}%` }} />
                  </div>
                  <span className="w-6 text-gray-400">{count}</span>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Review Cards */}
      <div className="space-y-3">
        {MOCK_REVIEWS.map((review) => (
          <div key={review.id} className="bg-white rounded-lg border border-gray-200 p-4">
            <div className="flex items-start gap-3">
              <div className="w-10 h-10 rounded-full bg-gray-300 flex items-center justify-center text-white font-bold text-sm shrink-0">
                {review.reviewer.username.charAt(0)}
              </div>
              <div className="flex-1 min-w-0">
                <div className="flex items-center justify-between">
                  <h3 className="font-medium text-sm text-gray-900">{review.reviewer.username}</h3>
                  <span className="text-xs text-gray-400">{timeAgo(review.createdAt)}</span>
                </div>
                <div className="flex items-center gap-0.5 mt-0.5 text-amber-400">
                  {Array.from({ length: 5 }).map((_, i) => (
                    <Star key={i} size={14} className={i < review.rating ? 'fill-amber-400' : 'text-gray-200'} />
                  ))}
                </div>
                <p className="text-sm text-gray-600 mt-2 leading-relaxed">{review.comment}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
