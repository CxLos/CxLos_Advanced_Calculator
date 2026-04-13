# app/core/config.py

"""
Application configuration settings.
"""

# ==============================================
# Imports
# ==============================================

from functools import lru_cache 
from pydantic_settings import BaseSettings
from typing import Optional, List

# =============================================
# Settings Class
# =============================================

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    
    This class uses Pydantic's BaseSettings to automatically load configuration
    from environment variables or a .env file. This follows the Twelve-Factor App
    methodology for configuration management.
    """
    
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/calculator_db"
    
    # JWT Settings
    JWT_SECRET_KEY: str = "your-super-secret-key-change-this-in-production"
    JWT_REFRESH_SECRET_KEY: str = "your-refresh-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # Security
    BCRYPT_ROUNDS: int = 12
    CORS_ORIGINS: List[str] = ["*"]
    
    # Redis (optional, for token blacklisting)
    REDIS_URL: Optional[str] = "redis://localhost:6379/0"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Create a global settings instance
settings = Settings()

# Optional: Add cached settings getter
@lru_cache()
def get_settings() -> Settings:
    return Settings()