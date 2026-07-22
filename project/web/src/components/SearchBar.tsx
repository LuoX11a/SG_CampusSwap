'use client';

import { useState, useCallback, useRef } from 'react';
import { Search, X } from 'lucide-react';
import { useRouter } from 'next/navigation';

interface SearchBarProps {
  initialValue?: string;
  placeholder?: string;
}

export default function SearchBar({ initialValue = '', placeholder = 'Search items, course codes, keywords...' }: SearchBarProps) {
  const [value, setValue] = useState(initialValue);
  const [isFocused, setIsFocused] = useState(false);
  const timeoutRef = useRef<NodeJS.Timeout>();
  const router = useRouter();

  const handleChange = useCallback((newValue: string) => {
    setValue(newValue);
    // Debounced search navigation
    if (timeoutRef.current) clearTimeout(timeoutRef.current);
    timeoutRef.current = setTimeout(() => {
      if (newValue.trim()) {
        router.push(`/browse?q=${encodeURIComponent(newValue.trim())}`);
      }
    }, 400);
  }, [router]);

  const handleClear = () => {
    setValue('');
    if (timeoutRef.current) clearTimeout(timeoutRef.current);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && value.trim()) {
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
      router.push(`/browse?q=${encodeURIComponent(value.trim())}`);
    }
  };

  return (
    <div className={`relative flex items-center ${isFocused ? 'ring-2 ring-blue-500 rounded-lg' : ''}`}>
      <div className="absolute left-3 text-gray-400">
        <Search size={20} />
      </div>
      <input
        type="text"
        value={value}
        onChange={(e) => handleChange(e.target.value)}
        onFocus={() => setIsFocused(true)}
        onBlur={() => setIsFocused(false)}
        onKeyDown={handleKeyDown}
        placeholder={placeholder}
        className="w-full h-11 pl-11 pr-10 bg-white border border-gray-200 rounded-lg text-sm text-gray-900 placeholder-gray-400 focus:outline-none"
      />
      {value && (
        <button
          onClick={handleClear}
          className="absolute right-3 text-gray-400 hover:text-gray-600"
          aria-label="Clear search"
        >
          <X size={18} />
        </button>
      )}
    </div>
  );
}
