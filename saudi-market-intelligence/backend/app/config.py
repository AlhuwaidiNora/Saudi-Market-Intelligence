from pydantic import BaseSettings, PostgresDsn
from typing import List
import json

class Settings(BaseSettings):
    PROJECT_NAME: str = "Saudi Market Intelligence"
    
    # Database
    DATABASE_URL: PostgresDsn

    # Security
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # API Keys
    TADAWUL_API_KEY: str
    NEWS_API_KEY: str

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = []

    @property
    def BACKEND_CORS_ORIGINS_LIST(self) -> List[str]:
        return json.loads(self.BACKEND_CORS_ORIGINS)

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
