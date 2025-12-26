"""
Message Transform Configuration
"""
from typing import List, Dict, Any
from pydantic import BaseModel
from app.enums import TransformType


class TransformConfig(BaseModel):
    """Message transform configuration"""
    transforms: List[TransformType]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "transforms": [t.value for t in self.transforms]
        }

