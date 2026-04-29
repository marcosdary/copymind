from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from functools import lru_cache

class Settings(BaseSettings):
    """
    Configurações gerais da aplicação

    Args:
        BaseSettings (_type_): _description_
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )
    API_V1_STR: Optional[str] = "/api/v1"
    URL_POSTGRES: str
    APP_KEY_GROQ: str
    LLAMA_VERSATILE: str
    GPT_OSS: str

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

settings = get_settings()



