"""
Provider Validator
"""
from app.validators.base_validator import BaseValidator, ValidationResult
from app.models.base import BaseRequest
from app.models.requests import ProviderConfig


class ProviderValidator(BaseValidator):
    """Validate provider configuration"""
    
    def validate(self, request: BaseRequest) -> ValidationResult:
        """Validate provider config"""
        errors = []
        
        if hasattr(request, 'provider') and request.provider:
            provider = request.provider
            if isinstance(provider, ProviderConfig):
                # Validate provider order
                if provider.order is not None:
                    if not isinstance(provider.order, list):
                        errors.append("Provider order must be a list")
                    elif len(provider.order) == 0:
                        errors.append("Provider order cannot be empty")
                
                # Validate quantizations
                if provider.quantizations is not None:
                    if not isinstance(provider.quantizations, list):
                        errors.append("Quantizations must be a list")
        
        if errors:
            return ValidationResult(is_valid=False, errors=errors)
        
        return self._validate_next(request)

