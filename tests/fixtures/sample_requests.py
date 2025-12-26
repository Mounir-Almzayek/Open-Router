"""
Sample request fixtures for testing
"""
from app.builders import ChatRequestBuilder
from app.enums import MessageRole, ReasoningEffort
from app.models.requests.content import TextContent, ImageContent, ImageURL


def get_basic_request():
    """Get basic chat request"""
    builder = ChatRequestBuilder()
    return builder.with_model("openai/gpt-4o").with_text("Hello!").build()


def get_request_with_system():
    """Get request with system prompt"""
    builder = ChatRequestBuilder()
    return (builder
        .with_model("openai/gpt-4o")
        .with_system_prompt("You are a helpful assistant.")
        .with_text("Hello!")
        .build())


def get_multimodal_request():
    """Get multimodal request"""
    builder = ChatRequestBuilder()
    text = TextContent(text="What is in this image?")
    image = ImageContent(image_url=ImageURL(url="https://example.com/image.jpg"))
    
    return (builder
        .with_model("google/gemini-2.5-flash")
        .with_message(MessageRole.USER, [text, image])
        .build())


def get_request_with_reasoning():
    """Get request with reasoning"""
    builder = ChatRequestBuilder()
    return (builder
        .with_model("anthropic/claude-sonnet-4")
        .with_text("Solve this problem")
        .with_reasoning(ReasoningEffort.HIGH)
        .build())


def get_request_with_web_search():
    """Get request with web search"""
    builder = ChatRequestBuilder()
    return (builder
        .with_model("openai/gpt-4o")
        .with_text("Latest AI news")
        .with_web_search(max_results=5)
        .build())

