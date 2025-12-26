"""
Base Processor Class
"""
from abc import ABC, abstractmethod
from typing import Any
from app.models.responses import BaseResponse


class BaseResponseProcessor(ABC):
    """Base processor for responses"""
    
    @abstractmethod
    def process(self, response: BaseResponse) -> Any:
        """Process response"""
        pass

