# Files/PDFs

## Feature Overview

File and PDF processing enables AI models to read, analyze, and extract information from document files. This feature allows you to send PDF documents to AI models for text extraction, document analysis, summarization, and information retrieval. PDFs can be processed using different engines optimized for various document types.

*معالجة الملفات وPDF تمكن نماذج الذكاء الاصطناعي من قراءة وتحليل واستخراج المعلومات من ملفات المستندات. تتيح لك هذه الميزة إرسال مستندات PDF إلى نماذج الذكاء الاصطناعي لاستخراج النص وتحليل المستندات والتلخيص واسترجاع المعلومات. يمكن معالجة ملفات PDF باستخدام محركات مختلفة محسّنة لأنواع المستندات المختلفة.*

## Feature Importance

Document processing is essential for applications that need to extract information from files, analyze documents, and understand structured content. From legal document analysis and research paper summarization to form processing and data extraction, PDF processing enables automation of document-heavy workflows.

*معالجة المستندات ضرورية للتطبيقات التي تحتاج إلى استخراج المعلومات من الملفات وتحليل المستندات وفهم المحتوى المنظم. من تحليل المستندات القانونية وتلخيص أوراق البحث إلى معالجة النماذج واستخراج البيانات، معالجة PDF تمكن أتمتة سير العمل الثقيل بالمستندات.*

## Key Benefits

### Text Extraction
PDF processing engines can extract text from documents, including scanned documents using OCR (Optical Character Recognition). This makes document content searchable and analyzable, even for image-based PDFs.

*محركات معالجة PDF يمكنها استخراج النص من المستندات، بما في ذلك المستندات الممسوحة ضوئياً باستخدام OCR (التعرف الضوئي على الأحرف). هذا يجعل محتوى المستندات قابلاً للبحث والتحليل، حتى لملفات PDF القائمة على الصور.*

### Document Analysis
AI models can analyze document structure, extract key information, understand context, and provide insights. This enables automated document review, summarization, and information extraction.

*يمكن لنماذج الذكاء الاصطناعي تحليل هيكل المستند واستخراج المعلومات الرئيسية وفهم السياق وتوفير الرؤى. هذا يتيح مراجعة المستندات الآلية والتلخيص واستخراج المعلومات.*

### Multiple Processing Engines
Different PDF engines are optimized for different document types—Mistral OCR for scanned documents, PDF Text for text-based PDFs, and Native for provider-optimized processing. This flexibility ensures optimal results for various document types.

*محركات PDF المختلفة محسّنة لأنواع المستندات المختلفة—Mistral OCR للمستندات الممسوحة ضوئياً، PDF Text لملفات PDF القائمة على النص، وNative للمعالجة المحسّنة من المزود. هذه المرونة تضمن نتائج مثلى لأنواع المستندات المختلفة.*

### Structured Data Extraction
PDF processing can extract structured data from documents, forms, and tables. Combined with structured outputs, this enables automated data entry and form processing.

*معالجة PDF يمكنها استخراج البيانات المنظمة من المستندات والنماذج والجداول. مجتمعة مع المخرجات المنظمة، هذا يتيح إدخال البيانات الآلي ومعالجة النماذج.*

### Multimodal Understanding
PDFs can contain both text and images. AI models can understand both, enabling comprehensive document analysis that considers visual elements alongside textual content.

*ملفات PDF يمكن أن تحتوي على النص والصور. يمكن لنماذج الذكاء الاصطناعي فهم كليهما، مما يتيح تحليل مستندات شامل يأخذ في الاعتبار العناصر المرئية إلى جانب المحتوى النصي.*

## Use Cases

### Legal Document Analysis
Analyze legal documents, contracts, and agreements to extract key terms, identify clauses, summarize content, and answer questions. This enables faster legal document review and analysis.

*حلل المستندات القانونية والعقود والاتفاقيات لاستخراج الشروط الرئيسية وتحديد البنود وتلخيص المحتوى والإجابة على الأسئلة. هذا يتيح مراجعة وتحليل المستندات القانونية بشكل أسرع.*

### Research Paper Summarization
Process academic papers and research documents to extract key findings, summarize methodologies, and identify important information. This enables faster literature review and research analysis.

*عالج الأوراق الأكاديمية ومستندات البحث لاستخراج النتائج الرئيسية وتلخيص المنهجيات وتحديد المعلومات المهمة. هذا يتيح مراجعة الأدبيات وتحليل البحث بشكل أسرع.*

### Form Processing
Extract data from forms, applications, and structured documents. This enables automated form processing, data entry, and document digitization workflows.

*استخرج البيانات من النماذج والتطبيقات والمستندات المنظمة. هذا يتيح معالجة النماذج الآلية وإدخال البيانات وسير عمل رقمنة المستندات.*

### Invoice and Receipt Processing
Analyze invoices and receipts to extract amounts, dates, vendors, and line items. This enables automated accounting and expense management.

*حلل الفواتير والإيصالات لاستخراج المبالغ والتواريخ والبائعين وعناصر السطر. هذا يتيح المحاسبة الآلية وإدارة النفقات.*

### Document Q&A
Answer questions about document content, enabling interactive document exploration and information retrieval. Users can ask questions and get answers based on document content.

*أجب على الأسئلة حول محتوى المستند، مما يتيح استكشاف المستندات التفاعلي واسترجاع المعلومات. يمكن للمستخدمين طرح الأسئلة والحصول على إجابات بناءً على محتوى المستند.*

## Performance Considerations

### Document Size Impact
Larger PDFs consume more tokens and processing time. Very large documents (100+ pages) can consume tens of thousands of tokens. Consider segmenting large documents or extracting relevant pages.

*ملفات PDF الأكبر تستهلك المزيد من الرموز المميزة ووقت المعالجة. المستندات الكبيرة جداً (100+ صفحة) يمكن أن تستهلك عشرات الآلاف من الرموز المميزة. فكر في تقسيم المستندات الكبيرة أو استخراج الصفحات ذات الصلة.*

### OCR Processing Time
Scanned documents require OCR processing, which takes longer than text extraction. Mistral OCR provides high-quality OCR but requires more processing time. Use appropriate engines based on document type.

*المستندات الممسوحة ضوئياً تتطلب معالجة OCR، والتي تستغرق وقتاً أطول من استخراج النص. Mistral OCR يوفر OCR عالي الجودة لكنه يتطلب وقت معالجة أكثر. استخدم المحركات المناسبة بناءً على نوع المستند.*

### Engine Selection Impact
Different engines have different performance characteristics. PDF Text is fastest for text-based PDFs. Mistral OCR is slower but handles scanned documents. Native provides provider-optimized performance.

*المحركات المختلفة لها خصائص أداء مختلفة. PDF Text أسرع لملفات PDF القائمة على النص. Mistral OCR أبطأ لكنه يتعامل مع المستندات الممسوحة ضوئياً. Native يوفر أداء محسّن من المزود.*

### Page Count Considerations
Processing time and token consumption scale with page count. Very long documents may exceed context limits. Consider processing documents in sections or extracting relevant pages only.

*وقت المعالجة واستهلاك الرموز المميزة يتناسبان مع عدد الصفحات. المستندات الطويلة جداً قد تتجاوز حدود السياق. فكر في معالجة المستندات في أقسام أو استخراج الصفحات ذات الصلة فقط.*

## Cost Implications

### Token Consumption
PDF processing consumes tokens based on document size and complexity. Text-based PDFs consume fewer tokens than scanned documents requiring OCR. Large documents can consume thousands to tens of thousands of tokens.

*معالجة PDF تستهلك الرموز المميزة بناءً على حجم وتعقيد المستند. ملفات PDF القائمة على النص تستهلك رموزاً مميزة أقل من المستندات الممسوحة ضوئياً التي تتطلب OCR. المستندات الكبيرة يمكن أن تستهلك آلاف إلى عشرات الآلاف من الرموز المميزة.*

### OCR Costs
Scanned documents requiring OCR processing cost more due to additional processing requirements. Mistral OCR provides high-quality results but increases costs compared to text extraction.

*المستندات الممسوحة ضوئياً التي تتطلب معالجة OCR تكلف أكثر بسبب متطلبات المعالجة الإضافية. Mistral OCR يوفر نتائج عالية الجودة لكنه يزيد التكاليف مقارنة باستخراج النص.*

### Engine Selection Costs
Different engines have different cost structures. PDF Text is typically most cost-effective for text-based documents. Mistral OCR costs more but is necessary for scanned documents. Choose engines based on document type to optimize costs.

*المحركات المختلفة لها هياكل تكلفة مختلفة. PDF Text عادة ما يكون الأكثر فعالية من حيث التكلفة للمستندات القائمة على النص. Mistral OCR يكلف أكثر لكنه ضروري للمستندات الممسوحة ضوئياً. اختر المحركات بناءً على نوع المستند لتحسين التكاليف.*

### Large Document Costs
Very large documents (100+ pages) can be expensive to process in full. Consider extracting relevant sections, processing in batches, or using document summarization to reduce costs while maintaining value.

*المستندات الكبيرة جداً (100+ صفحة) يمكن أن تكون مكلفة للمعالجة بالكامل. فكر في استخراج الأقسام ذات الصلة أو المعالجة في دفعات أو استخدام تلخيص المستندات لتقليل التكاليف مع الحفاظ على القيمة.*

## Best Practices

### Engine Selection
Choose the appropriate engine for your document type: Mistral OCR for scanned documents and images with text, PDF Text for text-based PDFs, Native for provider-optimized processing. Using the wrong engine reduces quality and wastes tokens.

*اختر المحرك المناسب لنوع المستند: Mistral OCR للمستندات الممسوحة ضوئياً والصور مع النص، PDF Text لملفات PDF القائمة على النص، Native للمعالجة المحسّنة من المزود. استخدام المحرك الخاطئ يقلل الجودة ويهدر الرموز المميزة.*

### Document Preprocessing
Before processing, ensure documents are clear and readable. For scanned documents, ensure good scan quality. Remove unnecessary pages or sections to reduce processing costs.

*قبل المعالجة، تأكد من أن المستندات واضحة وقابلة للقراءة. للمستندات الممسوحة ضوئياً، تأكد من جودة المسح الجيدة. أزل الصفحات أو الأقسام غير الضرورية لتقليل تكاليف المعالجة.*

### Page Selection
For large documents, extract and process only relevant pages or sections. This reduces costs and processing time while maintaining analysis quality. Don't process entire documents when only specific sections are needed.

*للمستندات الكبيرة، استخرج وعالج الصفحات أو الأقسام ذات الصلة فقط. هذا يقلل التكاليف ووقت المعالجة مع الحفاظ على جودة التحليل. لا تعالج المستندات الكاملة عندما تكون الأقسام المحددة فقط مطلوبة.*

### Combine with Structured Outputs
Use structured outputs with PDF processing to extract specific information in a structured format. This enables automated data extraction and form processing workflows.

*استخدم المخرجات المنظمة مع معالجة PDF لاستخراج معلومات محددة بتنسيق منظم. هذا يتيح استخراج البيانات الآلي وسير عمل معالجة النماذج.*

### Quality vs Cost Balance
Balance processing quality with costs. Use Mistral OCR when OCR quality is critical, but prefer PDF Text for text-based documents to reduce costs. Test different engines to find the best balance for your use case.

*وازن جودة المعالجة مع التكاليف. استخدم Mistral OCR عندما تكون جودة OCR حرجة، لكن افضل PDF Text للمستندات القائمة على النص لتقليل التكاليف. اختبر محركات مختلفة للعثور على أفضل توازن لحالة الاستخدام.*

## When NOT to Use

### Don't Process Entire Large Documents
Avoid processing entire very large documents (100+ pages) when only specific sections are needed. Extract relevant pages or sections to reduce costs and processing time.

*تجنب معالجة المستندات الكبيرة جداً بالكامل (100+ صفحة) عندما تكون الأقسام المحددة فقط مطلوبة. استخرج الصفحات أو الأقسام ذات الصلة لتقليل التكاليف ووقت المعالجة.*

### Don't Use Wrong Engine
Avoid using Mistral OCR for text-based PDFs—it's slower and more expensive than PDF Text. Similarly, don't use PDF Text for scanned documents—it won't extract text from images.

*تجنب استخدام Mistral OCR لملفات PDF القائمة على النص—إنه أبطأ وأغلى من PDF Text. وبالمثل، لا تستخدم PDF Text للمستندات الممسوحة ضوئياً—لن يستخرج النص من الصور.*

### Don't Process Low-Quality Scans
Avoid processing low-quality scanned documents. Poor scan quality reduces OCR accuracy and wastes tokens. Ensure good scan quality before processing, or preprocess images to improve quality.

*تجنب معالجة المستندات الممسوحة ضوئياً ذات الجودة المنخفضة. جودة المسح الضعيفة تقلل دقة OCR وتهدر الرموز المميزة. تأكد من جودة المسح الجيدة قبل المعالجة، أو قم بمعالجة مسبقة للصور لتحسين الجودة.*

### Don't Process Without Clear Goals
Avoid processing documents without specific analysis goals. Without clear instructions, the model may analyze irrelevant aspects, wasting tokens and money. Always provide specific analysis requirements.

*تجنب معالجة المستندات دون أهداف تحليل محددة. بدون تعليمات واضحة، قد يحلل النموذج الجوانب غير ذات الصلة، مما يهدر الرموز المميزة والمال. وفر دائماً متطلبات تحليل محددة.*

## Troubleshooting

### Text Not Extracted
If text isn't being extracted, verify you're using the correct engine. Use Mistral OCR for scanned documents, PDF Text for text-based PDFs. Check document quality—poor scans reduce extraction accuracy.

*إذا لم يتم استخراج النص، تحقق من أنك تستخدم المحرك الصحيح. استخدم Mistral OCR للمستندات الممسوحة ضوئياً، PDF Text لملفات PDF القائمة على النص. تحقق من جودة المستند—المسح الضعيف يقلل دقة الاستخراج.*

### High Processing Costs
If processing costs are high, review document size and engine selection. Use PDF Text for text-based documents instead of Mistral OCR. Extract only relevant pages or sections. Consider document summarization instead of full processing.

*إذا كانت تكاليف المعالجة عالية، راجع حجم المستند واختيار المحرك. استخدم PDF Text للمستندات القائمة على النص بدلاً من Mistral OCR. استخرج الصفحات أو الأقسام ذات الصلة فقط. فكر في تلخيص المستندات بدلاً من المعالجة الكاملة.*

### Poor OCR Accuracy
If OCR accuracy is poor, check scan quality—ensure high-resolution, clear scans. Preprocess images to improve quality if needed. Consider using Mistral OCR if you're using a different engine. Ensure proper document orientation.

*إذا كانت دقة OCR ضعيفة، تحقق من جودة المسح—تأكد من المسح عالي الدقة والوضوح. قم بمعالجة مسبقة للصور لتحسين الجودة إذا لزم الأمر. فكر في استخدام Mistral OCR إذا كنت تستخدم محركاً مختلفاً. تأكد من اتجاه المستند الصحيح.*

### Processing Timeouts
If processing times out, the document may be too large. Segment large documents into smaller sections. Extract only relevant pages. Consider processing documents in batches for very large files.

*إذا انتهت مهلة المعالجة، قد يكون المستند كبيراً جداً. قسّم المستندات الكبيرة إلى أقسام أصغر. استخرج الصفحات ذات الصلة فقط. فكر في معالجة المستندات في دفعات للملفات الكبيرة جداً.*

## Basic Usage

### PDF Processing

*معالجة PDF*

```python
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole, PDFEngine

file_content = ContentBuilder.from_url("https://example.com/doc.pdf", "file")
request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_pdf_processing(PDFEngine.MISTRAL_OCR)
    .with_message(MessageRole.USER, [file_content])
    .with_text("Summarize this document")
    .build())
```

### PDF Engines

*محركات PDF*

### Mistral OCR
Best for scanned documents and images.

*الأفضل للمستندات الممسوحة ضوئياً والصور.*

```python
request = builder.with_pdf_processing(PDFEngine.MISTRAL_OCR).build()
```

### PDF Text
Fast extraction for text-based PDFs.

*استخراج سريع لملفات PDF القائمة على النص.*

```python
request = builder.with_pdf_processing(PDFEngine.PDF_TEXT).build()
```

### Native
Provider's native PDF processing.

*معالجة PDF الأصلية من المزود.*

```python
request = builder.with_pdf_processing(PDFEngine.NATIVE).build()
```

### From Upload File

*من ملف مرفوع*

```python
from fastapi import UploadFile

async def process_pdf(upload_file: UploadFile):
    file_content = await ContentBuilder.from_upload_file(upload_file, "file")
    request = (ChatRequestBuilder()
        .with_model("anthropic/claude-sonnet-4")
        .with_pdf_processing(PDFEngine.MISTRAL_OCR)
        .with_message(MessageRole.USER, [file_content])
        .build())
```

### Document Analysis

*تحليل المستندات*

```python
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

## Advanced Examples

### Information Extraction from Forms

*استخراج المعلومات من النماذج*

```python
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole, PDFEngine

file_content = ContentBuilder.from_url("https://example.com/form.pdf", "file")

request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_pdf_processing(PDFEngine.MISTRAL_OCR)
    .with_message(MessageRole.USER, [file_content])
    .with_text("Extract all form fields and their values from this document")
    .with_structured_output(
        schema={
            "type": "object",
            "properties": {
                "fields": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "field_name": {"type": "string"},
                            "value": {"type": "string"},
                            "type": {"type": "string"}
                        }
                    }
                }
            }
        },
        name="FormData"
    )
    .build())
```

### Research Paper Analysis

*تحليل أوراق البحث*

```python
file_content = ContentBuilder.from_url("https://example.com/paper.pdf", "file")

request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_pdf_processing(PDFEngine.PDF_TEXT)  # Text-based PDF
    .with_message(MessageRole.USER, [file_content])
    .with_text("Analyze this research paper. Extract: title, authors, abstract, methodology, key findings, and conclusions.")
    .with_structured_output(
        schema={
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "authors": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "abstract": {"type": "string"},
                "methodology": {"type": "string"},
                "key_findings": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "conclusions": {"type": "string"}
            }
        },
        name="ResearchPaper"
    )
    .build())
```

### Document Q&A

*أسئلة وأجوبة المستندات*

```python
file_content = ContentBuilder.from_url("https://example.com/manual.pdf", "file")

request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_pdf_processing(PDFEngine.PDF_TEXT)
    .with_message(MessageRole.USER, [file_content])
    .with_text("Based on this document, answer: What are the main features described? How do I configure the system? What are the troubleshooting steps?")
    .build())
```
