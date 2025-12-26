"""
Cache Control Configuration
"""
from typing import Optional
from pydantic import BaseModel
from app.enums import CacheControlType, CacheTTL


class CacheControl(BaseModel):
    """Cache control configuration"""
    type: CacheControlType = CacheControlType.EPHEMERAL
    ttl: Optional[CacheTTL] = None
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        result = {"type": self.type.value}
        if self.ttl:
            result["ttl"] = self.ttl.value
        return result

