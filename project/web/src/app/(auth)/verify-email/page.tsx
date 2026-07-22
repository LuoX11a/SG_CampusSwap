'use client';

import { useState, useRef, useEffect, KeyboardEvent, ClipboardEvent, Suspense } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import { useAuthStore } from '@/stores/auth-store';
import toast from 'react-hot-toast';

export default function VerifyEmailPage() {
  return (
    <Suspense fallback={<div className="p-4">Loading...</div>}>
      <VerifyContent />
    </Suspense>
  );
}

function VerifyContent() {
  const searchParams = useSearchParams();
  const email = searchParams.get('email') || '';
  const [code, setCode] = useState(['', '', '', '', '', '']);
  const inputRefs = useRef<(HTMLInputElement | null)[]>([]);
  const { verifyEmail, isLoading } = useAuthStore();
  const router = useRouter();

  const handleChange = (index: number, value: string) => {
    if (value.length > 1) return;
    const newCode = [...code];
    newCode[index] = value;
    setCode(newCode);

    // Auto-advance to next input
    if (value && index < 5) {
      inputRefs.current[index + 1]?.focus();
    }

    // Auto-submit when all 6 digits entered
    if (value && index === 5) {
      const fullCode = newCode.join('');
      if (fullCode.length === 6) handleVerify(newCode);
    }
  };

  const handleKeyDown = (index: number, e: KeyboardEvent) => {
    if (e.key === 'Backspace' && !code[index] && index > 0) {
      inputRefs.current[index - 1]?.focus();
    }
  };

  const handlePaste = (e: ClipboardEvent) => {
    e.preventDefault();
    const pasted = e.clipboardData.getData('text').replace(/\D/g, '').slice(0, 6);
    if (pasted.length === 6) {
      const digits = pasted.split('');
      setCode(digits);
      handleVerify(digits);
    }
  };

  const handleVerify = async (digits: string[]) => {
    const fullCode = digits.join('');
    if (fullCode.length !== 6) return;
    try {
      await verifyEmail(email, fullCode);
      toast.success('Email verified!');
      router.push('/login');
    } catch {
      setCode(['', '', '', '', '', '']);
      inputRefs.current[0]?.focus();
    }
  };

  return (
    <div className="min-h-[80vh] flex items-center justify-center bg-gray-50">
      <div className="w-full max-w-md">
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-8 text-center">
          <div className="text-5xl mb-4">📧</div>
          <h1 className="text-2xl font-bold text-gray-900 mb-2">Verify Your Email</h1>
          <p className="text-gray-500 mb-6">
            We sent a 6-digit code to <strong className="text-gray-700">{email}</strong>
          </p>

          <div className="flex justify-center gap-2 mb-6" onPaste={handlePaste}>
            {code.map((digit, i) => (
              <input key={i} ref={(el) => { inputRefs.current[i] = el; }}
                type="text" inputMode="numeric" autoComplete="one-time-code" maxLength={1}
                value={digit}
                onChange={(e) => handleChange(i, e.target.value)}
                onKeyDown={(e) => handleKeyDown(i, e)}
                className="w-12 h-14 text-center text-xl font-bold border-2 border-gray-200 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none transition-colors"
                autoFocus={i === 0}
              />
            ))}
          </div>

          <button onClick={() => handleVerify(code)}
            disabled={isLoading || code.join('').length !== 6}
            className="w-full py-2.5 bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300 text-white rounded-lg font-medium text-sm transition-colors">
            {isLoading ? 'Verifying...' : 'Verify Email'}
          </button>

          <p className="mt-4 text-sm text-gray-500">
            Didn&apos;t receive the code?{' '}
            <button className="text-blue-500 hover:text-blue-600 font-medium">Resend (30s)</button>
          </p>
        </div>
      </div>
    </div>
  );
}
