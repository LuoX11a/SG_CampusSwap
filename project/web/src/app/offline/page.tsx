export const dynamic = "force-static";

export default function OfflinePage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-gray-50 px-4">
      <div className="text-center">
        <div className="mb-6 text-7xl">📡</div>
        <h1 className="mb-2 text-2xl font-bold text-gray-900">
          You&apos;re offline
        </h1>
        <p className="mb-6 text-gray-500">
          Check your internet connection and try again.
        </p>
        <button
          onClick={() => window.location.reload()}
          className="rounded-lg bg-emerald-600 px-6 py-3 font-medium text-white shadow-sm hover:bg-emerald-700 transition-colors"
        >
          Try again
        </button>
      </div>
    </div>
  );
}
