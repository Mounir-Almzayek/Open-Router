"""
Generated Image Response Models
"""
from typing import Dict, Any
from pydantic import BaseModel


class GeneratedImageURL(BaseModel):
    """Generated image URL"""
    url: str  # Base64 data URL
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {"url": self.url}


class GeneratedImage(BaseModel):
    """Generated image"""
    type: str = "image_url"
    image_url: GeneratedImageURL
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "type": self.type,
            "image_url": self.image_url.to_dict()
        }

