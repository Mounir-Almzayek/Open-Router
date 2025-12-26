"""
Base Validator
"""
from abc import ABC, abstractmethod
from typing import Optional, List
from app.models.base import BaseRequest


class ValidationResult:
    """Validation result"""
    def __init__(self, is_valid: bool, errors: List[str] = None):
        self.is_valid = is_valid
        self.errors = errors or []


class BaseValidator(ABC):
    """Base validator"""
    _next: Optional['BaseValidator'] = None
    
    def set_next(self, validator: 'BaseValidator') -> 'BaseValidator':
        """Set next validator in chain"""
        self._next = validator
        return validator
    
    @abstractmethod
    def validate(self, request: BaseRequest) -> ValidationResult:
        """Validate request"""
        pass
    
    def _validate_next(self, request: BaseRequest) -> ValidationResult:
        """Validate with next validator"""
        if self._next:
            return self._next.validate(request)
        return ValidationResult(is_valid=True, errors=[])

