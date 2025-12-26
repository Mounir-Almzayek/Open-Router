"""
Image Content Model
"""
from typing import Dict, Any, Optional
from pydantic import BaseModel
from app.enums import ContentType
from app.models.requests.content.base_content import BaseContent


class ImageURL(BaseModel):
    """Image URL configuration"""
    url: str
    detail: Optional[str] = None  # "low", "high", "auto"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {"url": self.url}
        if self.detail:
            result["detail"] = self.detail
        return result


class ImageContent(BaseContent):
    """Image content"""
    type: ContentType = ContentType.IMAGE_URL
    image_url: ImageURL
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "type": self.type.value,
            "image_url": self.image_url.to_dict()
        }

