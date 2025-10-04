"""Application configuration."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings configuration."""

    # Application
    APP_NAME: str = "zapdos"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"

    # Public API
    PUBLIC_API_BASE_URL: str = "https://public.com/api"
    PUBLIC_API_TOKEN: str = ""

    # Database
    DATABASE_URL: str = "postgresql://z:password"
    REDIS_URL: str = "redis://localhost:6379/0"

    # Security
    SECRET_KEY: str = "your-secret-key-here"
    JWT_SECRET_KEY: str = "your-jwt-secret-key-here"

    # Monitoring
    PROMETHEUS_PORT: int = 8000

    # Trading
    PAPER_TRADING: bool = True
    MAX_POSITION_SIZE: float = 10000.0
    DAILY_LOSS_LIMIT: float = 1000.0

    class Config:
        """Pydantic configuration class."""

        env_file = ".env"
        case_sensitive = True


settings = Settings()
