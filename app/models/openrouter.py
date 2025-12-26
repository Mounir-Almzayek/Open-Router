"""
OpenRouter API Models (Models API, Credits API, etc.)
"""
from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class ModelInfo(BaseModel):
    """Model information from Models API"""
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    context_length: Optional[int] = None
    architecture: Optional[Dict[str, Any]] = None
    pricing: Optional[Dict[str, Any]] = None
    top_provider: Optional[Dict[str, Any]] = None
    supported_parameters: Optional[List[str]] = None


class CreditsInfo(BaseModel):
    """Credits information"""
    credits: Optional[float] = None
    usage: Optional[float] = None

