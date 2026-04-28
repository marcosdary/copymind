from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    HOST: str
    USER: str
    PORT: int
    PASSWORD: str
    DATABASE: str
    APP_KEY_GROQ: str
    LLAMA_VERSATILE: str
    GPT_OSS: str


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

settings = get_settings()

