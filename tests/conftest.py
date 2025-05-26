"""
Test configuration and fixtures.
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services import GeoProcessingService


@pytest.fixture
def test_client():
    """
    Create a test client for testing FastAPI endpoints.
    
    Returns:
        TestClient: FastAPI test client
    """
    with TestClient(app) as client:
        yield client


@pytest.fixture
def geo_service():
    """
    Create a GeoProcessingService for testing.
    
    Returns:
        GeoProcessingService: Service for geographic operations
    """
    return GeoProcessingService()
