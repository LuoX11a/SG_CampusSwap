'use client';

import { useState } from 'react';
import { ChevronRight, Bell, MessageSquare, Package, Shield, Trash2 } from 'lucide-react';
import { useAuthStore } from '@/stores/auth-store';
import toast from 'react-hot-toast';

export default function SettingsPage() {
  const { user } = useAuthStore();
  const [notifications, setNotifications] = useState({
    push: true,
    chat: true,
    listing: false,
  });

  const toggle = (key: keyof typeof notifications) => {
    setNotifications((prev) => ({ ...prev, [key]: !prev[key] }));
    toast.success('Preference saved');
  };

  return (
    <div className="max-w-lg mx-auto">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Settings</h1>

      {/* Account */}
      <div className="mb-6">
        <h2 className="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-3">Account</h2>
        <div className="bg-white rounded-lg border border-gray-200 divide-y divide-gray-100">
          <a href="/profile/edit" className="flex items-center justify-between p-4 hover:bg-gray-50 transition-colors">
            <span className="text-sm text-gray-900">Edit Profile</span>
            <ChevronRight size={18} className="text-gray-300" />
          </a>
          <button className="w-full flex items-center justify-between p-4 hover:bg-gray-50 transition-colors text-left">
            <span className="text-sm text-gray-900">Change Password</span>
            <ChevronRight size={18} className="text-gray-300" />
          </button>
          <div className="p-4">
            <p className="text-sm text-gray-500">{user?.email}</p>
          </div>
        </div>
      </div>

      {/* Notifications */}
      <div className="mb-6">
        <h2 className="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-3">Notifications</h2>
        <div className="bg-white rounded-lg border border-gray-200 divide-y divide-gray-100">
          <div className="flex items-center justify-between p-4">
            <span className="flex items-center gap-3 text-sm text-gray-900"><Bell size={20} className="text-gray-400" /> Push Notifications</span>
            <button onClick={() => toggle('push')}
              className={`w-11 h-6 rounded-full transition-colors ${notifications.push ? 'bg-blue-500' : 'bg-gray-300'}`}>
              <div className={`w-5 h-5 bg-white rounded-full shadow transition-transform ${notifications.push ? 'translate-x-6' : 'translate-x-0.5'}`} />
            </button>
          </div>
          <div className="flex items-center justify-between p-4">
            <span className="flex items-center gap-3 text-sm text-gray-900"><MessageSquare size={20} className="text-gray-400" /> Chat Messages</span>
            <button onClick={() => toggle('chat')}
              className={`w-11 h-6 rounded-full transition-colors ${notifications.chat ? 'bg-blue-500' : 'bg-gray-300'}`}>
              <div className={`w-5 h-5 bg-white rounded-full shadow transition-transform ${notifications.chat ? 'translate-x-6' : 'translate-x-0.5'}`} />
            </button>
          </div>
          <div className="flex items-center justify-between p-4">
            <span className="flex items-center gap-3 text-sm text-gray-900"><Package size={20} className="text-gray-400" /> Listing Updates</span>
            <button onClick={() => toggle('listing')}
              className={`w-11 h-6 rounded-full transition-colors ${notifications.listing ? 'bg-blue-500' : 'bg-gray-300'}`}>
              <div className={`w-5 h-5 bg-white rounded-full shadow transition-transform ${notifications.listing ? 'translate-x-6' : 'translate-x-0.5'}`} />
            </button>
          </div>
        </div>
      </div>

      {/* About */}
      <div className="mb-6">
        <h2 className="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-3">About</h2>
        <div className="bg-white rounded-lg border border-gray-200 divide-y divide-gray-100">
          <div className="flex items-center justify-between p-4">
            <span className="flex items-center gap-3 text-sm text-gray-900"><Shield size={20} className="text-gray-400" /> Privacy Policy</span>
            <ChevronRight size={18} className="text-gray-300" />
          </div>
        </div>
      </div>

      {/* Danger Zone */}
      <div className="mb-6">
        <h2 className="text-sm font-semibold text-red-500 uppercase tracking-wider mb-3">Danger Zone</h2>
        <div className="bg-white rounded-lg border border-red-200">
          <button onClick={() => { if (confirm('Delete your account? This cannot be undone.')) toast.error('Account deletion requires email confirmation.'); }}
            className="w-full flex items-center gap-3 p-4 text-sm text-red-500 hover:bg-red-50 transition-colors rounded-lg text-left">
            <Trash2 size={20} /> Delete Account
          </button>
        </div>
      </div>

      <p className="text-center text-xs text-gray-400 pb-8">SG CampusSwap v1.0.0 · © 2026</p>
    </div>
  );
}
