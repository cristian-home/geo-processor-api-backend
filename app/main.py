"""
Main FastAPI application configuration.
"""
from fastapi import FastAPI
from .routers import health, geo_processing
from .config import settings
from .exceptions import validation_exception_handler, general_exception_handler


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    
    Returns:
        FastAPI: Configured FastAPI application instance
    """
    app = FastAPI(
        title=settings.app_name,
        description=settings.description,
        version=settings.app_version,
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url
    )
    
    # Add exception handlers
    app.add_exception_handler(ValueError, validation_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)
    
    # Include routers
    app.include_router(health.router)
    app.include_router(geo_processing.router)
    
    return app


# Create the app instance
app = create_app()
