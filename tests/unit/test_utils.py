"""
Unit tests for utilities
"""
import pytest
from app.utils.file_handler import DirectFileHandler
from app.utils.url_validator import is_valid_url, is_data_url
from app.utils.encoders import encode_to_base64, create_data_url


class TestDirectFileHandler:
    """Tests for DirectFileHandler"""
    
    def test_encode_to_base64(self):
        """Test base64 encoding"""
        content = b"test content"
        mime_type = "text/plain"
        
        data_url = DirectFileHandler.encode_to_base64(content, mime_type)
        
        assert data_url.startswith("data:text/plain;base64,")
        assert "dGVzdCBjb250ZW50" in data_url
    
    def test_process_base64_string(self):
        """Test processing base64 string"""
        base64_data = "dGVzdA=="
        mime_type = "text/plain"
        
        data_url = DirectFileHandler.process_base64_string(base64_data, mime_type)
        
        assert data_url == f"data:{mime_type};base64,{base64_data}"
    
    def test_process_data_url(self):
        """Test processing existing data URL"""
        data_url = "data:image/png;base64,iVBORw0KGgo="
        
        result = DirectFileHandler.process_base64_string(data_url)
        
        assert result == data_url


class TestURLValidator:
    """Tests for URL validator"""
    
    def test_valid_url(self):
        """Test valid URL"""
        assert is_valid_url("https://example.com") is True
        assert is_valid_url("http://example.com") is True
    
    def test_invalid_url(self):
        """Test invalid URL"""
        assert is_valid_url("not-a-url") is False
        assert is_valid_url("") is False
    
    def test_data_url(self):
        """Test data URL detection"""
        assert is_data_url("data:image/png;base64,...") is True
        assert is_data_url("https://example.com") is False


class TestEncoders:
    """Tests for encoders"""
    
    def test_encode_to_base64(self):
        """Test base64 encoding"""
        data = b"test"
        encoded = encode_to_base64(data)
        
        assert encoded == "dGVzdA=="
    
    def test_create_data_url(self):
        """Test data URL creation"""
        data = b"test"
        mime_type = "text/plain"
        data_url = create_data_url(data, mime_type)
        
        assert data_url.startswith("data:text/plain;base64,")
        assert "dGVzdA==" in data_url

