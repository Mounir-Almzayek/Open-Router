# Base64 Encoding

## Feature Overview

Base64 encoding allows you to send file content directly in JSON requests without using multipart/form-data. This enables embedding images, videos, audio, and documents directly in JSON payloads, making it convenient for API integrations and programmatic file handling. Base64 encoding increases file size by approximately 33% but provides a simple way to include binary data in text-based formats.

*ترميز Base64 يسمح لك بإرسال محتوى الملف مباشرة في طلبات JSON دون استخدام multipart/form-data. هذا يتيح تضمين الصور والفيديو والصوت والمستندات مباشرة في حمولات JSON، مما يجعلها مريحة لتكاملات API والتعامل مع الملفات برمجياً. ترميز Base64 يزيد حجم الملف بنحو 33% لكنه يوفر طريقة بسيطة لتضمين البيانات الثنائية في التنسيقات القائمة على النص.*

## Feature Importance

Base64 encoding is essential for embedding binary data in JSON requests, enabling seamless file transmission in API calls. While it increases payload size, it simplifies integration by allowing all data to be sent in a single JSON request without multipart encoding complexity.

*ترميز Base64 ضروري لتضمين البيانات الثنائية في طلبات JSON، مما يتيح نقل الملفات السلس في استدعاءات API. بينما يزيد حجم الحمولة، فإنه يبسط التكامل عن طريق السماح بإرسال جميع البيانات في طلب JSON واحد دون تعقيد ترميز multipart.*

## Basic Usage

### Encode File to Base64

```python
import base64

# Read and encode file
with open("image.jpg", "rb") as f:
    file_data = f.read()
    base64_data = base64.b64encode(file_data).decode('utf-8')
    data_url = f"data:image/jpeg;base64,{base64_data}"
```

### Use in Request

```python
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole

# Create content from base64
image_content = ContentBuilder.from_base64_string(
    data_url,
    "image",
    "image/jpeg"
)

request = (ChatRequestBuilder()
    .with_model("google/gemini-2.5-flash")
    .with_message(MessageRole.USER, [image_content])
    .with_text("What is in this image?")
    .build())
```

## Data URL Format

Base64 data URLs follow this format:
```
data:<mime_type>;base64,<base64_encoded_data>
```

Examples:
- `data:image/jpeg;base64,/9j/4AAQSkZJRg...`
- `data:video/mp4;base64,AAAAIGZ0eXBpc29t...`
- `data:application/pdf;base64,JVBERi0xLjQK...`

## Using DirectFileHandler

```python
from app.utils.file_handler import DirectFileHandler

# Process base64 string
base64_string = "iVBORw0KGgoAAAANSUhEUg..."
data_url = DirectFileHandler.process_base64_string(
    base64_string,
    mime_type="image/png"
)
```

## Complete Example

```python
import base64
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole

# Encode image
with open("photo.jpg", "rb") as f:
    image_data = f.read()
    base64_encoded = base64.b64encode(image_data).decode('utf-8')
    data_url = f"data:image/jpeg;base64,{base64_encoded}"

# Create request
image_content = ContentBuilder.from_base64_string(
    data_url,
    "image",
    "image/jpeg"
)

request = (ChatRequestBuilder()
    .with_model("google/gemini-2.5-flash")
    .with_message(MessageRole.USER, [image_content])
    .with_text("Analyze this image")
    .build())
```

## Supported File Types

### Images
- JPEG: `data:image/jpeg;base64,...`
- PNG: `data:image/png;base64,...`
- WEBP: `data:image/webp;base64,...`
- GIF: `data:image/gif;base64,...`

### Videos
- MP4: `data:video/mp4;base64,...`
- WEBM: `data:video/webm;base64,...`

### Audio
- WAV: `data:audio/wav;base64,...`
- MP3: `data:audio/mpeg;base64,...`

### Documents
- PDF: `data:application/pdf;base64,...`

## Important Notes

- Base64 increases file size by ~33%
- Large files may exceed request size limits
- Use for files under 10MB in JSON requests
- For larger files, use multipart/form-data

## Best Practices

1. **Use for small files** (< 10MB)
2. **Include MIME type** for proper handling
3. **Validate base64** before sending
4. **Consider file size** when choosing encoding method
5. **Use multipart** for large files

## Utilities

```python
from app.utils.encoders import encode_to_base64, create_data_url

# Encode bytes
data = b"file content"
base64_str = encode_to_base64(data)

# Create data URL
data_url = create_data_url(data, "image/jpeg")
```

