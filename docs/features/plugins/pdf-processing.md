# PDF Processing Plugin

## Feature Overview

The PDF processing plugin enables AI models to read and analyze PDF documents with support for multiple processing engines optimized for different document types. This feature allows you to extract text, analyze content, and understand PDF documents—from text-based PDFs to scanned documents requiring OCR (Optical Character Recognition).

*إضافة معالجة PDF تمكن نماذج الذكاء الاصطناعي من قراءة وتحليل مستندات PDF مع دعم محركات معالجة متعددة محسّنة لأنواع المستندات المختلفة. تتيح لك هذه الميزة استخراج النص وتحليل المحتوى وفهم مستندات PDF—من ملفات PDF القائمة على النص إلى المستندات الممسوحة ضوئياً التي تتطلب OCR (التعرف الضوئي على الأحرف).*

## Feature Importance

PDF processing is essential for applications that need to work with documents—legal documents, research papers, forms, invoices, and reports. Without PDF processing, AI models cannot access information locked in PDF format. This plugin bridges that gap, enabling AI to read, analyze, and extract information from PDF documents, making document-heavy workflows automatable.

*معالجة PDF ضرورية للتطبيقات التي تحتاج إلى العمل مع المستندات—المستندات القانونية وأوراق البحث والنماذج والفواتير والتقارير. بدون معالجة PDF، نماذج الذكاء الاصطناعي لا يمكنها الوصول إلى المعلومات المحبوسة في تنسيق PDF. هذه الإضافة تربط هذه الفجوة، مما يتيح للذكاء الاصطناعي قراءة وتحليل واستخراج المعلومات من مستندات PDF، مما يجعل سير العمل الثقيل بالمستندات قابل للأتمتة.*

## Available Engines

### Mistral OCR
Best for scanned documents and images with text.

```python
from app.builders import ChatRequestBuilder
from app.enums import PDFEngine

request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_pdf_processing(PDFEngine.MISTRAL_OCR)
    .build())
```

### PDF Text
Fast extraction for text-based PDFs.

```python
request = builder.with_pdf_processing(PDFEngine.PDF_TEXT).build()
```

### Native
Provider's native PDF processing.

```python
request = builder.with_pdf_processing(PDFEngine.NATIVE).build()
```

## Basic Usage

```python
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole, PDFEngine

# Add PDF file
file_content = ContentBuilder.from_url("https://example.com/document.pdf", "file")

request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_pdf_processing(PDFEngine.MISTRAL_OCR)
    .with_message(MessageRole.USER, [file_content])
    .with_text("Summarize this document")
    .build())
```

## Use Cases

### Document Summarization
```python
request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_pdf_processing(PDFEngine.MISTRAL_OCR)
    .with_message(MessageRole.USER, [file_content])
    .with_text("Create a summary with key points")
    .build())
```

### Information Extraction
```python
request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_pdf_processing(PDFEngine.PDF_TEXT)
    .with_message(MessageRole.USER, [file_content])
    .with_text("Extract all dates and names")
    .with_structured_output(
        schema={
            "type": "object",
            "properties": {
                "dates": {"type": "array", "items": {"type": "string"}},
                "names": {"type": "array", "items": {"type": "string"}}
            }
        },
        name="ExtractedData"
    )
    .build())
```

### Question Answering
```python
request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_pdf_processing(PDFEngine.MISTRAL_OCR)
    .with_message(MessageRole.USER, [file_content])
    .with_text("What is the main topic of this document?")
    .build())
```

## Engine Selection Guide

### Use Mistral OCR when:
- Document contains scanned images
- Text is embedded in images
- OCR accuracy is important
- Document quality is low

### Use PDF Text when:
- Document is text-based
- Fast processing is needed
- Document quality is high
- No images with text

### Use Native when:
- Provider has optimized processing
- You want provider-specific features
- Default behavior is acceptable

## Key Benefits

### Multiple Processing Engines
Different engines optimized for different document types ensure optimal results. Mistral OCR excels at scanned documents, PDF Text is fast for text-based PDFs, and Native provides provider-optimized processing.

*محركات معالجة مختلفة محسّنة لأنواع المستندات المختلفة تضمن نتائج مثلى. Mistral OCR يتفوق في المستندات الممسوحة ضوئياً، PDF Text سريع لملفات PDF القائمة على النص، وNative يوفر معالجة محسّنة من المزود.*

### OCR Capabilities
Mistral OCR enables processing of scanned documents and images with text, making previously inaccessible content analyzable. This opens up vast archives of scanned documents for AI analysis.

*Mistral OCR يتيح معالجة المستندات الممسوحة ضوئياً والصور مع النص، مما يجعل المحتوى الذي كان غير قابل للوصول سابقاً قابلاً للتحليل. هذا يفتح أرشيفات ضخمة من المستندات الممسوحة ضوئياً لتحليل الذكاء الاصطناعي.*

### Flexible Document Handling
Support for various PDF types—text-based, scanned, forms, tables—enables comprehensive document processing. Choose the right engine for each document type to optimize results.

*دعم أنواع PDF المختلفة—القائمة على النص، الممسوحة ضوئياً، النماذج، الجداول—يتيح معالجة مستندات شاملة. اختر المحرك المناسب لكل نوع مستند لتحسين النتائج.*

## Performance Considerations

### Processing Time
PDF processing time depends on document size, complexity, and engine selection. OCR processing takes longer than text extraction. Large documents may take significant time to process.

*وقت معالجة PDF يعتمد على حجم المستند والتعقيد واختيار المحرك. معالجة OCR تستغرق وقتاً أطول من استخراج النص. المستندات الكبيرة قد تستغرق وقتاً كبيراً للمعالجة.*

### Engine Performance
Different engines have different performance characteristics. PDF Text is fastest for text-based PDFs. Mistral OCR is slower but necessary for scanned documents. Choose engines based on document type and performance requirements.

*المحركات المختلفة لها خصائص أداء مختلفة. PDF Text أسرع لملفات PDF القائمة على النص. Mistral OCR أبطأ لكنه ضروري للمستندات الممسوحة ضوئياً. اختر المحركات بناءً على نوع المستند ومتطلبات الأداء.*

## Cost Implications

### Additional Processing Costs
PDF processing adds costs beyond standard API calls. OCR processing typically costs more than text extraction. Large documents consume more tokens and increase costs.

*معالجة PDF تضيف تكاليف تتجاوز استدعاءات API القياسية. معالجة OCR عادة ما تكلف أكثر من استخراج النص. المستندات الكبيرة تستهلك المزيد من الرموز المميزة وتزيد التكاليف.*

### Engine Cost Differences
Different engines have different cost structures. Mistral OCR may cost more than PDF Text due to OCR processing requirements. Choose engines based on document needs and cost constraints.

*المحركات المختلفة لها هياكل تكلفة مختلفة. Mistral OCR قد يكلف أكثر من PDF Text بسبب متطلبات معالجة OCR. اختر المحركات بناءً على احتياجات المستند وقيود التكلفة.*

## Best Practices

### Engine Selection
Use Mistral OCR for scanned documents and images with text. Use PDF Text for text-based PDFs. Use Native when provider optimization is preferred. Matching engines to document types ensures optimal results.

*استخدم Mistral OCR للمستندات الممسوحة ضوئياً والصور مع النص. استخدم PDF Text لملفات PDF القائمة على النص. استخدم Native عندما يكون التحسين من المزود مفضلاً. مطابقة المحركات لأنواع المستندات تضمن نتائج مثلى.*

### Document Preprocessing
Ensure documents are clear and readable before processing. For scanned documents, ensure good scan quality. Remove unnecessary pages to reduce processing costs.

*تأكد من أن المستندات واضحة وقابلة للقراءة قبل المعالجة. للمستندات الممسوحة ضوئياً، تأكد من جودة المسح الجيدة. أزل الصفحات غير الضرورية لتقليل تكاليف المعالجة.*

### Combine with Structured Outputs
Use structured outputs with PDF processing to extract specific information in organized formats. This enables automated data extraction and form processing.

*استخدم المخرجات المنظمة مع معالجة PDF لاستخراج معلومات محددة بتنسيقات منظمة. هذا يتيح استخراج البيانات الآلي ومعالجة النماذج.*

### Test Different Engines
Test different engines with your document types to find optimal settings. Document quality, type, and content affect which engine works best.

*اختبر محركات مختلفة مع أنواع مستنداتك للعثور على الإعدادات المثلى. جودة المستند والنوع والمحتوى تؤثر على أي محرك يعمل بشكل أفضل.*

## When NOT to Use

### Don't Use Wrong Engine
Avoid using Mistral OCR for text-based PDFs—it's slower and more expensive than PDF Text. Similarly, don't use PDF Text for scanned documents—it won't extract text from images.

*تجنب استخدام Mistral OCR لملفات PDF القائمة على النص—إنه أبطأ وأغلى من PDF Text. وبالمثل، لا تستخدم PDF Text للمستندات الممسوحة ضوئياً—لن يستخرج النص من الصور.*

### Don't Process Low-Quality Scans
Avoid processing low-quality scanned documents. Poor scan quality reduces OCR accuracy and wastes tokens. Ensure good scan quality or preprocess images before processing.

*تجنب معالجة المستندات الممسوحة ضوئياً ذات الجودة المنخفضة. جودة المسح الضعيفة تقلل دقة OCR وتهدر الرموز المميزة. تأكد من جودة المسح الجيدة أو قم بمعالجة مسبقة للصور قبل المعالجة.*

## Troubleshooting

### Poor OCR Accuracy
If OCR accuracy is poor, check scan quality and document clarity. Preprocess images to improve quality. Ensure proper document orientation. Consider using Mistral OCR if using a different engine.

*إذا كانت دقة OCR ضعيفة، تحقق من جودة المسح ووضوح المستند. قم بمعالجة مسبقة للصور لتحسين الجودة. تأكد من اتجاه المستند الصحيح. فكر في استخدام Mistral OCR إذا كنت تستخدم محركاً مختلفاً.*

### High Processing Costs
If costs are high, review document sizes and engine selection. Use PDF Text for text-based documents instead of Mistral OCR. Extract only relevant pages or sections. Consider document summarization instead of full processing.

*إذا كانت تكاليف المعالجة عالية، راجع أحجام المستندات واختيار المحرك. استخدم PDF Text للمستندات القائمة على النص بدلاً من Mistral OCR. استخرج الصفحات أو الأقسام ذات الصلة فقط. فكر في تلخيص المستندات بدلاً من المعالجة الكاملة.*

## Important Notes

- PDF processing adds additional cost
  *معالجة PDF تضيف تكلفة إضافية*
- Processing time depends on document size
  *وقت المعالجة يعتمد على حجم المستند*
- OCR accuracy varies by document quality
  *دقة OCR تختلف حسب جودة المستند*
- Large PDFs may take longer to process
  *ملفات PDF الكبيرة قد تستغرق وقتاً أطول للمعالجة*

