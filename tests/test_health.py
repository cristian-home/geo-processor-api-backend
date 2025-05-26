"""
Tests for health and root endpoints.
"""
from fastapi.testclient import TestClient


def test_root_endpoint(test_client: TestClient):
    """Test the root endpoint returns correct service information."""
    response = test_client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "service" in data
    assert "version" in data
    assert "description" in data
    assert data["service"] == "Geo-processor API"


def test_health_endpoint(test_client: TestClient):
    """Test the health check endpoint returns healthy status."""
    response = test_client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data == {"status": "healthy"}
