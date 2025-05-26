"""
Geo-processor FastAPI microservice entry point.

This service provides an endpoint to process a list of geographic points and compute:
- Centroid (average coordinates)
- Bounding box (north, south, east, west extremes)
"""
import uvicorn
from app.main import app
from app.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level
    )
