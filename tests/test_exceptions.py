"""
Tests for custom exception handlers.
"""
from fastapi.responses import JSONResponse
import pytest
from app.exceptions import validation_exception_handler, general_exception_handler


class MockRequest:
    def __init__(self, url="/test"):
        self.url = url


@pytest.mark.asyncio
async def test_validation_exception_handler():
    """Test validation exception handler returns correct response."""
    request = MockRequest()
    exc = ValueError("Test validation error")
    
    response = await validation_exception_handler(request, exc)
    
    assert isinstance(response, JSONResponse)
    assert response.status_code == 400
    content = response.body.decode()
    assert "Validation Error" in content
    assert "Test validation error" in content
    assert "validation_error" in content


@pytest.mark.asyncio
async def test_general_exception_handler():
    """Test general exception handler returns correct response."""
    request = MockRequest()
    exc = Exception("Test general error")
    
    response = await general_exception_handler(request, exc)
    
    assert isinstance(response, JSONResponse)
    assert response.status_code == 500
    content = response.body.decode()
    assert "Internal Server Error" in content
    assert "unexpected error" in content
    assert "internal_error" in content
