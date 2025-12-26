"""
Tool Call Models
"""
from typing import Dict, Any, Literal
from pydantic import BaseModel


class ToolCallFunction(BaseModel):
    """Tool call function"""
    name: str
    arguments: str  # JSON string
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "name": self.name,
            "arguments": self.arguments
        }


class ToolCall(BaseModel):
    """Tool call"""
    id: str
    type: Literal["function"] = "function"
    function: ToolCallFunction
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "id": self.id,
            "type": self.type,
            "function": self.function.to_dict()
        }

