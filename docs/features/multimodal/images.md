# Images

## Feature Overview

Image processing enables AI models to see, analyze, and understand visual content. This feature allows you to send images to AI models for analysis, description, extraction, and various computer vision tasks. Images can be provided via URLs, base64 encoding, or direct file uploads, making it flexible for different use cases.

*معالجة الصور تمكن نماذج الذكاء الاصطناعي من رؤية وتحليل وفهم المحتوى المرئي. تتيح لك هذه الميزة إرسال الصور إلى نماذج الذكاء الاصطناعي للتحليل والوصف والاستخراج ومهام رؤية الكمبيوتر المختلفة. يمكن توفير الصور عبر عناوين URL أو ترميز base64 أو رفع الملفات مباشرة، مما يجعلها مرنة لحالات استخدام مختلفة.*

## Feature Importance

Visual understanding is a fundamental capability that enables countless applications—from content moderation and accessibility features to medical image analysis and autonomous systems. Image processing transforms AI from text-only systems to multimodal assistants that can understand the visual world around us.

*الفهم البصري هو قدرة أساسية تمكن عدد لا يحصى من التطبيقات—من إدارة المحتوى وميزات إمكانية الوصول إلى تحليل الصور الطبية والأنظمة المستقلة. معالجة الصور تحول الذكاء الاصطناعي من أنظمة نصية فقط إلى مساعدين متعددين الوسائط يمكنهم فهم العالم المرئي من حولنا.*

## Key Benefits

### Visual Content Analysis
AI models can analyze images to extract information, identify objects, read text (OCR), understand scenes, and describe visual content. This enables applications that need to understand visual information.

*يمكن لنماذج الذكاء الاصطناعي تحليل الصور لاستخراج المعلومات وتحديد الكائنات وقراءة النص (OCR) وفهم المشاهد ووصف المحتوى المرئي. هذا يتيح التطبيقات التي تحتاج إلى فهم المعلومات المرئية.*

### Accessibility Features
Image analysis enables accessibility features like automatic image descriptions for visually impaired users, making digital content more accessible and inclusive.

*تحليل الصور يتيح ميزات إمكانية الوصول مثل الأوصاف التلقائية للصور للمستخدمين ضعاف البصر، مما يجعل المحتوى الرقمي أكثر سهولة في الوصول وشاملاً.*

### Content Moderation
AI can analyze images to detect inappropriate content, verify authenticity, identify objects or people, and enforce content policies automatically at scale.

*يمكن للذكاء الاصطناعي تحليل الصور لاكتشاف المحتوى غير المناسب والتحقق من الأصالة وتحديد الكائنات أو الأشخاص وإنفاذ سياسات المحتوى تلقائياً على نطاق واسع.*

### Document Processing
Images of documents can be analyzed to extract text, understand structure, identify forms, and process visual documents without manual data entry.

*يمكن تحليل صور المستندات لاستخراج النص وفهم الهيكل وتحديد النماذج ومعالجة المستندات المرئية دون إدخال بيانات يدوي.*

### Multimodal Understanding
Combining images with text enables rich interactions where AI can understand context, answer questions about images, and provide detailed analysis based on both visual and textual information.

*دمج الصور مع النص يتيح تفاعلات غنية حيث يمكن للذكاء الاصطناعي فهم السياق والإجابة على الأسئلة حول الصور وتوفير تحليل مفصل بناءً على المعلومات المرئية والنصية.*

## Use Cases

### E-commerce Product Analysis
Analyze product images to extract features, compare products, generate descriptions, and provide visual search capabilities. Customers can upload images to find similar products.

*حلل صور المنتجات لاستخراج الميزات ومقارنة المنتجات وإنشاء الأوصاف وتوفير قدرات البحث المرئي. يمكن للعملاء رفع الصور للعثور على منتجات مماثلة.*

### Medical Image Analysis
Assist healthcare professionals by analyzing medical images (X-rays, MRIs, scans) to identify anomalies, provide preliminary assessments, and support diagnostic workflows.

*ساعد المهنيين الصحيين من خلال تحليل الصور الطبية (الأشعة السينية، التصوير بالرنين المغناطيسي، الفحوصات) لتحديد الشذوذ وتوفير التقييمات الأولية ودعم سير عمل التشخيص.*

### Content Moderation Systems
Automatically detect inappropriate content, verify image authenticity, identify prohibited items, and enforce community guidelines at scale without manual review.

*اكتشف تلقائياً المحتوى غير المناسب والتحقق من أصالة الصورة وتحديد العناصر المحظورة وإنفاذ إرشادات المجتمع على نطاق واسع دون مراجعة يدوية.*

### Accessibility Tools
Generate automatic image descriptions for screen readers, making websites and applications accessible to visually impaired users. Describe images in detail for better understanding.

*أنشئ أوصاف صور تلقائية لقارئات الشاشة، مما يجعل المواقع والتطبيقات قابلة للوصول للمستخدمين ضعاف البصر. صف الصور بالتفصيل لفهم أفضل.*

### Educational Content
Analyze diagrams, charts, graphs, and educational images to explain concepts, extract information, and provide learning support for students studying visual materials.

*حلل المخططات والرسوم البيانية والصور التعليمية لشرح المفاهيم واستخراج المعلومات وتوفير دعم التعلم للطلاب الذين يدرسون المواد المرئية.*

## Performance Considerations

### Image Size Impact
Larger images consume more tokens and processing time. High-resolution images provide more detail but significantly increase costs. Use appropriate image sizes based on your needs—often medium resolution is sufficient.

*الصور الأكبر تستهلك المزيد من الرموز المميزة ووقت المعالجة. الصور عالية الدقة توفر المزيد من التفاصيل لكنها تزيد التكاليف بشكل كبير. استخدم أحجام صور مناسبة بناءً على احتياجاتك—غالباً ما تكون الدقة المتوسطة كافية.*

### Detail Level Configuration
Image detail levels (low, high, auto) control how much detail the model processes. Low detail is faster and cheaper but may miss fine details. High detail is more accurate but costs more. Auto balances based on image size.

*مستويات تفاصيل الصورة (منخفض، عالي، تلقائي) تتحكم في مقدار التفاصيل التي يعالجها النموذج. التفاصيل المنخفضة أسرع وأرخص لكنها قد تفوت التفاصيل الدقيقة. التفاصيل العالية أكثر دقة لكنها تكلف أكثر. التلقائي يوازن بناءً على حجم الصورة.*

### Format Optimization
Different image formats have different sizes and quality. JPEG is smaller but lossy, PNG is larger but lossless. Choose formats based on your quality requirements and cost constraints.

*تنسيقات الصور المختلفة لها أحجام وجودة مختلفة. JPEG أصغر لكنه بخسارة، PNG أكبر لكنه بدون فقدان. اختر التنسيقات بناءً على متطلبات الجودة وقيود التكلفة.*

### Batch Processing
Processing multiple images sequentially can be slow. Consider parallel processing for multiple images, but be mindful of rate limits and costs. Some use cases may benefit from combining multiple images in a single request.

*معالجة صور متعددة بشكل تسلسلي يمكن أن تكون بطيئة. فكر في المعالجة المتوازية لصور متعددة، لكن كن حذراً من حدود المعدل والتكاليف. بعض حالات الاستخدام قد تستفيد من دمج صور متعددة في طلب واحد.*

## Cost Implications

### Token Consumption
Images consume significantly more tokens than text. A single high-resolution image can consume thousands of tokens. Detail level directly affects token consumption—high detail uses more tokens than low detail.

*الصور تستهلك رموزاً مميزة أكثر بكثير من النص. صورة واحدة عالية الدقة يمكن أن تستهلك آلاف الرموز المميزة. مستوى التفاصيل يؤثر مباشرة على استهلاك الرموز المميزة—التفاصيل العالية تستخدم رموزاً مميزة أكثر من التفاصيل المنخفضة.*

### Resolution and Cost
Higher resolution images cost more because they contain more pixels and require more processing. Optimize image resolution based on actual needs—don't use maximum resolution unless necessary.

*الصور عالية الدقة تكلف أكثر لأنها تحتوي على المزيد من البكسل وتتطلب المزيد من المعالجة. قم بتحسين دقة الصورة بناءً على الاحتياجات الفعلية—لا تستخدم الدقة القصوى ما لم يكن ضرورياً.*

### Detail Level Costs
High detail level can cost 2-4x more than low detail for the same image. Use high detail only when fine details are critical. For most use cases, auto or low detail provides good results at lower cost.

*مستوى التفاصيل العالي يمكن أن يكلف 2-4 مرات أكثر من التفاصيل المنخفضة لنفس الصورة. استخدم التفاصيل العالية فقط عندما تكون التفاصيل الدقيقة حرجة. لمعظم حالات الاستخدام، التلقائي أو التفاصيل المنخفضة توفر نتائج جيدة بتكلفة أقل.*

### Format Impact
Base64 encoding increases file size by ~33%, which increases token consumption. Using URLs instead of base64 can reduce costs for large images, as the model downloads them directly.

*ترميز base64 يزيد حجم الملف بنحو 33%، مما يزيد استهلاك الرموز المميزة. استخدام عناوين URL بدلاً من base64 يمكن أن يقلل التكاليف للصور الكبيرة، حيث يقوم النموذج بتنزيلها مباشرة.*

## Best Practices

### Image Size Optimization
Resize images to appropriate dimensions before sending. Most use cases don't need full-resolution images. A good rule of thumb is 1024x1024 pixels for most analyses, scaling up only when fine details are critical.

*قم بتغيير حجم الصور إلى أبعاد مناسبة قبل الإرسال. معظم حالات الاستخدام لا تحتاج صور بدقة كاملة. قاعدة جيدة هي 1024x1024 بكسل لمعظم التحليلات، مع التكبير فقط عندما تكون التفاصيل الدقيقة حرجة.*

### Detail Level Selection
Use "auto" detail level for most cases—it balances quality and cost automatically. Use "low" for simple object detection or when cost is critical. Use "high" only when fine details like text or small objects are important.

*استخدم مستوى التفاصيل "تلقائي" لمعظم الحالات—إنه يوازن الجودة والتكلفة تلقائياً. استخدم "منخفض" لاكتشاف الكائنات البسيطة أو عندما تكون التكلفة حرجة. استخدم "عالي" فقط عندما تكون التفاصيل الدقيقة مثل النص أو الكائنات الصغيرة مهمة.*

### Format Choice
Use JPEG for photographs and complex images where some quality loss is acceptable. Use PNG for images with text, diagrams, or when lossless quality is needed. Use WEBP for web applications when supported.

*استخدم JPEG للصور الفوتوغرافية والصور المعقدة حيث يكون فقدان الجودة مقبولاً. استخدم PNG للصور مع النص أو المخططات أو عندما تكون الجودة بدون فقدان مطلوبة. استخدم WEBP للتطبيقات الويب عند الدعم.*

### URL vs Base64
Use URLs for images already hosted online—this avoids encoding overhead and reduces request size. Use base64 for local images or when URLs aren't available. For large images (>5MB), prefer URLs.

*استخدم عناوين URL للصور المستضافة بالفعل على الإنترنت—هذا يتجنب حمل الترميز ويقلل حجم الطلب. استخدم base64 للصور المحلية أو عندما لا تكون عناوين URL متاحة. للصور الكبيرة (>5MB)، افضل عناوين URL.*

### Combining with Text
Provide context with text prompts when analyzing images. Clear instructions help the model focus on relevant aspects and produce better results. Combine image analysis with structured outputs for data extraction.

*وفر السياق مع مطالب النص عند تحليل الصور. التعليمات الواضحة تساعد النموذج على التركيز على الجوانب ذات الصلة وإنتاج نتائج أفضل. اجمع تحليل الصور مع المخرجات المنظمة لاستخراج البيانات.*

## When NOT to Use

### Don't Use High Detail Unnecessarily
Avoid high detail level unless fine details are critical. High detail significantly increases costs without always improving results. Most use cases work well with auto or low detail.

*تجنب مستوى التفاصيل العالي ما لم تكن التفاصيل الدقيقة حرجة. التفاصيل العالية تزيد التكاليف بشكل كبير دون تحسين النتائج دائماً. معظم حالات الاستخدام تعمل بشكل جيد مع التلقائي أو التفاصيل المنخفضة.*

### Don't Send Oversized Images
Avoid sending full-resolution images when smaller sizes would suffice. Oversized images waste tokens and money without providing proportional value. Always resize images before sending.

*تجنب إرسال صور بدقة كاملة عندما تكون الأحجام الأصغر كافية. الصور كبيرة الحجم تهدر الرموز المميزة والمال دون توفير قيمة متناسبة. قم دائماً بتغيير حجم الصور قبل الإرسال.*

### Don't Use Base64 for Large Images
Avoid base64 encoding for images larger than 5MB. Base64 increases size by 33% and makes requests very large. Use URLs or file uploads for large images instead.

*تجنب ترميز base64 للصور الأكبر من 5MB. base64 يزيد الحجم بنسبة 33% ويجعل الطلبات كبيرة جداً. استخدم عناوين URL أو رفع الملفات للصور الكبيرة بدلاً من ذلك.*

### Don't Process Images Without Context
Avoid sending images without accompanying text prompts. Without context, the model may not understand what analysis you need. Always provide clear instructions about what to analyze or extract.

*تجنب إرسال الصور دون مطالب نصية مصاحبة. بدون السياق، قد لا يفهم النموذج التحليل الذي تحتاجه. وفر دائماً تعليمات واضحة حول ما يجب تحليله أو استخراجه.*

## Troubleshooting

### Images Not Processing
If images aren't being processed, verify the model supports image inputs. Check image format is supported (JPEG, PNG, WEBP, GIF). Ensure images are properly encoded (base64 or valid URL). Check file size limits.

*إذا لم تتم معالجة الصور، تحقق من أن النموذج يدعم مدخلات الصور. تحقق من أن تنسيق الصورة مدعوم (JPEG، PNG، WEBP، GIF). تأكد من ترميز الصور بشكل صحيح (base64 أو URL صالح). تحقق من حدود حجم الملف.*

### High Token Costs
If token costs are high, review image sizes and detail levels. Resize images to appropriate dimensions. Use lower detail levels when possible. Consider using URLs instead of base64 for large images.

*إذا كانت تكاليف الرموز المميزة عالية، راجع أحجام الصور ومستويات التفاصيل. قم بتغيير حجم الصور إلى أبعاد مناسبة. استخدم مستويات تفاصيل أقل عند الإمكان. فكر في استخدام عناوين URL بدلاً من base64 للصور الكبيرة.*

### Poor Analysis Results
If analysis results are poor, try increasing detail level (if cost allows). Provide clearer text prompts with specific instructions. Ensure images are clear and not corrupted. Consider using models specifically trained for vision tasks.

*إذا كانت نتائج التحليل ضعيفة، جرب زيادة مستوى التفاصيل (إذا سمحت التكلفة). وفر مطالب نصية أوضح مع تعليمات محددة. تأكد من أن الصور واضحة وغير تالفة. فكر في استخدام النماذج المدربة خصيصاً لمهام الرؤية.*

### URL Access Issues
If URLs aren't accessible, ensure images are publicly accessible (not behind authentication). Check URL format is correct (https://). Verify the server allows direct access. Some providers may have restrictions on URL sources.

*إذا لم تكن عناوين URL قابلة للوصول، تأكد من أن الصور قابلة للوصول العام (ليست خلف المصادقة). تحقق من أن تنسيق URL صحيح (https://). تحقق من أن الخادم يسمح بالوصول المباشر. بعض المزودين قد يكون لديهم قيود على مصادر URL.*

## Basic Usage

### From URL

*من URL*

```python
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole

image_content = ContentBuilder.from_url("https://example.com/image.jpg", "image")
request = (ChatRequestBuilder()
    .with_model("google/gemini-2.5-flash")
    .with_message(MessageRole.USER, [image_content])
    .with_text("What is in this image?")
    .build())
```

### From Base64

*من Base64*

```python
import base64

with open("image.jpg", "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode('utf-8')
    data_url = f"data:image/jpeg;base64,{image_base64}"

image_content = ContentBuilder.from_base64_string(data_url, "image", "image/jpeg")
```

### From Upload File

*من ملف مرفوع*

```python
from fastapi import UploadFile

async def process_image(upload_file: UploadFile):
    image_content = await ContentBuilder.from_upload_file(upload_file, "image")
    request = (ChatRequestBuilder()
        .with_model("google/gemini-2.5-flash")
        .with_message(MessageRole.USER, [image_content])
        .build())
```

### Image Detail

*تفاصيل الصورة*

```python
from app.models.requests.content import ImageURL, ImageContent

image_url = ImageURL(url="https://example.com/image.jpg", detail="high")
image_content = ImageContent(image_url=image_url)
```

Detail options: `"low"`, `"high"`, `"auto"`

*خيارات التفاصيل: `"low"`، `"high"`، `"auto"`*

## Advanced Examples

### Image Analysis with Structured Output

*تحليل الصور مع إخراج منظم*

```python
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole

image_content = ContentBuilder.from_url("https://example.com/product.jpg", "image")

request = (ChatRequestBuilder()
    .with_model("google/gemini-2.5-flash")
    .with_message(MessageRole.USER, [image_content])
    .with_text("Extract product information from this image")
    .with_structured_output(
        schema={
            "type": "object",
            "properties": {
                "product_name": {"type": "string"},
                "price": {"type": "string"},
                "brand": {"type": "string"},
                "description": {"type": "string"}
            }
        },
        name="ProductInfo"
    )
    .build())
```

### Multiple Images Analysis

*تحليل صور متعددة*

```python
from app.models.requests.content import TextContent, ImageContent
from app.builders import ContentBuilder

image1 = ContentBuilder.from_url("https://example.com/image1.jpg", "image")
image2 = ContentBuilder.from_url("https://example.com/image2.jpg", "image")
text = TextContent(text="Compare these two images and describe the differences")

request = (ChatRequestBuilder()
    .with_model("google/gemini-2.5-flash")
    .with_message(MessageRole.USER, [text, image1, image2])
    .build())
```

### Image OCR with High Detail

*OCR للصور مع تفاصيل عالية*

```python
from app.models.requests.content import ImageURL, ImageContent

# High detail for text extraction
image_url = ImageURL(url="https://example.com/document.jpg", detail="high")
image_content = ImageContent(image_url=image_url)

request = (ChatRequestBuilder()
    .with_model("google/gemini-2.5-flash")
    .with_message(MessageRole.USER, [image_content])
    .with_text("Extract all text from this image")
    .build())
```
