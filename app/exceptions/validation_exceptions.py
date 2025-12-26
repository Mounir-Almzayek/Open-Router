"""
Validation exceptions
"""
from typing import List


class ValidationError(Exception):
    """Validation error"""
    def __init__(self, errors: List[str]):
        self.errors = errors
        message = "Validation failed: " + "; ".join(errors)
        super().__init__(message)


class ModelValidationError(ValidationError):
    """Model validation error"""
    pass


class MessageValidationError(ValidationError):
    """Message validation error"""
    pass


class ContentValidationError(ValidationError):
    """Content validation error"""
    pass


class ProviderValidationError(ValidationError):
    """Provider validation error"""
    pass


class ToolValidationError(ValidationError):
    """Tool validation error"""
    pass

