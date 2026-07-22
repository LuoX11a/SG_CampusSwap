/** Format cents to dollar string: 2500 → "25.00" */
export function formatPrice(cents: number): string {
  return (cents / 100).toFixed(2);
}

/** Format cents to display string: 2500 → "$25.00" */
export function formatPriceDisplay(cents: number): string {
  return `$${formatPrice(cents)}`;
}

/** Format category enum to display label */
export function formatCategory(cat: string): string {
  const map: Record<string, string> = {
    textbook: '📚 Textbook',
    electronics: '💻 Electronics',
    furniture: '🪑 Furniture',
    daily: '🧴 Daily Essentials',
    other: '📦 Other',
  };
  return map[cat] || cat;
}

/** Format condition enum to display label */
export function formatCondition(cond: string): string {
  const map: Record<string, string> = {
    like_new: 'Like New',
    good: 'Good',
    fair: 'Fair',
    worn: 'Worn',
  };
  return map[cond] || cond;
}

/** Format status enum to display label */
export function formatStatus(status: string): string {
  const map: Record<string, string> = {
    available: 'Available',
    reserved: 'Reserved',
    sold: 'Sold',
  };
  return map[status] || status;
}

/** Relative time display */
export function timeAgo(dateStr: string): string {
  const now = Date.now();
  const date = new Date(dateStr).getTime();
  const diffMs = now - date;
  const diffMins = Math.floor(diffMs / 60000);
  const diffHours = Math.floor(diffMs / 3600000);
  const diffDays = Math.floor(diffMs / 86400000);
  const diffWeeks = Math.floor(diffDays / 7);

  if (diffMins < 1) return 'Just now';
  if (diffMins < 60) return `${diffMins}m ago`;
  if (diffHours < 24) return `${diffHours}h ago`;
  if (diffDays < 7) return `${diffDays}d ago`;
  if (diffWeeks < 4) return `${diffWeeks}w ago`;
  return new Date(dateStr).toLocaleDateString('en-SG', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  });
}
