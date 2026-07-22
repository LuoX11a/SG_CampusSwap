'use client';

import clsx from 'clsx';

interface Category {
  key: string | null;
  label: string;
}

interface CategoryChipsProps {
  categories: Category[];
  active: string | null;
  onChange: (key: string | null) => void;
}

export default function CategoryChips({ categories, active, onChange }: CategoryChipsProps) {
  return (
    <div className="flex items-center gap-2 overflow-x-auto pb-1 scrollbar-hide">
      {categories.map((cat) => (
        <button
          key={cat.key ?? '__all__'}
          onClick={() => onChange(cat.key)}
          className={clsx(
            'shrink-0 px-4 py-1.5 rounded-full text-sm font-medium transition-colors duration-150',
            active === cat.key
              ? 'bg-blue-500 text-white shadow-sm'
              : 'bg-white text-gray-600 border border-gray-200 hover:bg-gray-50',
          )}
        >
          {cat.label}
        </button>
      ))}
    </div>
  );
}
