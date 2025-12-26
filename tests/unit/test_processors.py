"""
Unit tests for processors
"""
import pytest
from app.processors import ContentExtractor, UsageAnalyzer, ReasoningExtractor
from app.models.responses import ChatResponse, ChoiceResponse, MessageResponse, Usage


class TestContentExtractor:
    """Tests for ContentExtractor"""
    
    def test_extract_text(self):
        """Test text extraction"""
        message = MessageResponse(role="assistant", content="Hello!")
        choice = ChoiceResponse(index=0, message=message)
        response = ChatResponse(choices=[choice])
        
        extractor = ContentExtractor()
        text = extractor.extract_text(response)
        
        assert text == "Hello!"
    
    def test_extract_empty_text(self):
        """Test extraction when no content"""
        message = MessageResponse(role="assistant", content=None)
        choice = ChoiceResponse(index=0, message=message)
        response = ChatResponse(choices=[choice])
        
        extractor = ContentExtractor()
        text = extractor.extract_text(response)
        
        assert text == ""


class TestUsageAnalyzer:
    """Tests for UsageAnalyzer"""
    
    def test_analyze_usage(self):
        """Test usage analysis"""
        usage = Usage(
            prompt_tokens=100,
            completion_tokens=50,
            total_tokens=150
        )
        
        analyzer = UsageAnalyzer()
        analysis = analyzer.analyze_usage(usage)
        
        assert analysis["prompt_tokens"] == 100
        assert analysis["completion_tokens"] == 50
        assert analysis["total_tokens"] == 150

