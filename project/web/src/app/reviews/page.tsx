'use client';

import { useEffect, useState } from 'react';
import { Star } from 'lucide-react';
import { useAuthStore } from '@/stores/auth-store';
import apiClient from '@/lib/api-client';
import type { Review, RatingSummary } from '@/lib/types';
import { timeAgo } from '@/lib/format';

export default function ReviewsPage() {
  const { user } = useAuthStore();
  const [summary, setSummary] = useState<RatingSummary | null>(null);
  const [reviews, setReviews] = useState<Review[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!user) { setIsLoading(false); return; }
    setIsLoading(true);
    setError(null);
    Promise.all([
      apiClient.get(`/reviews/rating-summary/${user.id}`).then(r => r.data).catch(() => null),
      apiClient.get(`/reviews/user/${user.id}`).then(r => r.data).catch(() => []),
    ]).then(([summaryData, reviewsData]) => {
      setSummary(summaryData);
      setReviews(Array.isArray(reviewsData) ? reviewsData : reviewsData?.items || []);
    }).catch(() => {
      setError('Failed to load reviews.');
    }).finally(() => setIsLoading(false));
  }, [user]);

  if (!user) {
    return (
      <div className="text-center py-20 text-gray-500">
        <div className="text-5xl mb-4">🔒</div>
        <p className="text-lg">Please sign in to view reviews.</p>
      </div>
    );
  }

  if (isLoading) {
    return (
      <div className="max-w-2xl mx-auto">
        <h1 className="text-2xl font-bold text-gray-900 mb-6">My Reviews</h1>
        <div className="bg-white rounded-lg border border-gray-200 p-6 animate-pulse space-y-4">
          <div className="flex gap-6">
            <div className="w-20 h-20 bg-gray-200 rounded" />
            <div className="flex-1 space-y-2">
              {Array.from({ length: 5 }).map((_, i) => (
                <div key={i} className="h-3 bg-gray-100 rounded w-full" />
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="max-w-2xl mx-auto text-center py-20">
        <div className="text-5xl mb-4">⚠️</div>
        <h2 className="text-lg font-semibold text-gray-900 mb-2">{error}</h2>
        <button onClick={() => window.location.reload()} className="mt-4 px-4 py-2 bg-blue-500 text-white rounded-lg text-sm hover:bg-blue-600">Retry</button>
      </div>
    );
  }

  return (
    <div className="max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">My Reviews</h1>

      {/* Rating Summary */}
      {summary && (
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

        </div>
      </div>
      )}

      {/* Review Cards */}
      {reviews.length === 0 ? (
        <div className="text-center py-16 bg-white rounded-lg border border-gray-200">
          <div className="text-4xl mb-3">⭐</div>
          <p className="text-gray-500">No reviews yet. Complete a transaction to receive reviews.</p>
        </div>
      ) : (
        <div className="space-y-3">
          {reviews.map((review) => (
            <div key={review.id} className="bg-white rounded-lg border border-gray-200 p-4">
              <div className="flex items-start gap-3">
                <div className="w-10 h-10 rounded-full bg-blue-500 flex items-center justify-center text-white font-bold text-sm shrink-0">
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
      )}
    </div>
  );
}
