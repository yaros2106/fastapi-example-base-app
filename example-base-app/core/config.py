from pydantic import BaseModel
from pydantic_settings import BaseSettings


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    api: ApiPrefix = ApiPrefix()


settings = Settings()
