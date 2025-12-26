"""
Models API Endpoint
"""
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.openrouter import ModelInfo
from app.services import OpenRouterClient
from app.dependencies import get_openrouter_api_key

router = APIRouter(prefix="/api/v1", tags=["models"])


def get_client(api_key: str = Depends(get_openrouter_api_key)) -> OpenRouterClient:
    """Get OpenRouter client"""
    return OpenRouterClient(api_key=api_key)


@router.get("/models", response_model=List[ModelInfo])
async def list_models(client: OpenRouterClient = Depends(get_client)):
    """List available models"""
    try:
        models = await client.list_models()
        return models
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

