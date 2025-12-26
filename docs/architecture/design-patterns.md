# Design Patterns

## Builder Pattern

### Purpose
Create complex requests in an easy and flexible way.

### Implementation
```python
from app.builders import ChatRequestBuilder

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Hello!")
    .with_web_search(max_results=5)
    .with_reasoning(ReasoningEffort.HIGH)
    .build())
```

### Benefits
- Fluent API
- Method chaining
- Type-safe
- Easy to extend

## Strategy Pattern

### Purpose
Select providers and retry strategies.

### Implementation
```python
from app.strategies import ExponentialBackoffStrategy, RetryStrategy

strategy = ExponentialBackoffStrategy()
# Used in retry decorator
```

### Benefits
- Flexible retry logic
- Easy to swap strategies
- Testable

## Decorator Pattern

### Purpose
For retry, caching, logging.

### Implementation
```python
from app.decorators import retry_on_failure, log_request

@retry_on_failure(max_attempts=3)
@log_request
async def chat_completion(request):
    ...
```

### Benefits
- Separation of concerns
- Reusable functionality
- Clean code

## Chain of Responsibility

### Purpose
For validation.

### Implementation
```python
from app.validators import ValidatorChain

validator = ValidatorChain()
result = validator.validate(request)
```

### Benefits
- Modular validation
- Easy to add new validators
- Clear error messages

## Factory Pattern

### Purpose
Create different objects based on input.

### Implementation
```python
from app.templates import TextTemplate, ImageTemplate

# Factory creates appropriate template
template = create_template(type="image", prompt="...")
```

### Benefits
- Encapsulation
- Easy to extend
- Type safety

