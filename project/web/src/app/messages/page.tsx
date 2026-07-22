'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { useAuthStore } from '@/stores/auth-store';
import apiClient from '@/lib/api-client';
import type { ChatRoom } from '@/lib/types';
import { timeAgo } from '@/lib/format';

export default function ChatListPage() {
  const { user } = useAuthStore();
  const [chats, setChats] = useState<ChatRoom[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!user) { setIsLoading(false); return; }
    setIsLoading(true);
    setError(null);
    apiClient.get('/chat/rooms')
      .then(res => {
        setChats(res.data.rooms || []);
      })
      .catch(() => {
        setError('Chat is currently unavailable. Please try again later.');
      })
      .finally(() => setIsLoading(false));
  }, [user]);

  if (!user) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="text-center bg-white rounded-xl border border-gray-200 p-8 max-w-sm">
          <div className="text-5xl mb-4">💬</div>
          <h2 className="text-xl font-semibold text-gray-900 mb-2">Sign in to chat</h2>
          <p className="text-gray-500 mb-4">View your messages and chat with sellers</p>
          <Link href="/login" className="inline-flex px-6 py-2.5 bg-blue-500 text-white rounded-lg font-medium hover:bg-blue-600 transition-colors">Sign In</Link>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Messages</h1>

      {isLoading ? (
        <div className="space-y-3">
          {Array.from({ length: 3 }).map((_, i) => (
            <div key={i} className="bg-white rounded-lg border border-gray-200 p-4 flex items-center gap-4 animate-pulse">
              <div className="w-12 h-12 rounded-full bg-gray-200" />
              <div className="flex-1 space-y-2">
                <div className="h-4 bg-gray-200 rounded w-1/3" />
                <div className="h-3 bg-gray-100 rounded w-2/3" />
              </div>
            </div>
          ))}
        </div>
      ) : error ? (
        <div className="text-center py-20 bg-white rounded-lg border border-gray-200">
          <div className="text-5xl mb-4">⚠️</div>
          <h2 className="text-lg font-semibold text-gray-900 mb-2">{error}</h2>
          <button
            onClick={() => window.location.reload()}
            className="mt-4 px-4 py-2 bg-blue-500 text-white rounded-lg text-sm hover:bg-blue-600"
          >
            Retry
          </button>
        </div>
      ) : chats.length === 0 ? (
        <div className="text-center py-20 bg-white rounded-lg border border-gray-200">
          <div className="text-6xl mb-4">💬</div>
          <h2 className="text-xl font-semibold text-gray-900 mb-2">No messages yet</h2>
          <p className="text-gray-500 mb-4">Start a conversation from an item listing</p>
          <Link href="/" className="text-blue-500 hover:text-blue-600 font-medium">Browse items</Link>
        </div>
      ) : (
        <div className="bg-white rounded-lg border border-gray-200 divide-y divide-gray-100">
          {chats.map((chat) => (
            <Link key={chat.id} href={`/messages/${chat.id}`}
              className="flex items-center gap-4 p-4 hover:bg-gray-50 transition-colors">
              <div className="w-12 h-12 rounded-full bg-blue-500 flex items-center justify-center text-white font-bold shrink-0">
                {chat.itemTitle?.charAt(0) || 'C'}
              </div>
              <div className="flex-1 min-w-0">
                <div className="flex justify-between items-baseline">
                  <h3 className="font-medium text-gray-900 truncate">
                    {chat.itemTitle || 'Chat'}
                  </h3>
                  <span className="text-xs text-gray-400 shrink-0 ml-2">
                    {chat.lastMessage?.sentAt ? timeAgo(chat.lastMessage.sentAt) : ''}
                  </span>
                </div>
                <p className="text-sm text-gray-500 truncate mt-0.5">
                  {chat.lastMessage?.text || 'No messages yet'}
                </p>
              </div>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
