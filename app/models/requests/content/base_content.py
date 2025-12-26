"""
Base Content Model
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from pydantic import BaseModel
from app.enums import ContentType
from app.models.requests.content.cache_control import CacheControl


class BaseContent(BaseModel, ABC):
    """Base content class"""
    type: ContentType
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        pass
    
    class Config:
        arbitrary_types_allowed = True

