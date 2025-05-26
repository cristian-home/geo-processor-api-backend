"""
Custom exception handlers for the application.
"""
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)


async def validation_exception_handler(request: Request, exc: ValueError):
    """
    Handle validation errors with proper logging and response.
    
    Args:
        request: The incoming request
        exc: The validation exception
        
    Returns:
        JSONResponse: Formatted error response
    """
    logger.warning(f"Validation error in {request.url}: {str(exc)}")
    return JSONResponse(
        status_code=400,
        content={
            "error": "Validation Error",
            "detail": str(exc),
            "type": "validation_error"
        }
    )


async def general_exception_handler(request: Request, exc: Exception):
    """
    Handle general exceptions with proper logging and response.
    
    Args:
        request: The incoming request
        exc: The exception
        
    Returns:
        JSONResponse: Formatted error response
    """
    logger.error(f"Unexpected error in {request.url}: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "detail": "An unexpected error occurred",
            "type": "internal_error"
        }
    )
