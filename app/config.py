"""
Application configuration settings.
"""
from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    """Application settings configuration."""
    
    model_config = ConfigDict(env_file=".env")
    
    app_name: str = "Geo-processor API"
    app_version: str = "1.0.0"
    description: str = "A microservice for processing geographic coordinates"
    debug: bool = False
    
    # API Configuration
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    
    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True
    log_level: str = "info"


# Global settings instance
settings = Settings()
