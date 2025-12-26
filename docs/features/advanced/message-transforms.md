# Message Transforms

## Overview

Message transforms allow you to optimize message content, such as compressing long conversations using middle-out compression.

## Middle-Out Compression

Middle-out compression keeps the first and last messages intact while compressing the middle messages. This is useful for long conversations that exceed context limits.

## Enable Middle-Out Compression

```python
from app.builders import ChatRequestBuilder
from app.enums import TransformType

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Long conversation...")
    .with_middle_out_compression()
    .build())
```

## How It Works

1. **First message** (usually system prompt) - Kept intact
2. **Middle messages** - Compressed/truncated
3. **Last message** (current user input) - Kept intact

## Use Cases

### Long Conversations
When conversation history is too long:

```python
# Without compression - may exceed context
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_system_prompt("You are a helpful assistant")
    .with_text("Message 1")
    .with_text("Message 2")
    # ... many messages ...
    .with_text("Current query")
    .build())

# With compression - fits in context
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_system_prompt("You are a helpful assistant")
    .with_text("Message 1")
    .with_text("Message 2")
    # ... many messages ...
    .with_text("Current query")
    .with_middle_out_compression()
    .build())
```

### Context Window Optimization
Optimize context window usage:

```python
request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_system_prompt("Long system prompt...")
    .with_text("User message 1")
    .with_text("User message 2")
    # ... 50+ messages ...
    .with_text("Latest query")
    .with_middle_out_compression()
    .build())
```

## Compression Details

### What Gets Compressed
- Middle messages in the conversation
- Long content is truncated
- Summary information is preserved when possible

### What Stays Intact
- First message (system prompt)
- Last message (current input)
- Important context markers

## Example

```python
# Original conversation (too long)
messages = [
    {"role": "system", "content": "You are helpful"},  # Kept
    {"role": "user", "content": "Message 1"},          # Compressed
    {"role": "assistant", "content": "Response 1"},    # Compressed
    {"role": "user", "content": "Message 2"},         # Compressed
    {"role": "assistant", "content": "Response 2"},    # Compressed
    {"role": "user", "content": "Current query"}      # Kept
]

# After middle-out compression
# System prompt: Kept
# Middle messages: Compressed/Summarized
# Current query: Kept
```

## Important Notes

- Compression may lose some context
- Best for conversations with clear start/end
- Not suitable when all messages are important
- Test compression impact on your use case

## Best Practices

1. **Use for long conversations** that exceed context limits
2. **Keep important messages** at the start or end
3. **Test compression quality** to ensure acceptable results
4. **Combine with extended context** when available
5. **Monitor token usage** to optimize compression

## Alternative Approaches

### Manual Truncation
```python
# Manually truncate old messages
old_messages = messages[1:-1]  # Remove first and last
truncated = [msg[:500] for msg in old_messages]  # Truncate
```

### Summary Messages
```python
# Summarize old conversation
summary = "Previous conversation about topic X..."
request = builder.with_text(f"Context: {summary}\n\nCurrent: {query}").build()
```

