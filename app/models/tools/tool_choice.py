"""
Tool Choice Configuration
"""
from typing import Dict, Any, Literal, Optional, Union
from pydantic import BaseModel


class ToolChoiceFunction(BaseModel):
    """Tool choice function configuration"""
    name: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {"name": self.name}


class ToolChoiceConfig(BaseModel):
    """Tool choice configuration"""
    type: Literal["none", "auto", "function"]
    function: Optional[ToolChoiceFunction] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {"type": self.type}
        if self.function is not None:
            result["function"] = self.function.to_dict()
        return result

