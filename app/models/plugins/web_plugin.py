"""
Web Search Plugin Model
"""
from typing import Dict, Any
from pydantic import BaseModel
from app.enums import PluginType


class WebPlugin(BaseModel):
    """Web search plugin"""
    id: PluginType = PluginType.WEB
    engine: str = "exa"  # "native" or "exa"
    max_results: int = 5
    search_prompt: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {
            "id": self.id.value,
            "engine": self.engine,
            "max_results": self.max_results
        }
        if self.search_prompt is not None:
            result["search_prompt"] = self.search_prompt
        return result

