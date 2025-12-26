"""
Validator Chain
"""
from app.validators.base_validator import BaseValidator, ValidationResult
from app.validators.model_validator import ModelValidator
from app.validators.message_validator import MessageValidator
from app.validators.content_validator import ContentValidator
from app.validators.provider_validator import ProviderValidator
from app.validators.tool_validator import ToolValidator
from app.models.base import BaseRequest


class ValidatorChain:
    """Validator chain using Chain of Responsibility pattern"""
    
    def __init__(self):
        """Initialize validator chain"""
        self._first = ModelValidator()
        self._first.set_next(
            MessageValidator()
        ).set_next(
            ContentValidator()
        ).set_next(
            ProviderValidator()
        ).set_next(
            ToolValidator()
        )
    
    def validate(self, request: BaseRequest) -> ValidationResult:
        """Validate request through chain"""
        return self._first.validate(request)
    
    def add_validator(self, validator: BaseValidator) -> 'ValidatorChain':
        """Add custom validator to chain"""
        # Find last validator
        current = self._first
        while current._next:
            current = current._next
        current.set_next(validator)
        return self

