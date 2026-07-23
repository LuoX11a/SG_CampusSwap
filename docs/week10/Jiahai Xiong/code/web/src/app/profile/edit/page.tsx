'use client';

import { useState, useEffect, FormEvent } from 'react';
import { useRouter } from 'next/navigation';
import { useAuthStore } from '@/stores/auth-store';
import apiClient from '@/lib/api-client';
import toast from 'react-hot-toast';

export default function EditProfilePage() {
  const { user, fetchMe } = useAuthStore();
  const router = useRouter();
  const [username, setUsername] = useState('');
  const [university, setUniversity] = useState('');
  const [campus, setCampus] = useState('');
  const [isSaving, setIsSaving] = useState(false);

  useEffect(() => {
    if (user) {
      setUsername(user.username);
      setUniversity(user.university);
      setCampus(user.campus);
    }
  }, [user]);

  const handleSave = async (e: FormEvent) => {
    e.preventDefault();
    setIsSaving(true);
    try {
      await apiClient.put('/users/me', { username, university, campus });
      await fetchMe();
      toast.success('Profile updated!');
      router.back();
    } catch {
      toast.error('Failed to update profile');
    } finally {
      setIsSaving(false);
    }
  };

  return (
    <div className="max-w-lg mx-auto">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Edit Profile</h1>
      <div className="bg-white rounded-lg border border-gray-200 p-6">
        {/* Avatar */}
        <div className="text-center mb-6">
          <div className="w-24 h-24 rounded-full bg-gray-300 flex items-center justify-center text-white text-3xl font-bold mx-auto">
            {username.charAt(0)?.toUpperCase() || '?'}
          </div>
          <button className="mt-2 text-sm text-blue-500 hover:text-blue-600 font-medium">Change photo</button>
        </div>

        <form onSubmit={handleSave} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Username</label>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)}
              minLength={3} maxLength={20} pattern="^[a-zA-Z0-9_]+$"
              className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">University</label>
            <input type="text" value={university} onChange={(e) => setUniversity(e.target.value)}
              className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Campus</label>
            <input type="text" value={campus} onChange={(e) => setCampus(e.target.value)}
              className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
          </div>
          <button type="submit" disabled={isSaving}
            className="w-full py-2.5 bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300 text-white rounded-lg font-medium text-sm transition-colors">
            {isSaving ? 'Saving...' : 'Save Changes'}
          </button>
        </form>
      </div>
    </div>
  );
}
