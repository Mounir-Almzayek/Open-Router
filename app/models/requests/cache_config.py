"""
Cache Configuration
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel
from app.enums import CacheControlType, CacheTTL


class CacheConfig(BaseModel):
    """Cache configuration"""
    type: CacheControlType = CacheControlType.EPHEMERAL
    ttl: Optional[CacheTTL] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {"type": self.type.value}
        if self.ttl is not None:
            result["ttl"] = self.ttl.value
        return result

