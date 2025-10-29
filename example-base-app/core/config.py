from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DataBaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    api: ApiPrefix = ApiPrefix()
    db: DataBaseConfig


settings = Settings()
