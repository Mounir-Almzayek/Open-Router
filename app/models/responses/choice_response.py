"""
Choice Response Model
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel
from app.enums import FinishReason
from app.models.responses.message_response import MessageResponse


class ChoiceResponse(BaseModel):
    """Choice in completion response"""
    index: int
    message: MessageResponse
    finish_reason: Optional[FinishReason] = None
    logprobs: Optional[Dict[str, Any]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {
            "index": self.index,
            "message": self.message.to_dict()
        }
        if self.finish_reason is not None:
            result["finish_reason"] = self.finish_reason.value
        if self.logprobs is not None:
            result["logprobs"] = self.logprobs
        return result

