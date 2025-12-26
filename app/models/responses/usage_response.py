"""
Usage Information Models
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel


class Usage(BaseModel):
    """Token usage information"""
    prompt_tokens: Optional[int] = None
    completion_tokens: Optional[int] = None
    total_tokens: Optional[int] = None
    cache_read_tokens: Optional[int] = None
    cache_write_tokens: Optional[int] = None
    reasoning_tokens: Optional[int] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {}
        if self.prompt_tokens is not None:
            result["prompt_tokens"] = self.prompt_tokens
        if self.completion_tokens is not None:
            result["completion_tokens"] = self.completion_tokens
        if self.total_tokens is not None:
            result["total_tokens"] = self.total_tokens
        if self.cache_read_tokens is not None:
            result["cache_read_tokens"] = self.cache_read_tokens
        if self.cache_write_tokens is not None:
            result["cache_write_tokens"] = self.cache_write_tokens
        if self.reasoning_tokens is not None:
            result["reasoning_tokens"] = self.reasoning_tokens
        return result

