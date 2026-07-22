import type { Metadata, Viewport } from 'next';
import { Inter } from 'next/font/google';
import { Toaster } from 'react-hot-toast';
import Sidebar from '@/components/Sidebar';
import MobileBottomNav from '@/components/MobileBottomNav';
import './globals.css';

const inter = Inter({ subsets: ['latin'], display: 'swap' });

export const metadata: Metadata = {
  title: 'SG CampusSwap — Campus Marketplace',
  description: 'Buy and sell second-hand items within your university campus community.',
  manifest: '/manifest.json',
  themeColor: '#111827',
  appleWebApp: {
    capable: true,
    statusBarStyle: 'black-translucent',
    title: 'CampusSwap',
  },
};

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 5,
  userScalable: true,
  viewportFit: 'cover',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="flex min-h-screen">
          {/* Desktop Sidebar — hidden on mobile */}
          <div className="hidden md:block">
            <Sidebar />
          </div>

          {/* Main content — full width on mobile, offset on desktop */}
          <main className="flex-1 md:ml-[240px] pb-nav md:pb-6 p-3 md:p-6 bg-[#F3F4F6] min-h-screen overflow-x-hidden">
            {children}
          </main>
        </div>

        {/* Mobile Bottom Navigation */}
        <MobileBottomNav />

        <Toaster
          position="top-center"
          toastOptions={{
            duration: 3000,
            style: {
              fontSize: '14px',
              borderRadius: '10px',
              marginTop: '8px',
            },
          }}
        />
      </body>
    </html>
  );
}
