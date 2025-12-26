"""
Multimodal Request Model
"""
from typing import Optional, List
from app.models.requests.chat_request import ChatRequest
from app.enums import InputModality


class MultimodalRequest(ChatRequest):
    """Multimodal request with input modality specification"""
    input_modality: Optional[InputModality] = None
    
    @classmethod
    def create_image_request(
        cls,
        model: str,
        image: str,  # URL or base64
        text: Optional[str] = None,
        **kwargs
    ) -> 'MultimodalRequest':
        """Create image request"""
        from app.models.requests.content import TextContent, ImageContent, ImageURL
        from app.models.requests.base_request import Message
        from app.enums import MessageRole
        
        messages = []
        content_parts = []
        
        if text:
            content_parts.append(TextContent(text=text))
        
        content_parts.append(ImageContent(image_url=ImageURL(url=image)))
        messages.append(Message(role=MessageRole.USER.value, content=content_parts))
        
        return cls(
            model=model,
            messages=messages,
            input_modality=InputModality.IMAGE,
            **kwargs
        )
    
    @classmethod
    def create_audio_request(
        cls,
        model: str,
        audio: str,  # Base64
        audio_format: str,
        text: Optional[str] = None,
        **kwargs
    ) -> 'MultimodalRequest':
        """Create audio request"""
        from app.models.requests.content import TextContent, AudioContent, InputAudio
        from app.models.requests.base_request import Message
        from app.enums import MessageRole, AudioFormat
        
        messages = []
        content_parts = []
        
        if text:
            content_parts.append(TextContent(text=text))
        
        content_parts.append(AudioContent(
            input_audio=InputAudio(data=audio, format=AudioFormat(audio_format))
        ))
        messages.append(Message(role=MessageRole.USER.value, content=content_parts))
        
        return cls(
            model=model,
            messages=messages,
            input_modality=InputModality.AUDIO,
            **kwargs
        )

