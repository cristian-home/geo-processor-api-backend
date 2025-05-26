"""
Pydantic models for the geo-processor API.
"""
from typing import List
from pydantic import BaseModel, Field


class Point(BaseModel):
    """Represents a geographic point with latitude and longitude."""
    lat: float = Field(..., description="Latitude in decimal degrees", ge=-90, le=90)
    lng: float = Field(..., description="Longitude in decimal degrees", ge=-180, le=180)


class ProcessPointsRequest(BaseModel):
    """Request model for processing geographic points."""
    points: List[Point] = Field(..., description="List of geographic points to process", min_length=1)


class Centroid(BaseModel):
    """Represents the centroid of a set of points."""
    lat: float = Field(..., description="Centroid latitude")
    lng: float = Field(..., description="Centroid longitude")


class Bounds(BaseModel):
    """Represents the bounding box of a set of points."""
    north: float = Field(..., description="Maximum latitude")
    south: float = Field(..., description="Minimum latitude")
    east: float = Field(..., description="Maximum longitude")
    west: float = Field(..., description="Minimum longitude")


class ProcessPointsResponse(BaseModel):
    """Response model for processed geographic points."""
    centroid: Centroid = Field(..., description="Computed centroid of all points")
    bounds: Bounds = Field(..., description="Bounding box containing all points")
