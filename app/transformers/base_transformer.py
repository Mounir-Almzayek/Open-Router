"""
Base Transformer
"""
from abc import ABC, abstractmethod
from app.models.base import BaseRequest


class BaseTransformer(ABC):
    """Base transformer"""
    
    @abstractmethod
    def transform(self, request: BaseRequest) -> BaseRequest:
        """Transform request"""
        pass

