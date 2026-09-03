from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class DatabaseConfig(BaseModel):
    db_url: str


class ApiPrefixConfig(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    # db: DatabaseConfig = DatabaseConfig()
    api: ApiPrefixConfig = ApiPrefixConfig()


settings = Settings()
