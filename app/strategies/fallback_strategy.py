"""
Fallback Strategy
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.requests import ChatRequest


class FallbackStrategy(ABC):
    """Strategy for fallback handling"""
    
    @abstractmethod
    def get_fallback_model(self, original_model: str, attempt: int) -> Optional[str]:
        """Get fallback model"""
        pass


class ModelListFallbackStrategy(FallbackStrategy):
    """Fallback using model list"""
    
    def __init__(self, fallback_models: List[str]):
        self.fallback_models = fallback_models
    
    def get_fallback_model(self, original_model: str, attempt: int) -> Optional[str]:
        """Get fallback model from list"""
        if attempt <= len(self.fallback_models):
            return self.fallback_models[attempt - 1]
        return None


class ProviderFallbackStrategy(FallbackStrategy):
    """Fallback using provider routing"""
    
    def get_fallback_model(self, original_model: str, attempt: int) -> Optional[str]:
        """Provider fallback is handled by OpenRouter automatically"""
        return None

