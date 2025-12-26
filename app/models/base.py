"""
Base classes and abstract methods for models
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class BaseRequest(BaseModel, ABC):
    """Base class for all request types"""
    
    model: str
    messages: List[Any]  # Will be Message type
    stream: bool = False
    
    @abstractmethod
    def validate(self) -> bool:
        """Validate request"""
        pass
    
    @abstractmethod
    def to_openrouter_format(self) -> Dict[str, Any]:
        """Convert to OpenRouter API format"""
        pass
    
    def add_message(self, message: Any) -> 'BaseRequest':
        """Add message to request"""
        if not hasattr(self, 'messages') or self.messages is None:
            self.messages = []
        self.messages.append(message)
        return self
    
    def set_model(self, model: str) -> 'BaseRequest':
        """Set model"""
        self.model = model
        return self
    
    class Config:
        arbitrary_types_allowed = True


class BaseResponse(BaseModel, ABC):
    """Base class for all response types"""
    
    id: Optional[str] = None
    model: Optional[str] = None
    created: Optional[int] = None
    
    @abstractmethod
    def extract_content(self) -> Any:
        """Extract content from response"""
        pass
    
    class Config:
        arbitrary_types_allowed = True


class BaseContent(BaseModel, ABC):
    """Base content class"""
    type: str  # ContentType
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        pass
    
    class Config:
        arbitrary_types_allowed = True

