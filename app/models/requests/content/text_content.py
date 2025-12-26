"""
Text Content Model
"""
from typing import Dict, Any, Optional
from pydantic import BaseModel
from app.enums import ContentType
from app.models.requests.content.base_content import BaseContent
from app.models.requests.content.cache_control import CacheControl


class TextContent(BaseContent):
    """Text content"""
    type: ContentType = ContentType.TEXT
    text: str
    cache_control: Optional[CacheControl] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {
            "type": self.type.value,
            "text": self.text
        }
        if self.cache_control:
            result["cache_control"] = self.cache_control.to_dict()
        return result

