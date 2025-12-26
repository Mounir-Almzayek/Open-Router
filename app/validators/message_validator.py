"""
Message Validator
"""
from app.validators.base_validator import BaseValidator, ValidationResult
from app.models.base import BaseRequest


class MessageValidator(BaseValidator):
    """Validate messages"""
    
    def validate(self, request: BaseRequest) -> ValidationResult:
        """Validate messages"""
        errors = []
        
        if not hasattr(request, 'messages') or not request.messages:
            errors.append("At least one message is required")
        elif not isinstance(request.messages, list):
            errors.append("Messages must be a list")
        elif len(request.messages) == 0:
            errors.append("At least one message is required")
        else:
            # Validate each message
            for i, message in enumerate(request.messages):
                if not hasattr(message, 'role'):
                    errors.append(f"Message {i}: role is required")
                if not hasattr(message, 'content'):
                    errors.append(f"Message {i}: content is required")
        
        if errors:
            return ValidationResult(is_valid=False, errors=errors)
        
        return self._validate_next(request)

