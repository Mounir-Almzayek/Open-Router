"""
Base Builder Class
"""
from abc import ABC
from typing import TypeVar, Generic
from app.models.base import BaseRequest

T = TypeVar('T', bound=BaseRequest)


class BaseRequestBuilder(ABC, Generic[T]):
    """Base builder for requests"""
    
    def __init__(self):
        self._request: T = None
    
    def build(self) -> T:
        """Build and return request"""
        if self._request is None:
            raise ValueError("Request not initialized")
        return self._request
    
    def reset(self) -> 'BaseRequestBuilder':
        """Reset builder"""
        self._request = None
        return self

