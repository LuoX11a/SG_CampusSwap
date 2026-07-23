'use client';

import { useState, useEffect, useRef, FormEvent, useCallback } from 'react';
import { useParams } from 'next/navigation';
import { Send, ChevronLeft } from 'lucide-react';
import Link from 'next/link';
import { useAuthStore } from '@/stores/auth-store';
import apiClient from '@/lib/api-client';
import type { ChatMessage } from '@/lib/types';

export default function ChatRoomPage() {
  const { id } = useParams<{ id: string }>();
  const { user } = useAuthStore();
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [newMessage, setNewMessage] = useState('');
  const [sending, setSending] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const pollRef = useRef<ReturnType<typeof setInterval>>();

  const fetchMessages = useCallback(async () => {
    try {
      const res = await apiClient.get(`/chat/rooms/${id}/messages`);
      setMessages(
        res.data.messages.map((m: Record<string, unknown>) => ({
          id: m.id as string,
          senderId: m.sender_id as string,
          text: m.text as string,
          imageUrl: (m.image_url as string) || null,
          sentAt: m.sent_at as string,
          read: m.read as boolean,
        }))
      );
      setError(null);
    } catch {
      // Room not found or not a participant — handled silently
    } finally {
      setLoading(false);
    }
  }, [id]);

  useEffect(() => {
    fetchMessages();
    // Poll every 3 seconds for new messages
    pollRef.current = setInterval(fetchMessages, 3000);
    return () => clearInterval(pollRef.current);
  }, [fetchMessages]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSend = async (e: FormEvent) => {
    e.preventDefault();
    if (!newMessage.trim() || !user || sending) return;
    setSending(true);
    try {
      const res = await apiClient.post(`/chat/rooms/${id}/messages`, {
        text: newMessage.trim(),
      });
      const m = res.data;
      setMessages((prev) => [
        ...prev,
        {
          id: m.id as string,
          senderId: m.sender_id as string,
          text: m.text as string,
          imageUrl: null,
          sentAt: m.sent_at as string,
          read: false,
        },
      ]);
      setNewMessage('');
    } catch {
      // silently fail
    } finally {
      setSending(false);
      inputRef.current?.focus();
    }
  };

  const isOwn = (senderId: string) => senderId === user?.id;

  if (loading) {
    return (
      <div className="max-w-4xl mx-auto h-[calc(100vh-6rem)] flex items-center justify-center">
        <div className="animate-pulse text-gray-400">Loading messages...</div>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto h-[calc(100vh-6rem)] flex flex-col">
      {/* Header */}
      <div className="flex items-center gap-3 p-4 bg-white border-b border-gray-200 rounded-t-lg">
        <Link href="/messages" className="text-gray-400 hover:text-gray-600">
          <ChevronLeft size={20} />
        </Link>
        <div className="w-10 h-10 rounded-full bg-gray-300 flex items-center justify-center text-white font-bold text-sm">
          ?
        </div>
        <div>
          <h2 className="font-medium text-gray-900 text-sm">Chat</h2>
          <p className="text-xs text-gray-400">Messages</p>
        </div>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-3 bg-gray-50">
        {error && (
          <div className="text-center text-red-500 text-sm py-4">{error}</div>
        )}
        {!loading && messages.length === 0 && (
          <div className="text-center text-gray-400 py-8">
            No messages yet. Say hello!
          </div>
        )}
        {messages.map((msg) => (
          <div
            key={msg.id}
            className={`flex ${isOwn(msg.senderId) ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-[70%] px-4 py-2.5 rounded-2xl text-sm ${
                isOwn(msg.senderId)
                  ? 'bg-blue-500 text-white rounded-br-md'
                  : 'bg-white text-gray-900 rounded-bl-md border border-gray-200 shadow-sm'
              }`}
            >
              <p className="leading-relaxed">{msg.text}</p>
              <p
                className={`text-xs mt-1 ${
                  isOwn(msg.senderId) ? 'text-blue-100' : 'text-gray-400'
                }`}
              >
                {new Date(msg.sentAt).toLocaleTimeString([], {
                  hour: '2-digit',
                  minute: '2-digit',
                })}
              </p>
            </div>
          </div>
        ))}
        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <form
        onSubmit={handleSend}
        className="flex items-center gap-2 p-4 bg-white border-t border-gray-200 rounded-b-lg"
      >
        <input
          ref={inputRef}
          type="text"
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
          placeholder="Type a message..."
          maxLength={500}
          className="flex-1 h-10 px-3 border border-gray-200 rounded-full text-sm focus:ring-2 focus:ring-blue-500 outline-none"
        />
        <button
          type="submit"
          disabled={!newMessage.trim() || sending}
          className="w-10 h-10 bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300 text-white rounded-full flex items-center justify-center transition-colors"
        >
          <Send size={18} />
        </button>
      </form>
    </div>
  );
}
