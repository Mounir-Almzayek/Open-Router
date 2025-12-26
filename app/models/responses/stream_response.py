"""
Streaming Response Models
"""
from typing import Optional, Dict, Any, List
from pydantic import BaseModel
from app.enums import FinishReason


class StreamDelta(BaseModel):
    """Delta in streaming response"""
    role: Optional[str] = None
    content: Optional[str] = None
    tool_calls: Optional[Any] = None
    reasoning_details: Optional[Any] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {}
        if self.role is not None:
            result["role"] = self.role
        if self.content is not None:
            result["content"] = self.content
        if self.tool_calls is not None:
            result["tool_calls"] = self.tool_calls
        if self.reasoning_details is not None:
            result["reasoning_details"] = self.reasoning_details
        return result


class StreamChoice(BaseModel):
    """Choice in streaming response"""
    index: int
    delta: StreamDelta
    finish_reason: Optional[FinishReason] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {
            "index": self.index,
            "delta": self.delta.to_dict()
        }
        if self.finish_reason is not None:
            result["finish_reason"] = self.finish_reason.value
        return result


class StreamChunk(BaseModel):
    """Streaming response chunk"""
    id: Optional[str] = None
    model: Optional[str] = None
    created: Optional[int] = None
    object: str = "chat.completion.chunk"
    choices: List[StreamChoice] = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {
            "object": self.object,
            "choices": [choice.to_dict() for choice in self.choices]
        }
        if self.id is not None:
            result["id"] = self.id
        if self.model is not None:
            result["model"] = self.model
        if self.created is not None:
            result["created"] = self.created
        return result

