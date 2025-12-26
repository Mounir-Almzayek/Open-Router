"""Custom exceptions"""
from app.exceptions.openrouter_exceptions import (
    OpenRouterException,
    OpenRouterAPIError,
    OpenRouterRateLimitError,
    OpenRouterAuthenticationError,
    OpenRouterModelNotFoundError,
    OpenRouterTimeoutError
)
from app.exceptions.validation_exceptions import (
    ValidationError,
    ModelValidationError,
    MessageValidationError,
    ContentValidationError,
    ProviderValidationError,
    ToolValidationError
)
from app.exceptions.client_exceptions import (
    ClientException,
    ConnectionError,
    TimeoutError,
    FileProcessingError,
    ContentBuilderError
)

__all__ = [
    "OpenRouterException",
    "OpenRouterAPIError",
    "OpenRouterRateLimitError",
    "OpenRouterAuthenticationError",
    "OpenRouterModelNotFoundError",
    "OpenRouterTimeoutError",
    "ValidationError",
    "ModelValidationError",
    "MessageValidationError",
    "ContentValidationError",
    "ProviderValidationError",
    "ToolValidationError",
    "ClientException",
    "ConnectionError",
    "TimeoutError",
    "FileProcessingError",
    "ContentBuilderError",
]
