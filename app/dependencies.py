"""
Dependency injection utilities.
"""
from functools import lru_cache
from .config import Settings
from .services import GeoProcessingService


@lru_cache()
def get_settings() -> Settings:
    """
    Get application settings with caching.
    
    Returns:
        Settings: Application configuration settings
    """
    return Settings()


def get_geo_service() -> GeoProcessingService:
    """
    Get geo-processing service instance.
    
    Returns:
        GeoProcessingService: Service for geographic operations
    """
    return GeoProcessingService()
