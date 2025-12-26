"""
Model Validator
"""
from app.validators.base_validator import BaseValidator, ValidationResult
from app.models.base import BaseRequest


class ModelValidator(BaseValidator):
    """Validate model"""
    
    def validate(self, request: BaseRequest) -> ValidationResult:
        """Validate model field"""
        errors = []
        
        if not hasattr(request, 'model') or not request.model:
            errors.append("Model is required")
        elif not isinstance(request.model, str):
            errors.append("Model must be a string")
        elif len(request.model.strip()) == 0:
            errors.append("Model cannot be empty")
        
        if errors:
            return ValidationResult(is_valid=False, errors=errors)
        
        return self._validate_next(request)

