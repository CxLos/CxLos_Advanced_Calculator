from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/fastapi_db"
    QR_CODE_DIR: str = "qr_codes"
    FILL_COLOR: str = "black"
    BACK_COLOR: str = "white"
    
    class Config:
        env_file = ".env"

settings = Settings()