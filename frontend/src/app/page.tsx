"use client";

import { useState } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { api, type Podcast } from "@/lib/api";

const schema = z.object({
  name: z.string().min(1, "请输入播客名称").max(100),
  description: z.string().max(500).optional(),
  twitter_list_url: z
    .string()
    .url("请输入有效的 URL")
    .refine((v) => /\/lists\/\d+/.test(v), {
      message: "请使用数字 ID 格式的 List 链接，如 https://x.com/i/lists/1234567890",
    }),
  voice: z.enum(["alloy", "echo", "fable", "onyx", "nova", "shimmer"]),
  language: z.enum(["zh", "en"]),
  publish_hour: z.coerce.number().min(0).max(23),
});

type FormValues = z.infer<typeof schema>;

const VOICES = [
  { value: "alloy", label: "Alloy（中性）" },
  { value: "echo", label: "Echo（男声）" },
  { value: "fable", label: "Fable（英式）" },
  { value: "onyx", label: "Onyx（低沉）" },
  { value: "nova", label: "Nova（女声）" },
  { value: "shimmer", label: "Shimmer（温柔）" },
];

export default function Home() {
  const [result, setResult] = useState<Podcast | null>(null);
  const [coverFile, setCoverFile] = useState<File | null>(null);
  const [coverPreview, setCoverPreview] = useState<string>("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: { voice: "nova", language: "zh", publish_hour: 8 },
  });

  const handleCover = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setCoverFile(file);
    setCoverPreview(URL.createObjectURL(file));
  };

  const onSubmit = async (values: FormValues) => {
    if (!coverFile) {
      setError("请上传播客封面图");
      return;
    }
    setSubmitting(true);
    setError("");

    const form = new FormData();
    Object.entries(values).forEach(([k, v]) => {
      if (v !== undefined) form.append(k, String(v));
    });
    form.append("cover", coverFile);

    try {
      const podcast = await api.createPodcast(form);
      setResult(podcast);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : "创建失败，请重试");
    } finally {
      setSubmitting(false);
    }
  };

  if (result) {
    return <SuccessView podcast={result} onReset={() => setResult(null)} />;
  }

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-2xl font-bold">创建每日播客</h1>
        <p className="mt-1 text-gray-500">将 Twitter List 自动转为每日音频，支持所有播客客户端订阅</p>
      </div>

      <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
        {/* 基本信息 */}
        <section className="rounded-xl border bg-white p-6 space-y-4">
          <h2 className="font-semibold text-gray-700">基本信息</h2>

          <Field label="播客名称" error={errors.name?.message}>
            <input
              {...register("name")}
              placeholder="如：AI 日报"
              className={inputCls(!!errors.name)}
            />
          </Field>

          <Field label="播客简介（可选）" error={errors.description?.message}>
            <textarea
              {...register("description")}
              rows={2}
              placeholder="一句话介绍这个播客"
              className={inputCls(!!errors.description)}
            />
          </Field>

          <Field label="Twitter List 链接" error={errors.twitter_list_url?.message}>
            <input
              {...register("twitter_list_url")}
              placeholder="https://x.com/i/lists/1234567890"
              className={inputCls(!!errors.twitter_list_url)}
            />
          </Field>
        </section>

        {/* 播客设置 */}
        <section className="rounded-xl border bg-white p-6 space-y-4">
          <h2 className="font-semibold text-gray-700">播客设置</h2>

          <div className="grid grid-cols-2 gap-4">
            <Field label="语言" error={errors.language?.message}>
              <select {...register("language")} className={inputCls(false)}>
                <option value="zh">中文</option>
                <option value="en">English</option>
              </select>
            </Field>

            <Field label="每日发布时间（北京时间）" error={errors.publish_hour?.message}>
              <select {...register("publish_hour")} className={inputCls(false)}>
                {Array.from({ length: 24 }, (_, i) => (
                  <option key={i} value={i}>
                    {String(i).padStart(2, "0")}:00
                  </option>
                ))}
              </select>
            </Field>
          </div>

          <Field label="音色" error={errors.voice?.message}>
            <div className="grid grid-cols-3 gap-2">
              {VOICES.map((v) => (
                <label
                  key={v.value}
                  className="flex items-center gap-2 rounded-lg border p-3 cursor-pointer hover:bg-gray-50 has-[:checked]:border-blue-500 has-[:checked]:bg-blue-50"
                >
                  <input type="radio" value={v.value} {...register("voice")} className="accent-blue-500" />
                  <span className="text-sm">{v.label}</span>
                </label>
              ))}
            </div>
          </Field>
        </section>

        {/* 封面 */}
        <section className="rounded-xl border bg-white p-6 space-y-4">
          <h2 className="font-semibold text-gray-700">封面图</h2>
          <div className="flex items-start gap-4">
            {coverPreview ? (
              <img src={coverPreview} alt="封面预览" className="w-24 h-24 rounded-lg object-cover border" />
            ) : (
              <div className="w-24 h-24 rounded-lg border-2 border-dashed flex items-center justify-center text-gray-300 text-xs">
                预览
              </div>
            )}
            <div className="flex-1">
              <label className="block">
                <span className="sr-only">选择封面图</span>
                <input
                  type="file"
                  accept="image/jpeg,image/png,image/webp"
                  onChange={handleCover}
                  className="block w-full text-sm text-gray-500 file:mr-4 file:rounded-lg file:border-0 file:bg-blue-50 file:px-4 file:py-2 file:text-sm file:font-medium file:text-blue-700 hover:file:bg-blue-100"
                />
              </label>
              <p className="mt-1 text-xs text-gray-400">建议 3000×3000px，JPG/PNG，≤ 5MB</p>
            </div>
          </div>
        </section>

        {error && (
          <p className="rounded-lg bg-red-50 border border-red-200 px-4 py-3 text-sm text-red-600">
            {error}
          </p>
        )}

        <button
          type="submit"
          disabled={submitting}
          className="w-full rounded-xl bg-blue-600 py-3 text-white font-semibold hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        >
          {submitting ? "创建中..." : "创建播客"}
        </button>
      </form>
    </div>
  );
}

function SuccessView({ podcast, onReset }: { podcast: Podcast; onReset: () => void }) {
  const [copied, setCopied] = useState(false);

  const copy = () => {
    navigator.clipboard.writeText(podcast.feed_url);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="space-y-6">
      <div className="rounded-xl bg-green-50 border border-green-200 p-6">
        <h2 className="text-lg font-bold text-green-800">播客创建成功！</h2>
        <p className="mt-1 text-green-700 text-sm">
          「{podcast.name}」已创建，将在每天 {String(podcast.publish_hour).padStart(2, "0")}:00 自动生成新节目。
        </p>
      </div>

      <div className="rounded-xl border bg-white p-6 space-y-4">
        <h3 className="font-semibold">RSS 订阅链接</h3>
        <div className="flex items-center gap-2">
          <input
            readOnly
            value={podcast.feed_url}
            className="flex-1 rounded-lg border bg-gray-50 px-3 py-2 text-sm font-mono text-gray-600"
          />
          <button
            onClick={copy}
            className="shrink-0 rounded-lg border px-4 py-2 text-sm hover:bg-gray-50 transition-colors"
          >
            {copied ? "已复制" : "复制"}
          </button>
        </div>

        <div className="text-sm text-gray-500 space-y-1">
          <p className="font-medium text-gray-700">如何订阅：</p>
          <p>• <strong>Apple Podcasts</strong>：资料库 → 关注节目 → 粘贴 URL</p>
          <p>• <strong>小宇宙</strong>：发现 → 搜索 → 从 RSS 导入</p>
          <p>• <strong>Overcast / Pocket Casts</strong>：Add by URL</p>
        </div>
      </div>

      <div className="flex gap-3">
        <a
          href={`/podcasts/${podcast.id}`}
          className="flex-1 rounded-xl border py-3 text-center text-sm font-medium hover:bg-gray-50"
        >
          查看播客详情
        </a>
        <button
          onClick={onReset}
          className="flex-1 rounded-xl bg-blue-600 py-3 text-white text-sm font-semibold hover:bg-blue-700"
        >
          再创建一个
        </button>
      </div>
    </div>
  );
}

function Field({ label, error, children }: { label: string; error?: string; children: React.ReactNode }) {
  return (
    <div>
      <label className="block text-sm font-medium text-gray-700 mb-1">{label}</label>
      {children}
      {error && <p className="mt-1 text-xs text-red-500">{error}</p>}
    </div>
  );
}

function inputCls(hasError: boolean) {
  return [
    "w-full rounded-lg border px-3 py-2 text-sm outline-none transition",
    "focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
    hasError ? "border-red-400 bg-red-50" : "border-gray-300 bg-white",
  ].join(" ");
}
