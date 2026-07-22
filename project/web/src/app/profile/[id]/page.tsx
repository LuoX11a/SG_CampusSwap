'use client';

import { useEffect, useState } from 'react';
import { useParams } from 'next/navigation';
import Link from 'next/link';
import { Star, MapPin, Calendar } from 'lucide-react';
import apiClient from '@/lib/api-client';
import type { UserProfile, Review } from '@/lib/types';
import { timeAgo } from '@/lib/format';

export default function PublicProfilePage() {
  const { id } = useParams<{ id: string }>();
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [reviews, setReviews] = useState<Review[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    if (!id) return;
    Promise.all([
      apiClient.get(`/users/${id}`).then(r => setProfile(r.data)),
      apiClient.get(`/reviews/user/${id}`).then(r => setReviews(r.data)),
    ]).finally(() => setIsLoading(false));
  }, [id]);

  if (isLoading) {
    return <div className="max-w-2xl mx-auto"><div className="h-48 skeleton rounded-lg" /></div>;
  }

  if (!profile) {
    return <div className="text-center py-20 text-gray-500">User not found.</div>;
  }

  return (
    <div className="max-w-2xl mx-auto">
      {/* Profile Header */}
      <div className="bg-white rounded-lg border border-gray-200 p-6 text-center">
        <div className="w-20 h-20 rounded-full bg-gray-300 flex items-center justify-center text-white text-2xl font-bold mx-auto">
          {profile.username.charAt(0).toUpperCase()}
        </div>
        <h1 className="text-xl font-bold text-gray-900 mt-3">{profile.username}</h1>
        <p className="text-sm text-gray-500 flex items-center justify-center gap-1 mt-1">
          <MapPin size={14} /> {profile.university} · {profile.campus}
        </p>
        <p className="text-xs text-gray-400 flex items-center justify-center gap-1 mt-1">
          <Calendar size={12} /> Member since {new Date(profile.memberSince).toLocaleDateString('en-SG', { year: 'numeric', month: 'long' })}
        </p>
        <div className="mt-3 flex items-center justify-center gap-1 text-amber-500">
          <Star size={18} className="fill-amber-400" />
          <span className="font-semibold">{profile.ratingAvg?.toFixed(1) || '—'}</span>
          <span className="text-gray-400 text-sm">({profile.ratingCount} reviews)</span>
        </div>
      </div>

      {/* Reviews */}
      <div className="mt-6">
        <h2 className="text-lg font-semibold text-gray-900 mb-3">Reviews</h2>
        {reviews.length === 0 ? (
          <p className="text-gray-400 text-sm">No reviews yet.</p>
        ) : (
          <div className="space-y-3">
            {reviews.map((review) => (
              <div key={review.id} className="bg-white rounded-lg border border-gray-200 p-4">
                <div className="flex items-start gap-3">
                  <div className="w-10 h-10 rounded-full bg-gray-300 flex items-center justify-center text-white font-bold text-sm shrink-0">
                    {review.reviewer.username.charAt(0)}
                  </div>
                  <div className="flex-1">
                    <div className="flex items-center justify-between">
                      <h3 className="font-medium text-sm text-gray-900">{review.reviewer.username}</h3>
                      <span className="text-xs text-gray-400">{timeAgo(review.createdAt)}</span>
                    </div>
                    <div className="flex items-center gap-0.5 mt-0.5 text-amber-400">
                      {Array.from({ length: 5 }).map((_, i) => (
                        <Star key={i} size={14} className={i < review.rating ? 'fill-amber-400' : 'text-gray-200'} />
                      ))}
                    </div>
                    <p className="text-sm text-gray-600 mt-2">{review.comment}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
