"""
OpenRouter-specific exceptions
"""
from typing import Optional, Dict, Any


class OpenRouterException(Exception):
    """Base exception for OpenRouter errors"""
    def __init__(self, message: str, status_code: Optional[int] = None, details: Optional[Dict[str, Any]] = None):
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)


class OpenRouterAPIError(OpenRouterException):
    """OpenRouter API error"""
    pass


class OpenRouterRateLimitError(OpenRouterAPIError):
    """Rate limit error"""
    def __init__(self, message: str = "Rate limit exceeded", retry_after: Optional[int] = None):
        self.retry_after = retry_after
        super().__init__(message, status_code=429)


class OpenRouterAuthenticationError(OpenRouterAPIError):
    """Authentication error"""
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message, status_code=401)


class OpenRouterModelNotFoundError(OpenRouterAPIError):
    """Model not found error"""
    def __init__(self, model: str):
        super().__init__(f"Model not found: {model}", status_code=404)


class OpenRouterTimeoutError(OpenRouterAPIError):
    """Request timeout error"""
    def __init__(self, message: str = "Request timeout"):
        super().__init__(message, status_code=504)

