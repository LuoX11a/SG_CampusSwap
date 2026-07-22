'use client';

import { useState, useEffect, useRef, FormEvent } from 'react';
import { useParams } from 'next/navigation';
import { Send, Paperclip, ChevronLeft } from 'lucide-react';
import Link from 'next/link';
import { useAuthStore } from '@/stores/auth-store';
import type { ChatMessage } from '@/lib/types';

export default function ChatRoomPage() {
  const { id } = useParams<{ id: string }>();
  const { user } = useAuthStore();
  const [messages, setMessages] = useState<ChatMessage[]>([
    { id: 'm1', senderId: 'other', text: 'Hi! Is this still available?', imageUrl: null, sentAt: new Date(Date.now() - 300000).toISOString(), read: true },
    { id: 'm2', senderId: user?.id || 'me', text: 'Yes! Are you at UTown?', imageUrl: null, sentAt: new Date(Date.now() - 240000).toISOString(), read: true },
    { id: 'm3', senderId: 'other', text: "I'm at the library now. Can meet at Starbucks?", imageUrl: null, sentAt: new Date(Date.now() - 180000).toISOString(), read: true },
  ]);
  const [newMessage, setNewMessage] = useState('');
  const bottomRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // In production: Firebase Firestore real-time listener
  // useEffect(() => {
  //   const unsub = chatService.listenToMessages(id, (newMsgs) => setMessages(newMsgs));
  //   return () => unsub();
  // }, [id]);

  const handleSend = (e: FormEvent) => {
    e.preventDefault();
    if (!newMessage.trim() || !user) return;

    const msg: ChatMessage = {
      id: `m${Date.now()}`,
      senderId: user.id,
      text: newMessage.trim(),
      imageUrl: null,
      sentAt: new Date().toISOString(),
      read: false,
    };
    setMessages((prev) => [...prev, msg]);
    setNewMessage('');

    // In production: chatService.sendMessage(id, user.id, msg.text);
  };

  const isOwn = (senderId: string) => senderId === user?.id;

  return (
    <div className="max-w-4xl mx-auto h-[calc(100vh-6rem)] flex flex-col">
      {/* Header */}
      <div className="flex items-center gap-3 p-4 bg-white border-b border-gray-200 rounded-t-lg">
        <Link href="/messages" className="text-gray-400 hover:text-gray-600">
          <ChevronLeft size={20} />
        </Link>
        <div className="w-10 h-10 rounded-full bg-gray-300 flex items-center justify-center text-white font-bold text-sm">
          S
        </div>
        <div>
          <h2 className="font-medium text-gray-900 text-sm">Sarah Lim</h2>
          <p className="text-xs text-gray-400">CS1010 Textbook · $25.00</p>
        </div>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-3 bg-gray-50">
        {messages.map((msg) => (
          <div key={msg.id} className={`flex ${isOwn(msg.senderId) ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[70%] px-4 py-2.5 rounded-2xl text-sm ${
              isOwn(msg.senderId)
                ? 'bg-blue-500 text-white rounded-br-md'
                : 'bg-white text-gray-900 rounded-bl-md border border-gray-200 shadow-sm'
            }`}>
              <p className="leading-relaxed">{msg.text}</p>
              <p className={`text-xs mt-1 ${isOwn(msg.senderId) ? 'text-blue-100' : 'text-gray-400'}`}>
                {new Date(msg.sentAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
              </p>
            </div>
          </div>
        ))}
        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <form onSubmit={handleSend} className="flex items-center gap-2 p-4 bg-white border-t border-gray-200 rounded-b-lg">
        <button type="button" className="text-gray-400 hover:text-gray-600 p-1">
          <Paperclip size={20} />
        </button>
        <input ref={inputRef} type="text" value={newMessage} onChange={(e) => setNewMessage(e.target.value)}
          placeholder="Type a message..." maxLength={1000}
          className="flex-1 h-10 px-3 border border-gray-200 rounded-full text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
        <button type="submit" disabled={!newMessage.trim()}
          className="w-10 h-10 bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300 text-white rounded-full flex items-center justify-center transition-colors">
          <Send size={18} />
        </button>
      </form>
    </div>
  );
}
