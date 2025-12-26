# OpenRouter FastAPI Template

A comprehensive FastAPI template for OpenRouter API with full feature support, OOP design patterns, and direct file handling.

## Features

- ✅ Full OpenRouter API support
- ✅ OOP design patterns (Builder, Factory, Strategy, Decorator, Chain of Responsibility)
- ✅ Direct file handling from FastAPI requests (no local storage)
- ✅ Comprehensive Enums for all constants
- ✅ Advanced request/response models with validation
- ✅ Template system for prompt management
- ✅ Provider routing and fallback strategies
- ✅ Plugin support (Web Search, PDF Processing, Response Healing)
- ✅ Tool/Function calling
- ✅ Reasoning tokens support
- ✅ Structured outputs (JSON Schema)
- ✅ Prompt caching
- ✅ Image generation
- ✅ Message transforms (middle-out compression)
- ✅ Error handling and retry logic
- ✅ Monitoring and observability

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and configure:

```bash
OPENROUTER_API_KEY=your_api_key_here
```

## Usage

### Basic Chat

```python
from app.builders import ChatRequestBuilder
from app.services import OpenRouterClient

builder = ChatRequestBuilder()
request = builder.with_model("openai/gpt-4o").with_text("Hello!").build()

client = OpenRouterClient()
response = await client.chat_completion(request)
print(response.choices[0].message.content)
```

### With File Upload

```python
from fastapi import UploadFile
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole

builder = ChatRequestBuilder()
builder.with_model("google/gemini-2.5-flash")

# Upload image
image_content = await ContentBuilder.from_upload_file(upload_file, "image")
builder.with_message(MessageRole.USER, [image_content])

request = builder.build()
response = await client.chat_completion(request)
```

### With Advanced Features

```python
builder = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_text("What are the latest AI developments?")
    .with_web_search(max_results=5)
    .with_reasoning(ReasoningEffort.HIGH)
    .with_structured_output(schema={...}, name="AI_News")
    .with_zdr(enabled=True)
    .build())
```

## API Endpoints

- `POST /api/v1/chat/completions` - Chat completions
- `POST /api/v1/chat/completions/stream` - Streaming completions
- `POST /api/v1/chat/completions/multimodal` - Multimodal with file uploads
- `GET /api/v1/models` - List available models
- `GET /health` - Health check

## Running

```bash
uvicorn app.main:app --reload
```

## Documentation

See `docs/` directory for comprehensive documentation.
