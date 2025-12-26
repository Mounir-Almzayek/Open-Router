"""
Message Response Model
"""
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from app.enums import MessageRole
from app.models.tools import ToolCall
from app.models.responses.reasoning_response import ReasoningDetail
from app.models.responses.annotation_response import Annotation
from app.models.responses.image_response import GeneratedImage


class MessageResponse(BaseModel):
    """Enhanced message response"""
    role: MessageRole
    content: Optional[str] = None
    tool_calls: Optional[List[ToolCall]] = None
    tool_call_id: Optional[str] = None  # For tool role
    reasoning: Optional[str] = None  # Legacy reasoning field
    reasoning_details: Optional[List[ReasoningDetail]] = None
    images: Optional[List[GeneratedImage]] = None  # Generated images
    annotations: Optional[List[Annotation]] = None  # Citations, file annotations
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {"role": self.role.value}
        if self.content is not None:
            result["content"] = self.content
        if self.tool_calls is not None:
            result["tool_calls"] = [tc.to_dict() for tc in self.tool_calls]
        if self.tool_call_id is not None:
            result["tool_call_id"] = self.tool_call_id
        if self.reasoning is not None:
            result["reasoning"] = self.reasoning
        if self.reasoning_details is not None:
            result["reasoning_details"] = [rd.to_dict() for rd in self.reasoning_details]
        if self.images is not None:
            result["images"] = [img.to_dict() for img in self.images]
        if self.annotations is not None:
            result["annotations"] = [ann.to_dict() for ann in self.annotations]
        return result

