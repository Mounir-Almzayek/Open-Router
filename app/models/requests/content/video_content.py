"""
Video Content Model
"""
from typing import Dict, Any
from pydantic import BaseModel
from app.enums import ContentType
from app.models.requests.content.base_content import BaseContent


class VideoURL(BaseModel):
    """Video URL configuration"""
    url: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {"url": self.url}


class VideoContent(BaseContent):
    """Video content"""
    type: ContentType = ContentType.VIDEO_URL
    video_url: VideoURL
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "type": self.type.value,
            "video_url": self.video_url.to_dict()
        }

