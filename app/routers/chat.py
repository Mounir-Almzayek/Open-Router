"""
Chat Completions Endpoint
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from typing import Optional
from app.models.requests import ChatRequest
from app.models.responses import ChatResponse
from app.services import OpenRouterClient
from app.dependencies import get_openrouter_api_key
from app.builders import ChatRequestBuilder
from app.exceptions import ValidationError, OpenRouterAPIError
from app.config import settings

router = APIRouter(prefix="/api/v1", tags=["chat"])


def get_client(api_key: str = Depends(get_openrouter_api_key)) -> OpenRouterClient:
    """Get OpenRouter client"""
    return OpenRouterClient(api_key=api_key)


@router.post("/chat/completions", response_model=ChatResponse)
async def chat_completions(
    request: ChatRequest,
    client: OpenRouterClient = Depends(get_client)
):
    """Chat completions endpoint"""
    try:
        response = await client.chat_completion(request)
        return response
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except OpenRouterAPIError as e:
        raise HTTPException(status_code=e.status_code or 500, detail=e.message)
    except Exception as e:
        import traceback
        error_detail = str(e)
        if settings.debug:
            error_detail += f"\n\nTraceback:\n{traceback.format_exc()}"
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error_detail)


@router.post("/chat/completions/stream")
async def chat_completions_stream(
    request: ChatRequest,
    client: OpenRouterClient = Depends(get_client)
):
    """Streaming chat completions endpoint"""
    try:
        async def generate():
            async for chunk in client.stream_chat_completion(request):
                yield f"data: {chunk.json()}\n\n"
            yield "data: [DONE]\n\n"
        
        return StreamingResponse(generate(), media_type="text/event-stream")
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except OpenRouterAPIError as e:
        raise HTTPException(status_code=e.status_code or 500, detail=e.message)

