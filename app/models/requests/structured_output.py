"""
Structured Output Configuration
"""
from typing import Dict, Any, Literal, Optional
from pydantic import BaseModel


class JSONSchemaConfig(BaseModel):
    """JSON Schema configuration"""
    name: str
    strict: bool = True
    schema: Dict[str, Any]  # JSON Schema
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "name": self.name,
            "strict": self.strict,
            "schema": self.schema
        }


class ResponseFormatConfig(BaseModel):
    """Response format configuration"""
    type: Literal["json_object", "json_schema"]
    json_schema: Optional[JSONSchemaConfig] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {"type": self.type}
        if self.json_schema is not None:
            result["json_schema"] = self.json_schema.to_dict()
        return result

