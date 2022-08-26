from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Awesome API"
    DB_URL: str = "mongodb://localhost:27017/"
    DB_NAME: str = "test"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
