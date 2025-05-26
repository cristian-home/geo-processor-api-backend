"""
Geo-processing endpoints.
"""
from fastapi import APIRouter, Depends
from ..models import ProcessPointsRequest, ProcessPointsResponse
from ..services import GeoProcessingService
from ..dependencies import get_geo_service

router = APIRouter(
    prefix="/geo",
    tags=["geo-processing"]
)


@router.post("/process-points", response_model=ProcessPointsResponse)
async def process_points(
    request: ProcessPointsRequest,
    geo_service: GeoProcessingService = Depends(get_geo_service)
) -> ProcessPointsResponse:
    """
    Process a list of geographic points to compute centroid and bounds.
    
    Args:
        request: Request containing list of points to process
        geo_service: Injected geo-processing service
        
    Returns:
        ProcessPointsResponse: Computed centroid and bounding box
        
    Raises:
        HTTPException: 400 Bad Request if input validation fails
        HTTPException: 500 Internal Server Error for unexpected errors
    """
    points = request.points
    
    # Use the service to compute centroid and bounds
    centroid = geo_service.compute_centroid(points)
    bounds = geo_service.compute_bounds(points)
    
    return ProcessPointsResponse(
        centroid=centroid,
        bounds=bounds
    )
