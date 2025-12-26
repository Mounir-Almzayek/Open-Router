# Real-World Scenarios

## Customer Support Bot

```python
from app.builders import ChatRequestBuilder
from app.enums import ReasoningEffort

system_prompt = """You are a helpful customer support agent.
Be polite, professional, and try to solve customer issues."""

request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_system_prompt(system_prompt)
    .with_text("I can't log into my account")
    .with_reasoning(ReasoningEffort.MEDIUM)
    .build())
```

## Document Analysis System

```python
from app.enums import PDFEngine

request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_pdf_processing(PDFEngine.MISTRAL_OCR)
    .with_message(MessageRole.USER, [file_content])
    .with_text("Extract key points and create a summary")
    .with_structured_output(
        schema={
            "type": "object",
            "properties": {
                "summary": {"type": "string"},
                "key_points": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        },
        name="DocumentSummary"
    )
    .build())
```

## Content Generation Pipeline

```python
# Step 1: Research
research_request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Research topic: AI in healthcare")
    .with_web_search(max_results=10)
    .build())

# Step 2: Generate content
content_request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_text("Write an article based on the research")
    .with_reasoning(ReasoningEffort.HIGH)
    .build())
```

