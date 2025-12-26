# Quantizations

## Overview

Quantization levels control the precision of model weights, affecting model size, speed, and quality.

## Available Quantization Levels

```python
from app.enums import Quantization

# Supported quantizations:
# - INT4: 4-bit integer
# - INT8: 8-bit integer
# - FP4: 4-bit floating point
# - FP6: 6-bit floating point
# - FP8: 8-bit floating point
# - FP16: 16-bit floating point
# - BF16: Brain float 16
# - FP32: 32-bit floating point (full precision)
```

## Filter by Quantization

```python
from app.models.requests import ProviderConfig
from app.enums import Quantization

provider_config = ProviderConfig(
    quantizations=[Quantization.FP8, Quantization.FP16]
)

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Hello!")
    .build())
request.provider = provider_config
```

## Use Cases

### Performance Optimization
Use lower precision for faster inference:
```python
provider_config = ProviderConfig(
    quantizations=[Quantization.FP8, Quantization.FP16]
)
```

### Quality Priority
Use higher precision for better quality:
```python
provider_config = ProviderConfig(
    quantizations=[Quantization.FP32, Quantization.BF16]
)
```

### Cost Optimization
Lower precision models are often cheaper:
```python
provider_config = ProviderConfig(
    quantizations=[Quantization.INT8, Quantization.FP8]
)
```

## Trade-offs

| Quantization | Speed | Quality | Cost |
|--------------|-------|---------|------|
| INT4 | Fastest | Lower | Cheapest |
| INT8 | Fast | Lower | Cheap |
| FP8 | Medium | Medium | Medium |
| FP16 | Slower | Higher | Higher |
| FP32 | Slowest | Highest | Highest |

## Important Notes

- Not all models support all quantization levels
- Lower precision may reduce output quality
- Some quantizations are provider-specific
- Check model documentation for supported quantizations

## Best Practices

1. **Start with FP16** for a good balance
2. **Use FP8** for faster inference when quality is acceptable
3. **Use FP32** only when maximum quality is required
4. **Test different quantizations** to find the best balance for your use case

