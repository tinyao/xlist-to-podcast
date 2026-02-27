const BASE_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export type Voice = "alloy" | "echo" | "fable" | "onyx" | "nova" | "shimmer";
export type Language = "zh" | "en";

export interface Podcast {
  id: string;
  name: string;
  description: string;
  twitter_list_url: string;
  voice: Voice;
  language: Language;
  publish_hour: number;
  cover_url: string;
  feed_url: string;
  is_active: boolean;
  created_at: string;
}

export interface Episode {
  id: string;
  podcast_id: string;
  date: string;
  title: string;
  shownotes: string;
  audio_url: string;
  audio_duration: number;
  tweet_count: number;
  status: string;
  error_msg: string;
  created_at: string;
}

export interface EpisodeDetail extends Episode {
  script: string;
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${BASE_URL}${path}`, init);
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(err.detail ?? "请求失败");
  }
  if (res.status === 204) return undefined as T;
  return res.json();
}

export const api = {
  createPodcast: (form: FormData) =>
    request<Podcast>("/api/podcasts", { method: "POST", body: form }),

  listPodcasts: () =>
    request<Podcast[]>("/api/podcasts"),

  getPodcast: (id: string) =>
    request<Podcast>(`/api/podcasts/${id}`),

  deletePodcast: (id: string) =>
    request<void>(`/api/podcasts/${id}`, { method: "DELETE" }),

  listEpisodes: (podcastId: string) =>
    request<Episode[]>(`/api/podcasts/${podcastId}/episodes`),

  getEpisode: (podcastId: string, date: string) =>
    request<EpisodeDetail>(`/api/podcasts/${podcastId}/episodes/${date}`),

  triggerEpisode: (podcastId: string) =>
    request<{ message: string }>(`/api/podcasts/${podcastId}/episodes/trigger`, {
      method: "POST",
    }),
};
