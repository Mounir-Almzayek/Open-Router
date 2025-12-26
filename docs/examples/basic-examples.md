# Basic Examples

## Simple Chat

```python
from app.builders import ChatRequestBuilder
from app.services import OpenRouterClient

# Build request
builder = ChatRequestBuilder()
request = builder.with_model("openai/gpt-4o").with_text("Hello!").build()

# Send request
client = OpenRouterClient()
response = await client.chat_completion(request)

# Get response
print(response.choices[0].message.content)
```

## Chat with System Prompt

```python
request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_system_prompt("You are a helpful assistant.")
    .with_text("What is Python?")
    .build())

response = await client.chat_completion(request)
```

## Streaming Response

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Tell me a story")
    .with_streaming(True)
    .build())

async for chunk in client.stream_chat_completion(request):
    print(chunk.choices[0].delta.content, end="", flush=True)
```

## Generation Parameters

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Write a poem")
    .with_temperature(0.7)
    .with_max_tokens(500)
    .with_top_p(0.9)
    .build())
```

