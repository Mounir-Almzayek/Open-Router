# Upload Files

## Feature Overview

The template supports direct file uploads from FastAPI requests without local storage. Files are processed in memory, encoded to base64, and sent directly to OpenRouter—eliminating the need for temporary file storage and simplifying file handling workflows. This feature enables seamless multimodal interactions with images, videos, audio, and documents.

*القالب يدعم رفع الملفات مباشرة من طلبات FastAPI دون تخزين محلي. الملفات تُعالج في الذاكرة، تُشفّر إلى base64، وتُرسل مباشرة إلى OpenRouter—مما يلغي الحاجة لتخزين الملفات المؤقت ويبسط سير عمل التعامل مع الملفات. هذه الميزة تتيح تفاعلات متعددة الوسائط سلسة مع الصور والفيديو والصوت والمستندات.*

## Feature Importance

Direct file uploads eliminate the complexity of file storage, management, and cleanup. By processing files in memory, the system avoids disk I/O, reduces latency, and simplifies deployment. This is essential for applications that need to handle user-uploaded content efficiently and securely.

*رفع الملفات المباشر يلغي تعقيد تخزين الملفات وإدارتها والتنظيف. من خلال معالجة الملفات في الذاكرة، يتجنب النظام I/O القرص ويقلل زمن الانتظار ويبسط النشر. هذا ضروري للتطبيقات التي تحتاج إلى التعامل مع المحتوى المرفوع من المستخدم بكفاءة وأمان.*

## Methods

### 1. Multipart/Form-Data

```python
from fastapi import UploadFile, File
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole

@router.post("/upload")
async def upload_image(image: UploadFile = File(...)):
    builder = ChatRequestBuilder()
    builder.with_model("google/gemini-2.5-flash")
    
    # Process upload file directly
    image_content = await ContentBuilder.from_upload_file(image, "image")
    builder.with_message(MessageRole.USER, [image_content])
    
    request = builder.build()
    # Send to OpenRouter
```

### 2. Using the Multimodal Endpoint

```python
# POST /api/v1/chat/completions/multimodal
# multipart/form-data
files = {
    'image': ('image.jpg', open('image.jpg', 'rb'), 'image/jpeg'),
    'text': (None, 'What is in this image?'),
    'model': (None, 'google/gemini-2.5-flash'),
}
```

## Supported File Types

- **Images**: JPEG, PNG, WEBP, GIF
- **Videos**: MP4, MPEG, MOV, WEBM
- **Audio**: WAV, MP3, AIFF, AAC, OGG, FLAC, M4A
- **Files**: PDF

## File Size Limits

- Default: 50MB
- Videos: 100MB
- Configurable in `app/config.py`

## Key Benefits

### No Local Storage
Files are processed in memory without saving to disk, eliminating storage management, cleanup, and security concerns. This simplifies deployment and reduces infrastructure requirements.

*الملفات تُعالج في الذاكرة دون حفظ على القرص، مما يلغي إدارة التخزين والتنظيف ومخاوف الأمان. هذا يبسط النشر ويقلل متطلبات البنية التحتية.*

### Simplified Workflow
Direct processing eliminates intermediate file handling steps. Files flow directly from user upload to API request, reducing complexity and potential failure points.

*المعالجة المباشرة تلغي خطوات التعامل مع الملفات المتوسطة. الملفات تتدفق مباشرة من رفع المستخدم إلى طلب API، مما يقلل التعقيد ونقاط الفشل المحتملة.*

### Security
In-memory processing reduces attack surface by avoiding file system access. Files never touch disk, reducing risks of unauthorized access or data persistence.

*المعالجة في الذاكرة تقلل سطح الهجوم عن طريق تجنب الوصول إلى نظام الملفات. الملفات لا تلمس القرص أبداً، مما يقلل مخاطر الوصول غير المصرح به أو استمرارية البيانات.*

## Direct Processing

Files are processed in memory without saving to disk:
*الملفات تُعالج في الذاكرة دون حفظ على القرص:*

1. Read from `UploadFile`
   *اقرأ من `UploadFile`*
2. Encode to base64
   *شفر إلى base64*
3. Create data URL
   *أنشئ عنوان URL للبيانات*
4. Send directly to OpenRouter
   *أرسل مباشرة إلى OpenRouter*

