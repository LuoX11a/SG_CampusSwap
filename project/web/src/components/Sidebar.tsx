'use client';

import { useEffect } from 'react';
import { usePathname } from 'next/navigation';
import Link from 'next/link';
import {
  Home,
  Search,
  MessageCircle,
  Package,
  Settings,
  PlusCircle,
  LogOut,
} from 'lucide-react';
import { useAuthStore } from '@/stores/auth-store';
import clsx from 'clsx';

const NAV_ITEMS = [
  { href: '/', label: 'Home', icon: Home },
  { href: '/browse', label: 'Browse', icon: Search },
  { href: '/messages', label: 'Messages', icon: MessageCircle },
  { href: '/my-listings', label: 'My Listings', icon: Package },
  { href: '/settings', label: 'Settings', icon: Settings },
];

export default function Sidebar() {
  const pathname = usePathname();
  const { user, isAuthenticated, fetchMe, logout } = useAuthStore();

  useEffect(() => {
    fetchMe();
  }, []);

  const isActive = (href: string) => {
    if (href === '/') return pathname === '/';
    return pathname.startsWith(href);
  };

  // Hide sidebar on auth pages
  if (['/login', '/register', '/verify-email'].includes(pathname)) {
    return null;
  }

  return (
    <aside className="fixed left-0 top-0 h-screen w-sidebar bg-sidebar-bg flex flex-col z-30">
      {/* Logo */}
      <div className="px-4 py-5 border-b border-gray-800">
        <Link href="/" className="flex items-center gap-2">
          <div className="w-8 h-8 bg-blue-500 rounded-lg flex items-center justify-center">
            <span className="text-white font-bold text-sm">SG</span>
          </div>
          <span className="text-sidebar-text-active font-semibold text-sm">
            CampusSwap
          </span>
        </Link>
      </div>

      {/* Navigation */}
      <nav className="flex-1 px-3 py-4 space-y-1">
        {NAV_ITEMS.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            className={clsx(
              'flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors duration-150',
              isActive(item.href)
                ? 'bg-sidebar-active text-sidebar-text-active'
                : 'text-sidebar-text hover:bg-sidebar-hover hover:text-sidebar-text-active',
            )}
          >
            <item.icon
              size={20}
              className={clsx(
                isActive(item.href) ? 'text-sidebar-icon-active' : 'text-sidebar-icon',
              )}
            />
            {item.label}
          </Link>
        ))}
      </nav>

      {/* Sell Button */}
      <div className="px-3 py-2">
        <Link
          href="/sell"
          className="flex items-center justify-center gap-2 w-full py-2.5 bg-blue-500 hover:bg-blue-600 text-white rounded-lg font-medium text-sm transition-colors"
        >
          <PlusCircle size={18} />
          Sell an Item
        </Link>
      </div>

      {/* User Section */}
      {isAuthenticated && user && (
        <div className="px-3 py-4 border-t border-gray-800">
          <Link
            href="/profile"
            className="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-sidebar-hover transition-colors"
          >
            <div className="w-9 h-9 rounded-full bg-gray-600 flex items-center justify-center text-white text-sm font-medium">
              {user.username.charAt(0).toUpperCase()}
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-sidebar-text-active text-sm font-medium truncate">
                {user.username}
              </p>
              <p className="text-sidebar-icon text-xs truncate">
                {user.university} · {user.campus}
              </p>
            </div>
          </Link>
          <button
            onClick={logout}
            className="flex items-center gap-3 w-full px-3 py-2 mt-1 text-sidebar-icon hover:text-red-400 text-sm rounded-lg hover:bg-sidebar-hover transition-colors"
          >
            <LogOut size={16} />
            Log out
          </button>
        </div>
      )}
    </aside>
  );
}
