'use client';

import { useState, FormEvent } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { useAuthStore } from '@/stores/auth-store';

const UNIVERSITIES = [
  'National University of Singapore (NUS)',
  'Nanyang Technological University (NTU)',
  'Singapore Management University (SMU)',
  'Singapore University of Technology and Design (SUTD)',
  'Singapore University of Social Sciences (SUSS)',
  'Singapore Institute of Technology (SIT)',
  'James Cook University Singapore (JCU)',
];

export default function RegisterPage() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [university, setUniversity] = useState('');
  const [campus, setCampus] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const { register, isLoading, error, clearError } = useAuthStore();
  const router = useRouter();

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      return;
    }
    try {
      const result = await register({ username, email, university, campus, password, confirmPassword });
      if (result?.email) {
        router.push(`/verify-email?email=${encodeURIComponent(result.email)}`);
      }
    } catch (err: any) {
      // Error handled by store — but log for debugging
      console.error('Register error:', err?.response?.data || err);
    }
  };

  return (
    <div className="min-h-[80vh] flex items-center justify-center bg-gray-50 py-12">
      <div className="w-full max-w-md">
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-8">
          <div className="text-center mb-6">
            <h1 className="text-2xl font-bold text-gray-900">Create Account</h1>
            <p className="text-gray-500 mt-1">Join your campus community</p>
          </div>

          {error && (
            <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-sm text-red-700">
              {error}
              <button onClick={clearError} className="float-right text-red-400 hover:text-red-600">✕</button>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-3">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Username</label>
              <input type="text" value={username} onChange={(e) => setUsername(e.target.value)}
                placeholder="alex_chen" required minLength={3} maxLength={20} pattern="^[a-zA-Z0-9_]+$"
                className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">University Email</label>
              <input type="email" value={email} onChange={(e) => setEmail(e.target.value)}
                placeholder="e0123456@u.nus.edu" required
                className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
              <p className="text-xs text-gray-400 mt-1">Must use .edu or .edu.sg email</p>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">University</label>
              <select value={university} onChange={(e) => setUniversity(e.target.value)} required
                className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none bg-white">
                <option value="">Select your university</option>
                {UNIVERSITIES.map((u) => <option key={u} value={u}>{u}</option>)}
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Campus</label>
              <input type="text" value={campus} onChange={(e) => setCampus(e.target.value)}
                placeholder="e.g., UTown, Kent Ridge" required
                className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Password</label>
              <input type="password" value={password} onChange={(e) => setPassword(e.target.value)}
                placeholder="Min. 8 chars, 1 uppercase, 1 digit" required minLength={8}
                className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Confirm Password</label>
              <input type="password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)}
                placeholder="Re-enter your password" required minLength={8}
                className={`w-full h-11 px-3 border rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none ${confirmPassword && password !== confirmPassword ? 'border-red-300' : 'border-gray-300'}`} />
              {confirmPassword && password !== confirmPassword && (
                <p className="text-xs text-red-500 mt-1">Passwords do not match</p>
              )}
            </div>

            <button type="submit" disabled={isLoading}
              className="w-full h-11 bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300 text-white rounded-lg font-medium text-sm transition-colors mt-4">
              {isLoading ? 'Creating account...' : 'Create Account'}
            </button>
          </form>

          <p className="mt-6 text-center text-sm text-gray-500">
            Already have an account?{' '}
            <Link href="/login" className="text-blue-500 hover:text-blue-600 font-medium">Sign in</Link>
          </p>
        </div>
      </div>
    </div>
  );
}
