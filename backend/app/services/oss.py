import io
import oss2

from app.config import settings


def _bucket() -> oss2.Bucket:
    auth = oss2.Auth(settings.oss_access_key_id, settings.oss_access_key_secret)
    return oss2.Bucket(auth, settings.oss_endpoint, settings.oss_bucket_name)


def upload(key: str, data: bytes, content_type: str = "application/octet-stream") -> str:
    """上传文件，设置公共读，返回公开访问 URL。"""
    bucket = _bucket()
    headers = {
        "Content-Type": content_type,
        "x-oss-object-acl": oss2.OBJECT_ACL_PUBLIC_READ,
    }
    bucket.put_object(key, io.BytesIO(data), headers=headers)
    return f"{settings.oss_base_url}/{key}"


def delete(key: str) -> None:
    """删除 OSS 对象（不存在时静默忽略）。"""
    try:
        _bucket().delete_object(key)
    except oss2.exceptions.NoSuchKey:
        pass


def public_url(key: str) -> str:
    return f"{settings.oss_base_url}/{key}"
