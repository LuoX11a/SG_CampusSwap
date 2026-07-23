'use client';

import { usePathname } from 'next/navigation';
import Link from 'next/link';
import { Home, Search, MessageCircle, PlusCircle, User } from 'lucide-react';
import clsx from 'clsx';

const TABS = [
  { href: '/', label: 'Home', icon: Home },
  { href: '/browse', label: 'Browse', icon: Search },
  { href: '/messages', label: 'Chat', icon: MessageCircle },
  { href: '/sell', label: 'Sell', icon: PlusCircle },
  { href: '/profile', label: 'Profile', icon: User },
];

export default function MobileBottomNav() {
  const pathname = usePathname();

  // Hide on auth pages
  if (['/login', '/register', '/verify-email'].includes(pathname)) {
    return null;
  }

  // Hide on desktop (md+ uses Sidebar)
  return (
    <nav className="md:hidden fixed bottom-0 left-0 right-0 z-40 bg-white border-t border-gray-200 flex items-center justify-around"
      style={{ paddingBottom: 'env(safe-area-inset-bottom, 0px)', height: '64px' }}
    >
      {TABS.map((tab) => {
        const isActive =
          tab.href === '/'
            ? pathname === '/'
            : pathname.startsWith(tab.href);

        return (
          <Link
            key={tab.href}
            href={tab.href}
            className={clsx(
              'flex flex-col items-center justify-center gap-0.5 flex-1 h-full transition-colors',
              isActive
                ? 'text-blue-500'
                : 'text-gray-400 hover:text-gray-600',
            )}
          >
            <tab.icon size={22} strokeWidth={isActive ? 2.5 : 2} />
            <span className="text-[10px] font-medium">{tab.label}</span>
          </Link>
        );
      })}
    </nav>
  );
}
