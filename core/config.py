from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name:str
    app_version:str
    api_v1_prefix:str

    mongodb_uri:str
    mongodb_db:str
    mongodb_collection:str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()