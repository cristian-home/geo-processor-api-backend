"""
Tests for the GeoProcessingService.
"""
import pytest
from app.services import GeoProcessingService
from app.models import Point


def test_compute_centroid():
    """Test computing centroid with valid points."""
    service = GeoProcessingService()
    points = [
        Point(lat=10.0, lng=20.0),
        Point(lat=20.0, lng=30.0),
        Point(lat=30.0, lng=40.0)
    ]
    
    centroid = service.compute_centroid(points)
    assert centroid.lat == pytest.approx(20.0)
    assert centroid.lng == pytest.approx(30.0)


def test_compute_centroid_single_point():
    """Test computing centroid with a single point."""
    service = GeoProcessingService()
    points = [Point(lat=10.0, lng=20.0)]
    
    centroid = service.compute_centroid(points)
    assert centroid.lat == 10.0
    assert centroid.lng == 20.0


def test_compute_centroid_empty_list():
    """Test computing centroid with an empty list raises ValueError."""
    service = GeoProcessingService()
    
    with pytest.raises(ValueError, match="Cannot compute centroid of empty point list"):
        service.compute_centroid([])


def test_compute_bounds():
    """Test computing bounds with valid points."""
    service = GeoProcessingService()
    points = [
        Point(lat=10.0, lng=20.0),
        Point(lat=20.0, lng=-10.0),
        Point(lat=30.0, lng=40.0)
    ]
    
    bounds = service.compute_bounds(points)
    assert bounds.north == 30.0
    assert bounds.south == 10.0
    assert bounds.east == 40.0
    assert bounds.west == -10.0


def test_compute_bounds_single_point():
    """Test computing bounds with a single point."""
    service = GeoProcessingService()
    points = [Point(lat=10.0, lng=20.0)]
    
    bounds = service.compute_bounds(points)
    assert bounds.north == 10.0
    assert bounds.south == 10.0
    assert bounds.east == 20.0
    assert bounds.west == 20.0


def test_compute_bounds_empty_list():
    """Test computing bounds with an empty list raises ValueError."""
    service = GeoProcessingService()
    
    with pytest.raises(ValueError, match="Cannot compute bounds of empty point list"):
        service.compute_bounds([])
