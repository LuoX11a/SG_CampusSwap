'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { useAuthStore } from '@/stores/auth-store';
import { useChatStore } from '@/stores/chat-store';
import type { ChatRoom } from '@/lib/types';
import { timeAgo } from '@/lib/format';

export default function ChatListPage() {
  const { user } = useAuthStore();
  const { chats, setChats, isLoading } = useChatStore();
  const [mockChats] = useState<ChatRoom[]>([
    { id: '1', participants: ['u1', 'u2'], itemId: 'i1', itemTitle: 'CS1010 Textbook', lastMessage: { text: 'Is this still available?', senderId: 'u2', sentAt: new Date(Date.now() - 120000).toISOString() } },
    { id: '2', participants: ['u1', 'u3'], itemId: 'i2', itemTitle: 'Desk Lamp', lastMessage: { text: 'Sure, meet at UTown Starbucks at 3pm?', senderId: 'u1', sentAt: new Date(Date.now() - 3600000).toISOString() } },
    { id: '3', participants: ['u1', 'u4'], itemId: 'i3', itemTitle: 'Calculus Textbook', lastMessage: { text: 'Thanks for the purchase!', senderId: 'u4', sentAt: new Date(Date.now() - 86400000).toISOString() } },
  ]);

  useEffect(() => {
    setChats(mockChats);
  }, []);

  // In production: Firebase Firestore real-time listener
  // useEffect(() => {
  //   const unsub = chatService.listenToUserChats(user!.id, setChats);
  //   return () => unsub();
  // }, [user]);

  if (!user) {
    return <div className="text-center py-20 text-gray-500">Please sign in to view messages.</div>;
  }

  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Messages</h1>

      {mockChats.length === 0 ? (
        <div className="text-center py-20 bg-white rounded-lg border border-gray-200">
          <div className="text-6xl mb-4">💬</div>
          <h2 className="text-xl font-semibold text-gray-900 mb-2">No messages yet</h2>
          <p className="text-gray-500 mb-4">Start a conversation from an item listing</p>
          <Link href="/" className="text-blue-500 hover:text-blue-600 font-medium">Browse items</Link>
        </div>
      ) : (
        <div className="bg-white rounded-lg border border-gray-200 divide-y divide-gray-100">
          {mockChats.map((chat) => (
            <Link key={chat.id} href={`/messages/${chat.id}`}
              className="flex items-center gap-4 p-4 hover:bg-gray-50 transition-colors">
              <div className="w-12 h-12 rounded-full bg-gray-300 flex items-center justify-center text-white font-bold shrink-0">
                {chat.participants[1]?.charAt(0) || '?'}
              </div>
              <div className="flex-1 min-w-0">
                <div className="flex justify-between items-baseline">
                  <h3 className="font-medium text-gray-900 truncate">
                    {chat.itemTitle || 'Chat'}
                  </h3>
                  <span className="text-xs text-gray-400 shrink-0 ml-2">
                    {chat.lastMessage ? timeAgo(chat.lastMessage.sentAt) : ''}
                  </span>
                </div>
                <p className="text-sm text-gray-500 truncate mt-0.5">
                  {chat.lastMessage?.text || 'No messages'}
                </p>
              </div>
              {/* Unread dot — in production, computed from Firebase */}
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
