# Data Collection Policies

## Overview

Data collection policies control whether providers can collect and use your data for training or other purposes.

## Available Policies

### Allow
Allow providers to collect data (default behavior).

```python
from app.builders import ChatRequestBuilder
from app.enums import DataCollection

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("User query")
    .with_data_collection(DataCollection.ALLOW)
    .build())
```

### Deny
Prevent providers from collecting data.

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Sensitive information")
    .with_data_collection(DataCollection.DENY)
    .build())
```

## Use Cases

### Privacy-Sensitive Applications
```python
request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_text("Patient medical information")
    .with_data_collection(DataCollection.DENY)
    .with_zdr(enabled=True)
    .build())
```

### Compliance Requirements
For GDPR, HIPAA, or other privacy regulations:
- Use `DataCollection.DENY` to prevent data collection
- Combine with ZDR for maximum privacy

## Important Notes

- Not all providers support data collection policies
- Denying data collection may have cost implications
- Some providers require data collection for certain features
- Check provider documentation for specific support

## Best Practices

1. **Default to DENY** for sensitive applications
2. **Use ALLOW** only when necessary for specific features
3. **Combine with ZDR** for maximum privacy protection
4. **Document your policy** in your application

