from pydantic import BaseModel
import os


class Settings(BaseModel):
    APP_NAME: str = "Arabic Daily Horoscope API"
    VERSION: str = "1.2.0"
    ENV: str = os.getenv("ENV", "dev")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./horoscope.db")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "change-me-jwt-secret")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRE_DAYS: int = int(os.getenv("JWT_EXPIRE_DAYS", 30))
    KONNECT_API_URL: str = os.getenv("KONNECT_API_URL", "https://api.konnect.example/checkout")
    KONNECT_API_KEY: str = os.getenv("KONNECT_API_KEY", "konnect-key")
    PREMIUM_PRODUCT_ID: str = os.getenv("PREMIUM_PRODUCT_ID", "premium_monthly")
    RATE_LIMIT_FREEMIUM_PER_DAY: int = int(os.getenv("RATE_LIMIT_FREEMIUM_PER_DAY", 1))
    CACHE_TTL_SECONDS: int = int(os.getenv("CACHE_TTL_SECONDS", 6 * 3600))
    ALLOW_ORIGINS: str = os.getenv("ALLOW_ORIGINS", "*")

class Config:
    env_file = ".env"

settings = Settings()