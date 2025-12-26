"""
FastAPI dependencies
"""
from typing import Optional
from fastapi import Header, HTTPException, status
from app.config import settings


async def get_openrouter_api_key(
    authorization: Optional[str] = Header(None, alias="Authorization")
) -> str:
    """
    Extract OpenRouter API key from Authorization header or use default from settings
    
    Supports:
    - Bearer token: "Bearer sk-or-v1-..."
    - Direct token: "sk-or-v1-..."
    """
    if authorization:
        # Remove "Bearer " prefix if present
        if authorization.startswith("Bearer "):
            return authorization[7:]
        return authorization
    
    # Fallback to settings
    if settings.openrouter_api_key:
        return settings.openrouter_api_key
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="OpenRouter API key is required. Provide it via Authorization header or set OPENROUTER_API_KEY in environment."
    )


def get_app_attribution_headers() -> dict:
    """
    Get app attribution headers for OpenRouter requests
    """
    headers = {}
    
    if settings.app_url:
        headers["HTTP-Referer"] = settings.app_url
    
    if settings.app_title:
        headers["X-Title"] = settings.app_title
    
    return headers

