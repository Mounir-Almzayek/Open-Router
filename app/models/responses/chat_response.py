"""
Chat Response Model
"""
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from app.models.base import BaseResponse
from app.models.responses.choice_response import ChoiceResponse
from app.models.responses.usage_response import Usage


class ChatResponse(BaseResponse):
    """Chat completion response"""
    id: Optional[str] = None
    model: Optional[str] = None
    created: Optional[int] = None
    object: str = "chat.completion"
    choices: List[ChoiceResponse] = []
    usage: Optional[Usage] = None
    provider: Optional[str] = None
    
    def extract_content(self) -> Optional[str]:
        """Extract text content from response"""
        if self.choices and len(self.choices) > 0:
            return self.choices[0].message.content
        return None
    
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
        if self.usage is not None:
            result["usage"] = self.usage.to_dict()
        if self.provider is not None:
            result["provider"] = self.provider
        return result

