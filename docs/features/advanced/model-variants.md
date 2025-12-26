# Model Variants

## Overview

Model variants are suffixes that modify model behavior, such as free tiers, extended context, or special modes.

## Available Variants

```python
from app.enums import ModelVariant

# Available variants:
ModelVariant.FREE        # :free - Free tier
ModelVariant.EXTENDED    # :extended - Extended context
ModelVariant.EXACTO     # :exacto - Exact matching
ModelVariant.THINKING   # :thinking - Thinking mode
ModelVariant.ONLINE     # :online - Online search
ModelVariant.NITRO      # :nitro - Fast mode
ModelVariant.FLOOR      # :floor - Lowest price
```

## Usage

### Free Tier
```python
from app.builders import ChatRequestBuilder
from app.enums import ModelVariant

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_model_variant(ModelVariant.FREE)
    .with_text("Hello!")
    .build())
# Model becomes: "openai/gpt-4o:free"
```

### Extended Context
```python
request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_model_variant(ModelVariant.EXTENDED)
    .with_text("Long document analysis...")
    .build())
# Model becomes: "anthropic/claude-sonnet-4:extended"
```

### Thinking Mode
```python
request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_model_variant(ModelVariant.THINKING)
    .with_text("Solve this complex problem")
    .build())
# Model becomes: "anthropic/claude-sonnet-4:thinking"
```

### Online Search
```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_model_variant(ModelVariant.ONLINE)
    .with_text("Latest news about AI")
    .build())
# Model becomes: "openai/gpt-4o:online"
```

## Variant Details

### :free
- Free tier access
- May have rate limits
- Good for testing
- Limited features

### :extended
- Extended context window
- Handle longer documents
- More tokens available
- Higher cost

### :exacto
- Exact matching mode
- Precise responses
- Less creative
- Good for structured data

### :thinking
- Shows reasoning process
- More detailed responses
- Slower generation
- Higher token usage

### :online
- Built-in web search
- Real-time information
- Automatic citations
- Additional cost

### :nitro
- Fast inference
- Lower latency
- Optimized for speed
- May have quality trade-offs

### :floor
- Lowest price option
- Cost optimization
- May use different providers
- Quality may vary

## Use Cases

### Development and Testing
```python
# Use free tier for testing
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_model_variant(ModelVariant.FREE)
    .with_text("Test query")
    .build())
```

### Long Documents
```python
# Use extended for long documents
request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_model_variant(ModelVariant.EXTENDED)
    .with_text("Analyze this 100-page document...")
    .build())
```

### Cost Optimization
```python
# Use floor for lowest cost
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_model_variant(ModelVariant.FLOOR)
    .with_text("Simple query")
    .build())
```

## Important Notes

- Not all models support all variants
- Variants may change model behavior significantly
- Some variants have additional costs
- Check model documentation for variant support

## Best Practices

1. **Use :free for testing** to reduce costs
2. **Use :extended for long documents** when needed
3. **Use :thinking for complex problems** requiring reasoning
4. **Use :floor for cost-sensitive applications**
5. **Test variants** to find the best for your use case

