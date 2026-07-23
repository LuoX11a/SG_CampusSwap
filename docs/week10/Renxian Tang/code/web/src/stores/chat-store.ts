import { create } from 'zustand';
import type { ChatRoom, ChatMessage } from '@/lib/types';

interface ChatState {
  chats: ChatRoom[];
  currentMessages: ChatMessage[];
  isLoading: boolean;
  error: string | null;

  setChats: (chats: ChatRoom[]) => void;
  setMessages: (messages: ChatMessage[]) => void;
  addMessage: (message: ChatMessage) => void;
  updateLastMessage: (chatId: string, text: string, senderId: string) => void;
}

export const useChatStore = create<ChatState>((set) => ({
  chats: [],
  currentMessages: [],
  isLoading: false,
  error: null,

  setChats: (chats) => set({ chats }),
  setMessages: (messages) => set({ currentMessages: messages }),

  addMessage: (message) =>
    set((s) => ({ currentMessages: [...s.currentMessages, message] })),

  updateLastMessage: (chatId, text, senderId) =>
    set((s) => ({
      chats: s.chats.map((c) =>
        c.id === chatId
          ? { ...c, lastMessage: { text: text.slice(0, 100), senderId, sentAt: new Date().toISOString() } }
          : c,
      ),
    })),
}));
