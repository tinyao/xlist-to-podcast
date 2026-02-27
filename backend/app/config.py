from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Twitter
    twitter_bearer_token: str = ""

    # OpenAI
    openai_api_key: str = ""

    # 阿里云 OSS
    oss_access_key_id: str = ""
    oss_access_key_secret: str = ""
    oss_bucket_name: str = ""
    oss_endpoint: str = "oss-cn-hangzhou.aliyuncs.com"
    oss_base_url: str = ""

    # 数据库
    database_url: str = "sqlite+aiosqlite:///./data/app.db"


settings = Settings()
