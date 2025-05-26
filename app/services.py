"""
Business logic services for geo-processing operations.
"""
from typing import List
from .models import Point, Centroid, Bounds


class GeoProcessingService:
    """Service class for geographic processing operations."""
    
    @staticmethod
    def compute_centroid(points: List[Point]) -> Centroid:
        """
        Compute the centroid (average coordinates) of a list of points.
        
        Args:
            points: List of geographic points
            
        Returns:
            Centroid: The computed centroid
            
        Raises:
            ValueError: If the points list is empty
        """
        if not points:
            raise ValueError("Cannot compute centroid of empty point list")
        
        total_lat = sum(point.lat for point in points)
        total_lng = sum(point.lng for point in points)
        count = len(points)
        
        return Centroid(
            lat=total_lat / count,
            lng=total_lng / count
        )

    @staticmethod
    def compute_bounds(points: List[Point]) -> Bounds:
        """
        Compute the bounding box of a list of points.
        
        Args:
            points: List of geographic points
            
        Returns:
            Bounds: The computed bounding box
            
        Raises:
            ValueError: If the points list is empty
        """
        if not points:
            raise ValueError("Cannot compute bounds of empty point list")
        
        latitudes = [point.lat for point in points]
        longitudes = [point.lng for point in points]
        
        return Bounds(
            north=max(latitudes),
            south=min(latitudes),
            east=max(longitudes),
            west=min(longitudes)
        )
