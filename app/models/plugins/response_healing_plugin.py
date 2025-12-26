"""
Response Healing Plugin Model
"""
from typing import Dict, Any
from pydantic import BaseModel
from app.enums import PluginType


class ResponseHealingPlugin(BaseModel):
    """Response healing plugin"""
    id: PluginType = PluginType.RESPONSE_HEALING
    enabled: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "id": self.id.value,
            "enabled": self.enabled
        }

