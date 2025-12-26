"""
Base Request Model
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List
from pydantic import BaseModel
from app.models.base import BaseRequest


class Message(BaseModel):
    """Message in conversation"""
    role: str  # MessageRole
    content: Any  # str or List[BaseContent]
    name: Any = None
    tool_calls: Any = None
    tool_call_id: Any = None
    reasoning_details: Any = None
    annotations: Any = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {
            "role": self.role,
            "content": self._convert_content(self.content)
        }
        
        if self.name is not None:
            result["name"] = self.name
        if self.tool_calls is not None:
            result["tool_calls"] = self.tool_calls
        if self.tool_call_id is not None:
            result["tool_call_id"] = self.tool_call_id
        if self.reasoning_details is not None:
            result["reasoning_details"] = self.reasoning_details
        if self.annotations is not None:
            result["annotations"] = self.annotations
        
        return result
    
    def _convert_content(self, content: Any) -> Any:
        """Convert content to dict format"""
        if isinstance(content, str):
            return content
        elif isinstance(content, list):
            return [item.to_dict() if hasattr(item, 'to_dict') else item for item in content]
        elif hasattr(content, 'to_dict'):
            return content.to_dict()
        return content

