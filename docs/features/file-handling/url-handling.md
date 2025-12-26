# URL Handling

## Feature Overview

You can send files to OpenRouter by providing URLs instead of uploading files directly. This is useful for files already hosted online, eliminating the need to upload files and reducing request payload sizes. URLs enable efficient handling of large files and files already available on the web.

*يمكنك إرسال الملفات إلى OpenRouter عن طريق توفير عناوين URL بدلاً من رفع الملفات مباشرة. هذا مفيد للملفات المستضافة بالفعل على الإنترنت، مما يلغي الحاجة لرفع الملفات ويقلل أحجام حمولات الطلبات. عناوين URL تمكن التعامل الفعال مع الملفات الكبيرة والملفات المتاحة بالفعل على الويب.*

## Feature Importance

URL handling is essential for efficient file processing, especially for large files or files already hosted online. Using URLs avoids encoding overhead, reduces request sizes, and enables processing of files without local access.

*التعامل مع URL ضروري لمعالجة الملفات الفعالة، خاصة للملفات الكبيرة أو الملفات المستضافة بالفعل على الإنترنت. استخدام عناوين URL يتجنب حمل الترميز ويقلل أحجام الطلبات ويمكن معالجة الملفات دون وصول محلي.*

## Basic Usage

### Image from URL

```python
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole

image_content = ContentBuilder.from_url(
    "https://example.com/image.jpg",
    "image"
)

request = (ChatRequestBuilder()
    .with_model("google/gemini-2.5-flash")
    .with_message(MessageRole.USER, [image_content])
    .with_text("What is in this image?")
    .build())
```

### Video from URL

```python
video_content = ContentBuilder.from_url(
    "https://example.com/video.mp4",
    "video"
)

request = (ChatRequestBuilder()
    .with_model("google/gemini-2.5-flash")
    .with_message(MessageRole.USER, [video_content])
    .with_text("Describe this video")
    .build())
```

### PDF from URL

```python
file_content = ContentBuilder.from_url(
    "https://example.com/document.pdf",
    "file"
)

request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_message(MessageRole.USER, [file_content])
    .with_text("Summarize this document")
    .build())
```

## URL Validation

The system automatically validates URLs:

```python
from app.utils.url_validator import is_valid_url

# Check if URL is valid
if is_valid_url("https://example.com/image.jpg"):
    # Use URL
    pass
```

## Supported URL Schemes

- `https://` - HTTPS URLs
- `http://` - HTTP URLs (less secure)

## Use Cases

### Public Images
```python
# Use public image URLs
image_url = "https://example.com/public/photo.jpg"
image_content = ContentBuilder.from_url(image_url, "image")
```

### CDN Resources
```python
# Use CDN URLs for faster access
cdn_url = "https://cdn.example.com/video.mp4"
video_content = ContentBuilder.from_url(cdn_url, "video")
```

### Document Links
```python
# Use document URLs
doc_url = "https://docs.example.com/report.pdf"
file_content = ContentBuilder.from_url(doc_url, "file")
```

## URL Requirements

1. **Publicly accessible** - URL must be accessible from OpenRouter servers
2. **Valid format** - Must be a valid HTTP/HTTPS URL
3. **Supported format** - File must be in a supported format
4. **Size limits** - Subject to provider file size limits

## Important Notes

- URLs must be publicly accessible
- Private URLs or authentication may not work
- File size limits apply to URL-based files
- Some providers may download files before processing

## Best Practices

1. **Use HTTPS** for secure file access
2. **Ensure public access** to URLs
3. **Validate URLs** before sending requests
4. **Use CDN** for better performance
5. **Handle errors** for inaccessible URLs

## Error Handling

```python
from app.utils.url_validator import is_valid_url
from app.exceptions import ContentBuilderError

try:
    if not is_valid_url(url):
        raise ValueError("Invalid URL format")
    
    content = ContentBuilder.from_url(url, "image")
except ContentBuilderError as e:
    # Handle error
    print(f"Failed to create content: {e}")
```

## Comparison: URL vs Upload

### Use URLs when:
- Files are already hosted online
- Files are large (> 50MB)
- You want to avoid encoding overhead
- Files are publicly accessible

### Use Upload when:
- Files are local
- Files are private
- You need direct control
- Files are small (< 50MB)

