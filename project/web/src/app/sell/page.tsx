'use client';

import { useState, useRef, ChangeEvent } from 'react';
import { useRouter } from 'next/navigation';
import { ImagePlus, X } from 'lucide-react';
import { useItemStore } from '@/stores/item-store';
import { useAuthStore } from '@/stores/auth-store';
import apiClient from '@/lib/api-client';
import toast from 'react-hot-toast';

const CATEGORIES: { value: string; label: string }[] = [
  { value: 'textbook', label: '📚 Textbook' },
  { value: 'electronics', label: '💻 Electronics' },
  { value: 'furniture', label: '🪑 Furniture' },
  { value: 'daily', label: '🧴 Daily Essentials' },
  { value: 'other', label: '📦 Other' },
];

const CONDITIONS: { value: string; label: string }[] = [
  { value: 'like_new', label: 'Like New' },
  { value: 'good', label: 'Good' },
  { value: 'fair', label: 'Fair' },
  { value: 'worn', label: 'Worn' },
];

export default function CreateListingPage() {
  const { user, isAuthenticated } = useAuthStore();
  const router = useRouter();
  const fileInputRef = useRef<HTMLInputElement>(null);

  if (!isAuthenticated || !user) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="text-center bg-white rounded-xl border border-gray-200 p-8 max-w-sm">
          <div className="text-5xl mb-4">🛍️</div>
          <h2 className="text-xl font-semibold text-gray-900 mb-2">Sign in to sell</h2>
          <p className="text-gray-500 mb-4">Create listings and start selling to your campus community</p>
          <button
            onClick={() => router.push('/login')}
            className="inline-flex px-6 py-2.5 bg-blue-500 text-white rounded-lg font-medium hover:bg-blue-600 transition-colors"
          >Sign In</button>
        </div>
      </div>
    );
  }

  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [category, setCategory] = useState<string>('other');
  const [condition, setCondition] = useState<string>('good');
  const [priceDollars, setPriceDollars] = useState('');
  const [courseCode, setCourseCode] = useState('');
  const [campusLocation, setCampusLocation] = useState(user?.campus || '');
  const [meetupPoint, setMeetupPoint] = useState('');
  const [imageFiles, setImageFiles] = useState<File[]>([]);
  const [imagePreviews, setImagePreviews] = useState<string[]>([]);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleImageSelect = (e: ChangeEvent<HTMLInputElement>) => {
    const files = Array.from(e.target.files || []);
    const remaining = 5 - imageFiles.length;
    const toAdd = files.slice(0, remaining);

    toAdd.forEach((file) => {
      const reader = new FileReader();
      reader.onload = (ev) => {
        setImagePreviews((prev) => [...prev, ev.target?.result as string]);
      };
      reader.readAsDataURL(file);
    });

    setImageFiles((prev) => [...prev, ...toAdd]);
  };

  const removeImage = (index: number) => {
    setImageFiles((prev) => prev.filter((_, i) => i !== index));
    setImagePreviews((prev) => prev.filter((_, i) => i !== index));
  };

  const isValid = title && description.length >= 10 && priceDollars && imageFiles.length > 0;

  const handleSubmit = async () => {
    if (!isValid) return;
    setIsSubmitting(true);

    try {
      // Upload images first
      const formData = new FormData();
      imageFiles.forEach((f) => formData.append('files', f));
      const uploadRes = await apiClient.post('/upload/images', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      const imageUrls: string[] = uploadRes.data.images.map((img: any) => img.url);

      // Create item
      await useItemStore.getState().createItem({
        title,
        description,
        category,
        price: Math.round(parseFloat(priceDollars) * 100),
        condition,
        courseCode: courseCode || undefined,
        campusLocation,
        meetupPoint,
        imageUrls,
      });

      toast.success('Item listed successfully!');
      router.push('/');
    } catch {
      toast.error('Failed to create listing. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Create Listing</h1>

      <div className="bg-white rounded-lg border border-gray-200 p-6 space-y-5">
        {/* Photos */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Photos (max 5)</label>
          <div className="flex gap-3 flex-wrap">
            {imagePreviews.map((preview, i) => (
              <div key={i} className="relative w-24 h-24 rounded-lg overflow-hidden border border-gray-200">
                <img src={preview} alt="" className="w-full h-full object-cover" />
                <button onClick={() => removeImage(i)} className="absolute top-1 right-1 bg-black/50 text-white rounded-full p-0.5">
                  <X size={14} />
                </button>
              </div>
            ))}
            {imageFiles.length < 5 && (
              <button onClick={() => fileInputRef.current?.click()}
                className="w-24 h-24 rounded-lg border-2 border-dashed border-gray-300 flex flex-col items-center justify-center text-gray-400 hover:border-blue-400 hover:text-blue-400 transition-colors">
                <ImagePlus size={24} />
                <span className="text-xs mt-1">Add</span>
              </button>
            )}
          </div>
          <input ref={fileInputRef} type="file" accept="image/*" multiple onChange={handleImageSelect} className="hidden" />
        </div>

        {/* Title */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Title</label>
          <input type="text" value={title} onChange={(e) => setTitle(e.target.value)}
            placeholder="What are you selling?" maxLength={100}
            className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
        </div>

        {/* Category + Condition */}
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Category</label>
            <select value={category} onChange={(e) => setCategory(e.target.value)}
              className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none bg-white">
              {CATEGORIES.map((c) => <option key={c.value} value={c.value}>{c.label}</option>)}
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Condition</label>
            <select value={condition} onChange={(e) => setCondition(e.target.value)}
              className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none bg-white">
              {CONDITIONS.map((c) => <option key={c.value} value={c.value}>{c.label}</option>)}
            </select>
          </div>
        </div>

        {/* Price + Course Code */}
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Price (SGD)</label>
            <div className="relative">
              <span className="absolute left-3 top-2.5 text-gray-500 text-sm">$</span>
              <input type="number" value={priceDollars} onChange={(e) => setPriceDollars(e.target.value)}
                placeholder="0.00" step="0.01" min="0"
                className="w-full h-11 pl-8 pr-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
            </div>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Course Code <span className="text-gray-400">(optional)</span></label>
            <input type="text" value={courseCode} onChange={(e) => setCourseCode(e.target.value)}
              placeholder="e.g., CS1010" maxLength={20}
              className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
          </div>
        </div>

        {/* Campus + Meetup */}
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Campus</label>
            <input type="text" value={campusLocation} onChange={(e) => setCampusLocation(e.target.value)}
              placeholder="e.g., NUS UTown"
              className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Meetup Point</label>
            <input type="text" value={meetupPoint} onChange={(e) => setMeetupPoint(e.target.value)}
              placeholder="e.g., UTown Starbucks"
              className="w-full h-11 px-3 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
          </div>
        </div>

        {/* Description */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Description</label>
          <textarea value={description} onChange={(e) => setDescription(e.target.value)}
            placeholder="Describe your item �?condition, usage history, reason for selling..." rows={5} maxLength={2000}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none resize-none" />
          <p className="text-xs text-gray-400 mt-1">{description.length}/2000</p>
        </div>

        {/* Submit */}
        <button onClick={handleSubmit} disabled={!isValid || isSubmitting}
          className="w-full h-11 bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300 text-white rounded-lg font-medium text-sm transition-colors">
          {isSubmitting ? 'Posting...' : 'Post Listing'}
        </button>
      </div>
    </div>
  );
}
