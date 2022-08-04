from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Awesome API"
    db_url: str = "mongodb://localhost:27017/"
    db_name: str = "test"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()