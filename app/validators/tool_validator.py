"""
Tool Validator
"""
from app.validators.base_validator import BaseValidator, ValidationResult
from app.models.base import BaseRequest
from app.models.tools import ToolDefinition


class ToolValidator(BaseValidator):
    """Validate tools configuration"""
    
    def validate(self, request: BaseRequest) -> ValidationResult:
        """Validate tools"""
        errors = []
        
        if hasattr(request, 'tools') and request.tools:
            if not isinstance(request.tools, list):
                errors.append("Tools must be a list")
            else:
                for i, tool in enumerate(request.tools):
                    if not isinstance(tool, ToolDefinition):
                        errors.append(f"Tool {i}: Must be a ToolDefinition")
                    else:
                        # Validate tool structure
                        if not tool.function:
                            errors.append(f"Tool {i}: Function is required")
                        elif not tool.function.name:
                            errors.append(f"Tool {i}: Function name is required")
                        elif not tool.function.description:
                            errors.append(f"Tool {i}: Function description is required")
                        elif not tool.function.parameters:
                            errors.append(f"Tool {i}: Function parameters are required")
        
        if errors:
            return ValidationResult(is_valid=False, errors=errors)
        
        return self._validate_next(request)

