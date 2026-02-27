"use client";

import { useEffect, useState } from "react";
import { api, type Podcast } from "@/lib/api";

export default function PodcastsPage() {
  const [podcasts, setPodcasts] = useState<Podcast[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.listPodcasts().then(setPodcasts).finally(() => setLoading(false));
  }, []);

  if (loading) return <p className="text-gray-400">加载中...</p>;

  if (podcasts.length === 0) {
    return (
      <div className="text-center py-16">
        <p className="text-gray-400 text-lg">还没有播客</p>
        <a href="/" className="mt-4 inline-block rounded-xl bg-blue-600 px-6 py-3 text-white text-sm font-semibold hover:bg-blue-700">
          创建第一个播客
        </a>
      </div>
    );
  }

  return (
    <div>
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-xl font-bold">我的播客</h1>
        <a href="/" className="rounded-lg bg-blue-600 px-4 py-2 text-sm text-white font-medium hover:bg-blue-700">
          + 新建
        </a>
      </div>

      <div className="space-y-4">
        {podcasts.map((p) => (
          <a
            key={p.id}
            href={`/podcasts/${p.id}`}
            className="flex items-center gap-4 rounded-xl border bg-white p-4 hover:shadow-sm transition-shadow"
          >
            {p.cover_url ? (
              <img src={p.cover_url} alt={p.name} className="w-16 h-16 rounded-lg object-cover shrink-0" />
            ) : (
              <div className="w-16 h-16 rounded-lg bg-gray-100 shrink-0" />
            )}
            <div className="flex-1 min-w-0">
              <p className="font-semibold truncate">{p.name}</p>
              <p className="text-sm text-gray-400 mt-0.5">
                每日 {String(p.publish_hour).padStart(2, "0")}:00 · {p.language === "zh" ? "中文" : "English"} · {p.voice}
              </p>
              {p.description && (
                <p className="text-xs text-gray-400 mt-1 truncate">{p.description}</p>
              )}
            </div>
            <span className="text-gray-300 text-lg shrink-0">›</span>
          </a>
        ))}
      </div>
    </div>
  );
}
