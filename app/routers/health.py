"""
Health check and root endpoints.
"""
from fastapi import APIRouter, Depends
from ..dependencies import get_settings
from ..config import Settings

router = APIRouter()


@router.get("/")
async def root(settings: Settings = Depends(get_settings)):
    """Root endpoint returning basic service information."""
    return {
        "service": settings.app_name,
        "version": settings.app_version,
        "description": settings.description
    }


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
