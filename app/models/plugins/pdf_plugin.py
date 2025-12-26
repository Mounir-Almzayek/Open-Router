"""
PDF Processing Plugin Model
"""
from typing import Dict, Any
from pydantic import BaseModel
from app.enums import PluginType, PDFEngine


class PDFPlugin(BaseModel):
    """PDF processing plugin"""
    id: PluginType = PluginType.FILE_PARSER
    engine: PDFEngine = PDFEngine.MISTRAL_OCR
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "id": self.id.value,
            "pdf": {
                "engine": self.engine.value
            }
        }

