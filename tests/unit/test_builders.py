"""
Unit tests for builders
"""
import pytest
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole, ReasoningEffort, PluginType, PDFEngine
from app.models.requests.content import TextContent, ImageContent


class TestChatRequestBuilder:
    """Tests for ChatRequestBuilder"""
    
    def test_basic_build(self):
        """Test basic request building"""
        builder = ChatRequestBuilder()
        request = builder.with_model("openai/gpt-4o").with_text("Hello!").build()
        
        assert request.model == "openai/gpt-4o"
        assert len(request.messages) == 1
        assert request.messages[0].role == MessageRole.USER.value
    
    def test_system_prompt(self):
        """Test system prompt"""
        builder = ChatRequestBuilder()
        request = (builder
            .with_model("openai/gpt-4o")
            .with_system_prompt("You are helpful")
            .with_text("Hello!")
            .build())
        
        assert len(request.messages) == 2
        assert request.messages[0].role == MessageRole.SYSTEM.value
    
    def test_streaming(self):
        """Test streaming"""
        builder = ChatRequestBuilder()
        request = builder.with_model("openai/gpt-4o").with_streaming(True).build()
        
        assert request.stream is True
    
    def test_generation_params(self):
        """Test generation parameters"""
        builder = ChatRequestBuilder()
        request = (builder
            .with_model("openai/gpt-4o")
            .with_temperature(0.7)
            .with_max_tokens(500)
            .with_top_p(0.9)
            .build())
        
        assert request.temperature == 0.7
        assert request.max_tokens == 500
        assert request.top_p == 0.9
    
    def test_web_search_plugin(self):
        """Test web search plugin"""
        builder = ChatRequestBuilder()
        request = (builder
            .with_model("openai/gpt-4o")
            .with_web_search(max_results=5)
            .build())
        
        assert request.plugins is not None
        assert len(request.plugins) == 1
        assert request.plugins[0].id == PluginType.WEB
    
    def test_pdf_processing(self):
        """Test PDF processing"""
        builder = ChatRequestBuilder()
        request = builder.with_pdf_processing(PDFEngine.MISTRAL_OCR).build()
        
        assert request.plugins is not None
        assert len(request.plugins) == 1
        assert request.plugins[0].id == PluginType.FILE_PARSER
    
    def test_reasoning(self):
        """Test reasoning"""
        builder = ChatRequestBuilder()
        request = builder.with_reasoning(ReasoningEffort.HIGH).build()
        
        assert request.reasoning is not None
        assert request.reasoning.effort == ReasoningEffort.HIGH
    
    def test_model_fallbacks(self):
        """Test model fallbacks"""
        builder = ChatRequestBuilder()
        request = builder.with_model_fallbacks("model1", "model2").build()
        
        assert request.models == ["model1", "model2"]
    
    def test_provider_order(self):
        """Test provider order"""
        builder = ChatRequestBuilder()
        request = builder.with_provider_order(["provider1", "provider2"]).build()
        
        assert request.provider is not None
        assert request.provider.order == ["provider1", "provider2"]
    
    def test_zdr(self):
        """Test ZDR"""
        builder = ChatRequestBuilder()
        request = builder.with_zdr(True).build()
        
        assert request.provider is not None
        assert request.provider.zdr is True


class TestContentBuilder:
    """Tests for ContentBuilder"""
    
    def test_from_url_image(self):
        """Test creating image content from URL"""
        content = ContentBuilder.from_url("https://example.com/image.jpg", "image")
        
        assert isinstance(content, ImageContent)
        assert content.image_url.url == "https://example.com/image.jpg"
    
    def test_from_base64_string(self):
        """Test creating content from base64"""
        base64_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="
        data_url = f"data:image/png;base64,{base64_data}"
        
        content = ContentBuilder.from_base64_string(data_url, "image", "image/png")
        
        assert isinstance(content, ImageContent)
        assert content.image_url.url.startswith("data:image/png;base64,")

