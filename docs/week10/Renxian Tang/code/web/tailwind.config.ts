import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['./src/**/*.{js,ts,jsx,tsx,mdx}'],
  theme: {
    extend: {
      colors: {
        sidebar: {
          bg: '#111827',
          hover: '#1F2937',
          active: '#374151',
          text: '#D1D5DB',
          'text-active': '#FFFFFF',
          icon: '#9CA3AF',
          'icon-active': '#60A5FA',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
      },
      width: {
        sidebar: '240px',
      },
    },
  },
  plugins: [],
};

export default config;
