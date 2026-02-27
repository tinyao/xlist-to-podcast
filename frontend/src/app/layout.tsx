import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "XList to Podcast",
  description: "将 Twitter List 转为每日播客",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="zh">
      <body className="min-h-screen bg-gray-50 text-gray-900 antialiased">
        <header className="border-b bg-white">
          <div className="mx-auto max-w-3xl px-4 py-4 flex items-center justify-between">
            <a href="/" className="text-lg font-bold tracking-tight">
              🎙 XList to Podcast
            </a>
            <a href="/podcasts" className="text-sm text-gray-500 hover:text-gray-900">
              我的播客
            </a>
          </div>
        </header>
        <main className="mx-auto max-w-3xl px-4 py-8">{children}</main>
      </body>
    </html>
  );
}
