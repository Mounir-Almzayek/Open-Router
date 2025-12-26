"""
Unit tests for validators
"""
import pytest
from app.validators import ValidatorChain, ValidationResult
from app.models.requests import ChatRequest
from app.builders import ChatRequestBuilder
from app.exceptions import ValidationError


class TestValidatorChain:
    """Tests for ValidatorChain"""
    
    def test_valid_request(self):
        """Test validation of valid request"""
        builder = ChatRequestBuilder()
        request = builder.with_model("openai/gpt-4o").with_text("Hello!").build()
        
        validator = ValidatorChain()
        result = validator.validate(request)
        
        assert result.is_valid is True
        assert len(result.errors) == 0
    
    def test_missing_model(self):
        """Test validation fails when model is missing"""
        request = ChatRequest(model="", messages=[], stream=False)
        
        validator = ValidatorChain()
        result = validator.validate(request)
        
        assert result.is_valid is False
        assert len(result.errors) > 0
    
    def test_missing_messages(self):
        """Test validation fails when messages are missing"""
        request = ChatRequest(model="openai/gpt-4o", messages=[], stream=False)
        
        validator = ValidatorChain()
        result = validator.validate(request)
        
        assert result.is_valid is False
        assert any("message" in error.lower() for error in result.errors)

