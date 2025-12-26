# Advanced Examples

## Tool Calling Workflow

```python
from app.models.tools import ToolDefinition, FunctionDefinition, FunctionParameter

# Define tool
weather_tool = ToolDefinition(
    type="function",
    function=FunctionDefinition(
        name="get_weather",
        description="Get weather for a location",
        parameters=FunctionParameter(
            type="object",
            properties={
                "location": {"type": "string"}
            },
            required=["location"]
        )
    )
)

# Use tool
request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_text("What's the weather in Boston?")
    .with_tools([weather_tool])
    .build())

response = await client.chat_completion(request)

# Process tool calls
from app.processors import ToolCallProcessor
processor = ToolCallProcessor()
tool_calls = processor.process_tool_calls(response)
```

## Reasoning Chain

```python
from app.enums import ReasoningEffort

request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_text("Solve: If a train travels 60 mph for 2 hours, how far does it go?")
    .with_reasoning(ReasoningEffort.HIGH)
    .build())

response = await client.chat_completion(request)

# Extract reasoning
from app.processors import ReasoningExtractor
extractor = ReasoningExtractor()
reasoning = extractor.extract_reasoning_text(response)
```

## Structured Output with Web Search

```python
schema = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "sources": {
            "type": "array",
            "items": {"type": "string"}
        }
    }
}

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("What are the latest AI developments?")
    .with_web_search(max_results=5)
    .with_structured_output(schema, name="AI_News")
    .build())
```

## Image Generation

```python
from app.enums import AspectRatio, ImageSize, OutputModality

request = (ChatRequestBuilder()
    .with_model("google/gemini-2.5-flash-image-preview")
    .with_text("Generate a beautiful sunset over mountains")
    .with_image_generation(
        aspect_ratio=AspectRatio.RATIO_16_9,
        image_size=ImageSize.SIZE_4K
    )
    .build())

response = await client.chat_completion(request)

# Extract images
from app.processors import ContentExtractor
extractor = ContentExtractor()
images = extractor.extract_images(response)
```

