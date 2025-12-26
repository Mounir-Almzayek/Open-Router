# Multimodal Examples

## Image Analysis

```python
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole

# From URL
image_content = ContentBuilder.from_url("https://example.com/image.jpg", "image")
request = (ChatRequestBuilder()
    .with_model("google/gemini-2.5-flash")
    .with_message(MessageRole.USER, [image_content])
    .with_text("What is in this image?")
    .build())
```

## Video Description

```python
video_content = ContentBuilder.from_url("https://example.com/video.mp4", "video")
request = (ChatRequestBuilder()
    .with_model("google/gemini-2.5-flash")
    .with_message(MessageRole.USER, [video_content])
    .with_text("Describe this video")
    .build())
```

## Audio Transcription

```python
# From base64
audio_content = ContentBuilder.from_base64_string(
    base64_data, "audio", "audio/wav"
)
request = (ChatRequestBuilder()
    .with_model("openai/whisper-large-v3")
    .with_message(MessageRole.USER, [audio_content])
    .build())
```

## PDF Processing

```python
from app.enums import PDFEngine

file_content = ContentBuilder.from_url("https://example.com/doc.pdf", "file")
request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_pdf_processing(PDFEngine.MISTRAL_OCR)
    .with_message(MessageRole.USER, [file_content])
    .with_text("Summarize this document")
    .build())
```

