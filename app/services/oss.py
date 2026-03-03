"""
阿里云 OSS 上传服务。

未配置 OSS 时所有函数为 no-op，零性能开销。
调用方使用 asyncio.to_thread() 包装 upload_file_sync()。
"""
import logging
import mimetypes
from typing import Optional

from app.config import settings

logger = logging.getLogger(__name__)

_bucket = None
_initialized = False

# 扩展名 → Content-Type 映射（补充 mimetypes 缺失的类型）
_EXTRA_CONTENT_TYPES = {
    ".mp3": "audio/mpeg",
    ".xml": "application/rss+xml",
    ".json": "application/json",
    ".md": "text/markdown; charset=utf-8",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
}


def is_enabled() -> bool:
    return bool(
        settings.oss_access_key_id
        and settings.oss_access_key_secret
        and settings.oss_endpoint
        and settings.oss_bucket_name
    )


def _get_bucket():
    global _bucket, _initialized
    if _initialized:
        return _bucket
    _initialized = True

    if not is_enabled():
        logger.info("[OSS] Not configured, using local storage only")
        return None

    import oss2

    auth = oss2.Auth(settings.oss_access_key_id, settings.oss_access_key_secret)
    _bucket = oss2.Bucket(auth, settings.oss_endpoint, settings.oss_bucket_name)
    logger.info(f"[OSS] Initialized bucket: {settings.oss_bucket_name}")
    return _bucket


def _guess_content_type(key: str) -> Optional[str]:
    ext = "." + key.rsplit(".", 1)[-1] if "." in key else ""
    ext = ext.lower()
    if ext in _EXTRA_CONTENT_TYPES:
        return _EXTRA_CONTENT_TYPES[ext]
    ct, _ = mimetypes.guess_type(key)
    return ct


def upload_file_sync(key: str, data: bytes) -> None:
    """同步上传文件到 OSS。key 为 OSS 对象路径（如 '{podcast_id}/cover.jpg'）。"""
    bucket = _get_bucket()
    if bucket is None:
        return

    headers = {}
    ct = _guess_content_type(key)
    if ct:
        headers["Content-Type"] = ct

    bucket.put_object(key, data, headers=headers)
    logger.info(f"[OSS] Uploaded: {key} ({len(data)} bytes)")


def download_file_sync(key: str) -> Optional[bytes]:
    """同步从 OSS 下载文件。不存在返回 None。"""
    bucket = _get_bucket()
    if bucket is None:
        return None

    import oss2

    try:
        result = bucket.get_object(key)
        data = result.read()
        logger.info(f"[OSS] Downloaded: {key} ({len(data)} bytes)")
        return data
    except oss2.exceptions.NoSuchKey:
        logger.debug(f"[OSS] Not found: {key}")
        return None


def list_keys_sync(prefix: str) -> list[str]:
    """列出指定前缀下的所有对象 key。"""
    bucket = _get_bucket()
    if bucket is None:
        return []

    import oss2

    keys: list[str] = []
    for obj in oss2.ObjectIterator(bucket, prefix=prefix):
        keys.append(obj.key)
    logger.info(f"[OSS] Listed {len(keys)} keys under '{prefix}'")
    return keys


def public_url(relative_path: str) -> str:
    """
    返回文件的公开访问 URL。
    OSS 启用时返回 CDN/OSS 地址，否则返回本地 /static/ 地址。
    """
    if not relative_path:
        return ""

    if is_enabled():
        base = settings.oss_cdn_url.rstrip("/") if settings.oss_cdn_url else \
            f"https://{settings.oss_bucket_name}.{settings.oss_endpoint}"
        return f"{base}/{relative_path}"

    return f"{settings.server_base_url}/static/{relative_path}"
