"""
Tests for geo-processing endpoints.
"""
import pytest
from fastapi.testclient import TestClient


def test_process_points_valid(test_client: TestClient):
    """Test processing valid points returns correct centroid and bounds."""
    payload = {
        "points": [
            {"lat": 10.0, "lng": 20.0},
            {"lat": 20.0, "lng": 30.0},
            {"lat": 30.0, "lng": 40.0}
        ]
    }
    
    response = test_client.post("/geo/process-points", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert "centroid" in data
    assert "bounds" in data
    
    # Check centroid calculation
    assert data["centroid"]["lat"] == pytest.approx(20.0)
    assert data["centroid"]["lng"] == pytest.approx(30.0)
    
    # Check bounds calculation
    assert data["bounds"]["north"] == 30.0
    assert data["bounds"]["south"] == 10.0
    assert data["bounds"]["east"] == 40.0
    assert data["bounds"]["west"] == 20.0


def test_process_points_single(test_client: TestClient):
    """Test processing a single point."""
    payload = {
        "points": [
            {"lat": 10.0, "lng": 20.0}
        ]
    }
    
    response = test_client.post("/geo/process-points", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert data["centroid"]["lat"] == 10.0
    assert data["centroid"]["lng"] == 20.0
    assert data["bounds"]["north"] == 10.0
    assert data["bounds"]["south"] == 10.0
    assert data["bounds"]["east"] == 20.0
    assert data["bounds"]["west"] == 20.0


def test_process_points_empty(test_client: TestClient):
    """Test processing empty points list returns validation error."""
    payload = {
        "points": []
    }
    
    response = test_client.post("/geo/process-points", json=payload)
    assert response.status_code == 422  # Validation error


def test_process_points_invalid_lat(test_client: TestClient):
    """Test processing points with invalid latitude returns validation error."""
    payload = {
        "points": [
            {"lat": 100.0, "lng": 20.0}  # Latitude > 90
        ]
    }
    
    response = test_client.post("/geo/process-points", json=payload)
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data


def test_process_points_invalid_lng(test_client: TestClient):
    """Test processing points with invalid longitude returns validation error."""
    payload = {
        "points": [
            {"lat": 10.0, "lng": 200.0}  # Longitude > 180
        ]
    }
    
    response = test_client.post("/geo/process-points", json=payload)
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data


def test_process_points_missing_fields(test_client: TestClient):
    """Test processing points with missing fields returns validation error."""
    payload = {
        "points": [
            {"lat": 10.0}  # Missing lng
        ]
    }
    
    response = test_client.post("/geo/process-points", json=payload)
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data
