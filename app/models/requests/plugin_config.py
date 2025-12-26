"""
Plugin Configuration
"""
from typing import Optional, Dict, Any, Literal
from pydantic import BaseModel
from app.enums import PluginType, PDFEngine


class WebPluginConfig(BaseModel):
    """Web search plugin configuration"""
    engine: Optional[Literal["native", "exa"]] = None
    max_results: int = 5
    search_prompt: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {"max_results": self.max_results}
        if self.engine is not None:
            result["engine"] = self.engine
        if self.search_prompt is not None:
            result["search_prompt"] = self.search_prompt
        return result


class PDFPluginConfig(BaseModel):
    """PDF processing plugin configuration"""
    engine: PDFEngine = PDFEngine.MISTRAL_OCR
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {"engine": self.engine.value}


class ResponseHealingPluginConfig(BaseModel):
    """Response healing plugin configuration"""
    enabled: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {"enabled": self.enabled}


class PluginConfig(BaseModel):
    """Plugin configuration"""
    id: PluginType
    web: Optional[WebPluginConfig] = None
    pdf: Optional[PDFPluginConfig] = None
    enabled: Optional[bool] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {"id": self.id.value}
        if self.web is not None:
            result["web"] = self.web.to_dict()
        if self.pdf is not None:
            result["pdf"] = self.pdf.to_dict()
        if self.enabled is not None:
            result["enabled"] = self.enabled
        return result

