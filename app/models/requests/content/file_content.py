"""
File Content Model
"""
from typing import Dict, Any, Optional
from pydantic import BaseModel
from app.enums import ContentType
from app.models.requests.content.base_content import BaseContent


class FileData(BaseModel):
    """File data configuration"""
    filename: str
    file_data: str  # URL or base64 data URL
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "filename": self.filename,
            "file_data": self.file_data
        }


class FileContent(BaseContent):
    """File content (PDF, etc.)"""
    type: ContentType = ContentType.FILE
    file: FileData
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "type": self.type.value,
            "file": self.file.to_dict()
        }

