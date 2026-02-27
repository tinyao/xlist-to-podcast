"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { api, type Podcast, type Episode } from "@/lib/api";

const STATUS_LABEL: Record<string, string> = {
  done: "已生成",
  processing: "生成中",
  pending: "待处理",
  failed: "失败",
};
const STATUS_COLOR: Record<string, string> = {
  done: "bg-green-100 text-green-700",
  processing: "bg-blue-100 text-blue-700",
  pending: "bg-gray-100 text-gray-500",
  failed: "bg-red-100 text-red-600",
};

export default function PodcastDetailPage() {
  const { id } = useParams<{ id: string }>();
  const [podcast, setPodcast] = useState<Podcast | null>(null);
  const [episodes, setEpisodes] = useState<Episode[]>([]);
  const [loading, setLoading] = useState(true);
  const [triggering, setTriggering] = useState(false);
  const [triggerMsg, setTriggerMsg] = useState("");
  const [copied, setCopied] = useState(false);

  const refresh = () =>
    Promise.all([api.getPodcast(id), api.listEpisodes(id)]).then(([p, eps]) => {
      setPodcast(p);
      setEpisodes(eps);
    });

  useEffect(() => {
    refresh().finally(() => setLoading(false));
  }, [id]);

  const trigger = async () => {
    setTriggering(true);
    setTriggerMsg("");
    try {
      const res = await api.triggerEpisode(id);
      setTriggerMsg(res.message);
      setTimeout(refresh, 3000);
    } catch (e: unknown) {
      setTriggerMsg(e instanceof Error ? e.message : "触发失败");
    } finally {
      setTriggering(false);
    }
  };

  const copy = () => {
    if (!podcast) return;
    navigator.clipboard.writeText(podcast.feed_url);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  if (loading) return <p className="text-gray-400">加载中...</p>;
  if (!podcast) return <p className="text-red-500">播客不存在</p>;

  return (
    <div className="space-y-6">
      {/* 播客信息卡 */}
      <div className="flex items-start gap-4 rounded-xl border bg-white p-6">
        {podcast.cover_url && (
          <img src={podcast.cover_url} alt={podcast.name} className="w-20 h-20 rounded-xl object-cover shrink-0" />
        )}
        <div className="flex-1 min-w-0">
          <h1 className="text-xl font-bold">{podcast.name}</h1>
          {podcast.description && <p className="text-sm text-gray-500 mt-1">{podcast.description}</p>}
          <p className="text-xs text-gray-400 mt-2">
            每日 {String(podcast.publish_hour).padStart(2, "0")}:00 · {podcast.language === "zh" ? "中文" : "English"} · {podcast.voice}
          </p>
        </div>
      </div>

      {/* Feed URL */}
      <div className="rounded-xl border bg-white p-4 space-y-2">
        <p className="text-sm font-medium text-gray-700">RSS 订阅链接</p>
        <div className="flex items-center gap-2">
          <input
            readOnly
            value={podcast.feed_url}
            className="flex-1 rounded-lg border bg-gray-50 px-3 py-2 text-xs font-mono text-gray-600"
          />
          <button
            onClick={copy}
            className="shrink-0 rounded-lg border px-3 py-2 text-sm hover:bg-gray-50"
          >
            {copied ? "已复制" : "复制"}
          </button>
        </div>
      </div>

      {/* 操作 */}
      <div className="flex items-center gap-3">
        <button
          onClick={trigger}
          disabled={triggering}
          className="rounded-lg bg-blue-600 px-4 py-2 text-sm text-white font-medium hover:bg-blue-700 disabled:opacity-50"
        >
          {triggering ? "触发中..." : "手动生成今日节目"}
        </button>
        {triggerMsg && <span className="text-sm text-gray-500">{triggerMsg}</span>}
      </div>

      {/* 节目列表 */}
      <div>
        <h2 className="font-semibold mb-3">节目列表</h2>
        {episodes.length === 0 ? (
          <p className="text-gray-400 text-sm">暂无节目，等待每日自动生成或手动触发</p>
        ) : (
          <div className="space-y-2">
            {episodes.map((ep) => (
              <EpisodeRow key={ep.id} episode={ep} podcastId={id} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

function EpisodeRow({ episode: ep, podcastId }: { episode: Episode; podcastId: string }) {
  const [open, setOpen] = useState(false);
  const [detail, setDetail] = useState<import("@/lib/api").EpisodeDetail | null>(null);

  const toggle = async () => {
    if (!open && !detail) {
      const d = await api.getEpisode(podcastId, ep.date);
      setDetail(d);
    }
    setOpen((v) => !v);
  };

  const formatDuration = (s: number) => {
    const m = Math.floor(s / 60);
    const sec = s % 60;
    return `${m}:${String(sec).padStart(2, "0")}`;
  };

  return (
    <div className="rounded-xl border bg-white overflow-hidden">
      <button onClick={toggle} className="w-full flex items-center gap-4 p-4 text-left hover:bg-gray-50">
        <div className="flex-1 min-w-0">
          <p className="font-medium text-sm truncate">{ep.title || ep.date}</p>
          <p className="text-xs text-gray-400 mt-0.5">
            {ep.tweet_count} 条推文 · {ep.audio_duration ? formatDuration(ep.audio_duration) : "-"}
          </p>
        </div>
        <span
          className={`shrink-0 rounded-full px-2 py-0.5 text-xs font-medium ${STATUS_COLOR[ep.status] ?? "bg-gray-100 text-gray-500"}`}
        >
          {STATUS_LABEL[ep.status] ?? ep.status}
        </span>
        <span className={`text-gray-400 text-sm transition-transform ${open ? "rotate-90" : ""}`}>›</span>
      </button>

      {open && detail && (
        <div className="border-t px-4 py-4 space-y-4">
          {ep.audio_url && (
            <audio controls src={ep.audio_url} className="w-full h-10" />
          )}
          {ep.status === "failed" && ep.error_msg && (
            <p className="text-xs text-red-500 bg-red-50 rounded p-2">{ep.error_msg}</p>
          )}
          {detail.shownotes && (
            <div className="prose prose-sm max-w-none">
              <pre className="whitespace-pre-wrap text-xs text-gray-600 bg-gray-50 rounded-lg p-3">
                {detail.shownotes}
              </pre>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
