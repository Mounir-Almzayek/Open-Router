# File Upload Examples

## Upload Image (Multipart)

```python
from fastapi import UploadFile, File
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole

@router.post("/analyze-image")
async def analyze_image(image: UploadFile = File(...)):
    builder = ChatRequestBuilder()
    builder.with_model("google/gemini-2.5-flash")
    
    image_content = await ContentBuilder.from_upload_file(image, "image")
    builder.with_message(MessageRole.USER, [image_content])
    builder.with_text("What is in this image?")
    
    request = builder.build()
    client = OpenRouterClient()
    response = await client.chat_completion(request)
    return response
```

## Upload Video

```python
@router.post("/describe-video")
async def describe_video(video: UploadFile = File(...)):
    video_content = await ContentBuilder.from_upload_file(video, "video")
    request = (ChatRequestBuilder()
        .with_model("google/gemini-2.5-flash")
        .with_message(MessageRole.USER, [video_content])
        .with_text("Describe this video")
        .build())
    
    client = OpenRouterClient()
    return await client.chat_completion(request)
```

## Upload PDF

```python
@router.post("/summarize-pdf")
async def summarize_pdf(file: UploadFile = File(...)):
    from app.enums import PDFEngine
    
    file_content = await ContentBuilder.from_upload_file(file, "file")
    request = (ChatRequestBuilder()
        .with_model("anthropic/claude-sonnet-4")
        .with_pdf_processing(PDFEngine.MISTRAL_OCR)
        .with_message(MessageRole.USER, [file_content])
        .with_text("Summarize this document")
        .build())
    
    client = OpenRouterClient()
    return await client.chat_completion(request)
```

## Multiple Files

```python
@router.post("/process-files")
async def process_files(
    image: UploadFile = File(None),
    pdf: UploadFile = File(None)
):
    content_parts = []
    
    if image:
        content_parts.append(await ContentBuilder.from_upload_file(image, "image"))
    if pdf:
        content_parts.append(await ContentBuilder.from_upload_file(pdf, "file"))
    
    request = (ChatRequestBuilder()
        .with_model("google/gemini-2.5-flash")
        .with_message(MessageRole.USER, content_parts)
        .with_text("Analyze these files")
        .build())
    
    client = OpenRouterClient()
    return await client.chat_completion(request)
```

