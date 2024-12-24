# backend/app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL: str
    MONGODB_NAME: str
    MODEL_PATH: str
    DATA_REFRESH_INTERVAL: int = 3600

    class Config:
        env_file = ".env"

settings = Settings()
