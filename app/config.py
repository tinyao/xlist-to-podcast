from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Twitter
    twitter_bearer_token: str = ""

    # OpenAI (TTS)
    openai_api_key: str = ""

    # OpenRouter (LLM)
    openrouter_api_key: str = ""

    # 本地文件服务 base URL（生产环境改为实际域名）
    server_base_url: str = "http://localhost:8000"

    # GitHub Pages 站点地址（如 "https://podcast.example.com"）
    site_url: str = ""

    # 阿里云 OSS（可选，全部配置后启用）
    oss_access_key_id: str = ""
    oss_access_key_secret: str = ""
    oss_endpoint: str = ""
    oss_bucket_name: str = ""
    oss_cdn_url: str = ""


settings = Settings()
