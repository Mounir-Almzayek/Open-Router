# Provider Order

## Set Provider Order

Specify which providers to use and in what order.

```python
from app.builders import ChatRequestBuilder

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_provider_order(["anthropic", "openai", "google"])
    .build())
```

## How It Works

OpenRouter will try providers in the specified order:
1. First tries "anthropic"
2. If fails, tries "openai"
3. If fails, tries "google"

## With Fallbacks

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_provider_order(["anthropic", "openai"])
    .build())
```

If `allow_fallbacks` is enabled (default), OpenRouter will automatically try other providers if the specified ones fail.

## Use Cases

- **Cost Optimization**: Order by price
- **Performance**: Order by latency
- **Reliability**: Order by availability
- **Compliance**: Order by data policies

