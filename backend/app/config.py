# backend/app/config.py
import os
from typing import Optional

class Settings:
    # Database
    DATABASE_USER: str = os.getenv("DATABASE_USER", "root")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "password")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT: str = os.getenv("DATABASE_PORT", "3306")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "vad_ska_vi_ata")
    
    @property
    def DATABASE_URL(self) -> str:
        return f"mysql+pymysql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
    
    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "din-hemliga-nyckel-byt-ut-denna-i-produktion")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # App
    APP_NAME: str = "Vad ska vi äta API"
    VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()