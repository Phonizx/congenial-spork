from typing import List

from pydantic import HttpUrl
from pydantic_settings import BaseSettings  # NEW


class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[HttpUrl] = []

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
