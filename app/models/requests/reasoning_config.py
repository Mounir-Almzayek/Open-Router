"""
Reasoning Configuration
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel
from app.enums import ReasoningEffort


class ReasoningConfig(BaseModel):
    """Reasoning tokens configuration"""
    effort: Optional[ReasoningEffort] = None
    max_tokens: Optional[int] = None
    exclude: bool = False
    enabled: Optional[bool] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {}
        if self.effort is not None:
            result["effort"] = self.effort.value
        if self.max_tokens is not None:
            result["max_tokens"] = self.max_tokens
        if self.exclude is not None:
            result["exclude"] = self.exclude
        if self.enabled is not None:
            result["enabled"] = self.enabled
        return result

