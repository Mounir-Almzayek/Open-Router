"""
Multimodal Endpoints with direct file handling
"""
from fastapi import APIRouter, UploadFile, File, Form, Body, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from typing import Optional, List, Union
from pydantic import BaseModel
from app.models.requests import ChatRequest
from app.models.responses import ChatResponse
from app.services import OpenRouterClient
from app.dependencies import get_openrouter_api_key
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole
from app.exceptions import ValidationError, OpenRouterAPIError

router = APIRouter(prefix="/api/v1", tags=["multimodal"])


def get_client(api_key: str = Depends(get_openrouter_api_key)) -> OpenRouterClient:
    """Get OpenRouter client"""
    return OpenRouterClient(api_key=api_key)


class ChatRequestJSON(BaseModel):
    """JSON body for chat request"""
    model: str
    messages: Optional[List[dict]] = None
    text: Optional[str] = None
    image_url: Optional[str] = None  # URL or base64
    video_url: Optional[str] = None
    file_url: Optional[str] = None
    stream: bool = False
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None


@router.post("/chat/completions/multimodal")
async def chat_completions_multimodal(
    # JSON body parameters
    request: Optional[ChatRequestJSON] = Body(None),
    
    # File uploads (multipart/form-data)
    image: Optional[UploadFile] = File(None),
    video: Optional[UploadFile] = File(None),
    audio: Optional[UploadFile] = File(None),
    file: Optional[UploadFile] = File(None),
    
    # Additional form fields
    model: Optional[str] = Form(None),
    text: Optional[str] = Form(None),
    stream: Optional[bool] = Form(False),
    
    client: OpenRouterClient = Depends(get_client)
):
    """
    Chat completions endpoint with direct file handling
    
    Supports:
    1. JSON body with base64 strings
    2. multipart/form-data with UploadFile
    3. Mix between the two
    """
    try:
        builder = ChatRequestBuilder()
        
        # Use model from form or JSON
        model_name = model or (request.model if request else None)
        if not model_name:
            raise HTTPException(status_code=400, detail="Model is required")
        builder.with_model(model_name)
        
        # Process files
        content_parts = []
        
        # Text from form or JSON
        text_content = text or (request.text if request else None)
        if text_content:
            from app.models.requests.content import TextContent
            content_parts.append(TextContent(text=text_content))
        
        # Image handling
        if image:
            image_content = await ContentBuilder.from_upload_file(image, "image")
            content_parts.append(image_content)
        elif request and request.image_url:
            if request.image_url.startswith("data:") or len(request.image_url) > 200:
                # base64
                image_content = ContentBuilder.from_base64_string(
                    request.image_url, "image", "image/jpeg"
                )
            else:
                # URL
                image_content = ContentBuilder.from_url(request.image_url, "image")
            content_parts.append(image_content)
        
        # Video handling
        if video:
            video_content = await ContentBuilder.from_upload_file(video, "video")
            content_parts.append(video_content)
        elif request and request.video_url:
            if request.video_url.startswith("data:") or len(request.video_url) > 200:
                video_content = ContentBuilder.from_base64_string(
                    request.video_url, "video", "video/mp4"
                )
            else:
                video_content = ContentBuilder.from_url(request.video_url, "video")
            content_parts.append(video_content)
        
        # Audio handling
        if audio:
            audio_content = await ContentBuilder.from_upload_file(audio, "audio")
            content_parts.append(audio_content)
        
        # File/PDF handling
        if file:
            file_content = await ContentBuilder.from_upload_file(file, "file")
            content_parts.append(file_content)
        elif request and request.file_url:
            if request.file_url.startswith("data:") or len(request.file_url) > 200:
                file_content = ContentBuilder.from_base64_string(
                    request.file_url, "file", "application/pdf"
                )
            else:
                file_content = ContentBuilder.from_url(request.file_url, "file")
            content_parts.append(file_content)
        
        # Build message
        if content_parts:
            builder.with_message(MessageRole.USER, content_parts)
        
        # Add messages from JSON if provided
        if request and request.messages:
            for msg in request.messages:
                builder.with_message(MessageRole(msg["role"]), msg["content"])
        
        # Set streaming
        stream_enabled = stream or (request.stream if request else False)
        builder.with_streaming(stream_enabled)
        
        # Build request
        chat_request = builder.build()
        
        # Send to OpenRouter
        if stream_enabled:
            async def stream_response():
                async for chunk in client.stream_chat_completion(chat_request):
                    yield f"data: {chunk.json()}\n\n"
                yield "data: [DONE]\n\n"
            
            return StreamingResponse(stream_response(), media_type="text/event-stream")
        else:
            response = await client.chat_completion(chat_request)
            return response
    
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except OpenRouterAPIError as e:
        raise HTTPException(status_code=e.status_code or 500, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

