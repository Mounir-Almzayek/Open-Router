"""
Tool Definition Models
"""
from typing import Dict, Any, Literal, Optional, List
from pydantic import BaseModel
from app.enums import ToolType


class FunctionParameter(BaseModel):
    """Function parameter schema"""
    type: str
    properties: Optional[Dict[str, Any]] = None
    required: Optional[List[str]] = None
    additionalProperties: Optional[bool] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {"type": self.type}
        if self.properties is not None:
            result["properties"] = self.properties
        if self.required is not None:
            result["required"] = self.required
        if self.additionalProperties is not None:
            result["additionalProperties"] = self.additionalProperties
        return result


class FunctionDefinition(BaseModel):
    """Function definition"""
    name: str
    description: str
    parameters: FunctionParameter
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters.to_dict()
        }


class ToolDefinition(BaseModel):
    """Tool definition"""
    type: ToolType = ToolType.FUNCTION
    function: FunctionDefinition
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "type": self.type.value,
            "function": self.function.to_dict()
        }

