"""
Audio Content Model
"""
from typing import Dict, Any
from pydantic import BaseModel
from app.enums import ContentType, AudioFormat
from app.models.requests.content.base_content import BaseContent


class InputAudio(BaseModel):
    """Input audio configuration"""
    data: str  # Base64 encoded audio
    format: AudioFormat
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "data": self.data,
            "format": self.format.value
        }


class AudioContent(BaseContent):
    """Audio content"""
    type: ContentType = ContentType.INPUT_AUDIO
    input_audio: InputAudio
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "type": self.type.value,
            "input_audio": self.input_audio.to_dict()
        }

