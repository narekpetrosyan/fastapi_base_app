from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class ApiPrefixConfig(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        case_sensitive=False,
        env_prefix="FASTAPI__",
        env_nested_delimiter="__",
    )
    run: RunConfig = RunConfig()
    api: ApiPrefixConfig = ApiPrefixConfig()
    db: DatabaseConfig


settings = Settings()
