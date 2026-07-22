export default function SkeletonCard() {
  return (
    <div className="bg-white rounded-lg border border-gray-200 shadow-sm overflow-hidden">
      {/* Image placeholder */}
      <div className="h-48 skeleton" />
      {/* Content */}
      <div className="p-4 space-y-3">
        <div className="h-5 w-20 skeleton" />
        <div className="h-5 w-full skeleton" />
        <div className="h-4 w-3/4 skeleton" />
        <div className="flex gap-2">
          <div className="h-5 w-20 skeleton rounded-full" />
          <div className="h-5 w-16 skeleton rounded-full" />
        </div>
        <div className="flex justify-between">
          <div className="h-4 w-28 skeleton" />
          <div className="h-4 w-16 skeleton" />
        </div>
      </div>
    </div>
  );
}
