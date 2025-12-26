"""
Pytest configuration and fixtures
"""
import pytest
from typing import AsyncGenerator
from app.services import OpenRouterClient
from app.builders import ChatRequestBuilder
from app.models.requests import ChatRequest, Message
from app.enums import MessageRole


@pytest.fixture
def api_key():
    """Test API key"""
    return "test-api-key"


@pytest.fixture
def openrouter_client(api_key):
    """OpenRouter client fixture"""
    return OpenRouterClient(api_key=api_key, base_url="https://openrouter.ai/api/v1")


@pytest.fixture
def chat_request():
    """Basic chat request fixture"""
    builder = ChatRequestBuilder()
    return builder.with_model("openai/gpt-4o").with_text("Hello!").build()


@pytest.fixture
def chat_request_with_system():
    """Chat request with system prompt"""
    builder = ChatRequestBuilder()
    return (builder
        .with_model("openai/gpt-4o")
        .with_system_prompt("You are a helpful assistant.")
        .with_text("Hello!")
        .build())


@pytest.fixture
def streaming_request():
    """Streaming request fixture"""
    builder = ChatRequestBuilder()
    return (builder
        .with_model("openai/gpt-4o")
        .with_text("Tell me a story")
        .with_streaming(True)
        .build())


@pytest.fixture
def multimodal_request():
    """Multimodal request fixture"""
    from app.models.requests.content import TextContent, ImageContent, ImageURL
    
    builder = ChatRequestBuilder()
    text = TextContent(text="What is in this image?")
    image = ImageContent(image_url=ImageURL(url="https://example.com/image.jpg"))
    
    return (builder
        .with_model("google/gemini-2.5-flash")
        .with_message(MessageRole.USER, [text, image])
        .build())


@pytest.fixture
def tool_request():
    """Request with tools fixture"""
    from app.models.tools import ToolDefinition, FunctionDefinition, FunctionParameter
    
    tool = ToolDefinition(
        type="function",
        function=FunctionDefinition(
            name="get_weather",
            description="Get weather",
            parameters=FunctionParameter(
                type="object",
                properties={"location": {"type": "string"}},
                required=["location"]
            )
        )
    )
    
    builder = ChatRequestBuilder()
    return (builder
        .with_model("anthropic/claude-sonnet-4")
        .with_text("What's the weather?")
        .with_tools([tool])
        .build())

