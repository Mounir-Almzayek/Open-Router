"""
Reasoning Response Models
"""
from typing import Optional, List, Dict, Any, Literal
from pydantic import BaseModel


class ReasoningDetail(BaseModel):
    """Reasoning detail"""
    type: Literal["reasoning.summary", "reasoning.encrypted", "reasoning.text"]
    summary: Optional[str] = None
    data: Optional[str] = None
    text: Optional[str] = None
    signature: Optional[str] = None
    id: Optional[str] = None
    format: str = "anthropic-claude-v1"
    index: Optional[int] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {
            "type": self.type,
            "format": self.format
        }
        if self.summary is not None:
            result["summary"] = self.summary
        if self.data is not None:
            result["data"] = self.data
        if self.text is not None:
            result["text"] = self.text
        if self.signature is not None:
            result["signature"] = self.signature
        if self.id is not None:
            result["id"] = self.id
        if self.index is not None:
            result["index"] = self.index
        return result


class ReasoningResponse(BaseModel):
    """Reasoning tokens response"""
    reasoning_details: List[ReasoningDetail]

