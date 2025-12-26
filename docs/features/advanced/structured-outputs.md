# Structured Outputs

## Feature Overview

Structured outputs enable AI models to return data in specific, predictable formats defined by JSON schemas. Instead of free-form text, models produce structured data that can be directly consumed by applications, integrated with databases, or processed programmatically. This feature is essential for building reliable AI-powered applications that need consistent, parseable outputs.

*المخرجات المنظمة تمكن نماذج الذكاء الاصطناعي من إرجاع البيانات بتنسيقات محددة وقابلة للتنبؤ محددة بواسطة مخططات JSON. بدلاً من النص الحر، تنتج النماذج بيانات منظمة يمكن استهلاكها مباشرة من قبل التطبيقات أو التكامل مع قواعد البيانات أو معالجتها برمجياً. هذه الميزة ضرورية لبناء تطبيقات مدعومة بالذكاء الاصطناعي موثوقة تحتاج مخرجات متسقة وقابلة للتحليل.*

## Feature Importance

Structured outputs bridge the gap between AI text generation and application integration. Without structured outputs, applications must parse free-form text, which is error-prone and unreliable. Structured outputs enable reliable, production-ready AI applications that integrate seamlessly with existing systems.

*المخرجات المنظمة تربط الفجوة بين توليد النص بالذكاء الاصطناعي وتكامل التطبيقات. بدون المخرجات المنظمة، يجب على التطبيقات تحليل النص الحر، وهو عرضة للأخطاء وغير موثوق. المخرجات المنظمة تمكن تطبيقات الذكاء الاصطناعي الموثوقة الجاهزة للإنتاج التي تتكامل بسلاسة مع الأنظمة الموجودة.*

## Key Benefits

### Reliable Data Extraction
Structured outputs ensure consistent data formats, making it safe to parse and process AI responses programmatically. This eliminates parsing errors and enables reliable data extraction from AI-generated content.

*المخرجات المنظمة تضمن تنسيقات بيانات متسقة، مما يجعل من الآمن تحليل ومعالجة استجابات الذكاء الاصطناعي برمجياً. هذا يلغي أخطاء التحليل ويمكن استخراج البيانات الموثوق من المحتوى المولد من الذكاء الاصطناعي.*

### Direct Integration
Structured outputs can be directly integrated with databases, APIs, and applications without parsing or transformation. This enables seamless AI integration into existing workflows and systems.

*المخرجات المنظمة يمكن دمجها مباشرة مع قواعد البيانات وAPIs والتطبيقات دون تحليل أو تحويل. هذا يتيح تكامل الذكاء الاصطناعي السلس في سير العمل والأنظمة الموجودة.*

### Type Safety
JSON schemas provide type safety, ensuring outputs match expected data types. This prevents type errors and enables reliable data processing in strongly-typed systems.

*مخططات JSON توفر أمان النوع، مما يضمن تطابق المخرجات مع أنواع البيانات المتوقعة. هذا يمنع أخطاء النوع ويمكن معالجة البيانات الموثوقة في الأنظمة ذات الأنواع القوية.*

### Validation and Constraints
JSON schemas allow validation rules and constraints, ensuring outputs meet specific requirements. This enables reliable data quality and prevents invalid outputs.

*مخططات JSON تسمح بقواعد التحقق والقيود، مما يضمن استيفاء المخرجات لمتطلبات محددة. هذا يتيح جودة بيانات موثوقة ويمنع المخرجات غير الصالحة.*

### Reduced Parsing Complexity
Structured outputs eliminate the need for complex text parsing, regex patterns, and error-prone extraction logic. Applications can directly consume structured data, reducing code complexity and bugs.

*المخرجات المنظمة تلغي الحاجة لتحليل النص المعقد وأنماط regex ومنطق الاستخراج المعرض للأخطاء. التطبيقات يمكنها استهلاك البيانات المنظمة مباشرة، مما يقلل تعقيد الكود والأخطاء.*

## Use Cases

### Data Extraction
Extract structured data from unstructured text, documents, or conversations. Define schemas for entities, relationships, and attributes to reliably extract information for databases or applications.

*استخرج البيانات المنظمة من النص غير المنظم أو المستندات أو المحادثات. حدد مخططات للكيانات والعلاقات والسمات لاستخراج المعلومات بشكل موثوق لقواعد البيانات أو التطبيقات.*

### Form Processing
Process forms, applications, and structured documents to extract data in consistent formats. This enables automated form processing and data entry workflows.

*عالج النماذج والتطبيقات والمستندات المنظمة لاستخراج البيانات بتنسيقات متسقة. هذا يتيح معالجة النماذج الآلية وسير عمل إدخال البيانات.*

### API Response Generation
Generate API responses in structured formats for integration with other systems. AI can produce JSON responses that match API specifications, enabling AI-powered API endpoints.

*أنشئ استجابات API بتنسيقات منظمة للتكامل مع أنظمة أخرى. يمكن للذكاء الاصطناعي إنتاج استجابات JSON تطابق مواصفات API، مما يتيح نقاط نهاية API مدعومة بالذكاء الاصطناعي.*

### Database Integration
Generate structured data for database insertion. AI can extract and format data from various sources into database-ready formats, enabling automated data pipelines.

*أنشئ بيانات منظمة لإدراج قاعدة البيانات. يمكن للذكاء الاصطناعي استخراج وتنسيق البيانات من مصادر مختلفة إلى تنسيقات جاهزة لقاعدة البيانات، مما يتيح خطوط بيانات آلية.*

### Content Analysis
Analyze content and return structured insights, summaries, or metadata. This enables automated content processing, tagging, and organization systems.

*حلل المحتوى وأعد رؤى منظمة أو ملخصات أو بيانات وصفية. هذا يتيح أنظمة معالجة المحتوى الآلية والوسم والتنظيم.*

## Performance Considerations

### Schema Complexity
More complex schemas with nested objects, arrays, and constraints may take longer to generate. Keep schemas as simple as possible while meeting requirements to optimize performance.

*المخططات الأكثر تعقيداً مع الكائنات المتداخلة والمصفوفات والقيود قد تستغرق وقتاً أطول للتوليد. حافظ على المخططات بسيطة قدر الإمكان مع استيفاء المتطلبات لتحسين الأداء.*

### Strict Mode Impact
Strict mode enforces exact schema compliance, which may require more processing time and retries. Non-strict mode is faster but allows flexibility. Choose based on your requirements.

*الوضع الصارم يفرض الامتثال الدقيق للمخطط، مما قد يتطلب وقت معالجة وإعادة محاولة أكثر. الوضع غير الصارم أسرع لكنه يسمح بالمرونة. اختر بناءً على متطلباتك.*

### Response Length
Structured outputs may be longer than free-form text due to JSON formatting and required fields. However, structured data is more efficient to process programmatically.

*المخرجات المنظمة قد تكون أطول من النص الحر بسبب تنسيق JSON والحقول المطلوبة. ومع ذلك، البيانات المنظمة أكثر كفاءة للمعالجة برمجياً.*

### Validation Overhead
Schema validation adds minimal overhead but ensures output quality. The benefits of validation usually outweigh the small performance cost.

*التحقق من المخطط يضيف حمل ضئيل لكنه يضمن جودة الإخراج. فوائد التحقق عادة ما تفوق تكلفة الأداء الصغيرة.*

## Cost Implications

### Token Consumption
Structured outputs consume tokens similar to text outputs. However, JSON formatting may slightly increase token usage compared to free-form text. The benefits of structured data usually justify the small cost increase.

*المخرجات المنظمة تستهلك رموزاً مميزة مشابهة لمخرجات النص. ومع ذلك، تنسيق JSON قد يزيد استخدام الرموز المميزة قليلاً مقارنة بالنص الحر. فوائد البيانات المنظمة عادة ما تبرر الزيادة الصغيرة في التكلفة.*

### Retry Costs
In strict mode, invalid outputs may require retries, increasing costs. However, strict mode ensures quality, reducing downstream processing errors and costs. Balance strictness with cost considerations.

*في الوضع الصارم، المخرجات غير الصالحة قد تتطلب إعادة محاولة، مما يزيد التكاليف. ومع ذلك، الوضع الصارم يضمن الجودة، مما يقلل أخطاء معالجة المصب والتكاليف. وازن الصرامة مع اعتبارات التكلفة.*

### Schema Size
Larger schemas consume more tokens in the request. Keep schemas concise while maintaining necessary structure. Avoid unnecessary nesting or verbose field descriptions.

*المخططات الأكبر تستهلك المزيد من الرموز المميزة في الطلب. حافظ على المخططات موجزة مع الحفاظ على الهيكل الضروري. تجنب التداخل غير الضروري أو أوصاف الحقول المطولة.*

## Best Practices

### Schema Design
Design clear, well-structured schemas that match your data needs. Use appropriate data types, define required fields, and include validation constraints. Keep schemas as simple as possible while meeting requirements.

*صمم مخططات واضحة ومنظمة جيداً تطابق احتياجات بياناتك. استخدم أنواع البيانات المناسبة وحدد الحقول المطلوبة واشمل قيود التحقق. حافظ على المخططات بسيطة قدر الإمكان مع استيفاء المتطلبات.*

### Strict Mode Usage
Use strict mode when output format is critical and must match schemas exactly. Use non-strict mode when some flexibility is acceptable. Strict mode ensures reliability but may require retries.

*استخدم الوضع الصارم عندما يكون تنسيق الإخراج حرجاً ويجب أن يطابق المخططات بدقة. استخدم الوضع غير الصارم عندما تكون بعض المرونة مقبولة. الوضع الصارم يضمن الموثوقية لكنه قد يتطلب إعادة محاولة.*

### Schema Validation
Validate schemas before use to ensure they're correct and complete. Test schemas with sample data to verify they work as expected. Use schema validation tools when available.

*تحقق من المخططات قبل الاستخدام لضمان صحتها واكتمالها. اختبر المخططات مع بيانات عينة للتحقق من أنها تعمل كما هو متوقع. استخدم أدوات التحقق من المخططات عند التوفر.*

### Error Handling
Implement error handling for cases where structured outputs don't match schemas. Provide fallback logic, retry mechanisms, and user feedback for validation failures.

*نفذ معالجة أخطاء للحالات حيث لا تطابق المخرجات المنظمة المخططات. وفر منطق احتياطي وآليات إعادة محاولة وردود فعل المستخدم لفشل التحقق.*

### Combine with Other Features
Combine structured outputs with other features like reasoning tokens for complex analysis, or tool calling for data retrieval. This enables powerful AI applications with reliable outputs.

*اجمع المخرجات المنظمة مع ميزات أخرى مثل رموز التفكير للتحليل المعقد، أو استدعاء الأدوات لاسترجاع البيانات. هذا يتيح تطبيقات ذكاء اصطناعي قوية مع مخرجات موثوقة.*

## When NOT to Use

### Don't Use for Free-Form Content
Avoid structured outputs for content that needs to be free-form, creative, or conversational. Structured outputs constrain creativity and are best for data extraction and structured information.

*تجنب المخرجات المنظمة للمحتوى الذي يحتاج إلى أن يكون حراً أو إبداعياً أو محادثة. المخرجات المنظمة تقيد الإبداع وهي الأفضل لاستخراج البيانات والمعلومات المنظمة.*

### Don't Over-Complicate Schemas
Avoid overly complex schemas with excessive nesting or unnecessary fields. Complex schemas are harder to generate correctly and increase processing time and costs.

*تجنب المخططات المعقدة للغاية مع التداخل المفرط أو الحقول غير الضرورية. المخططات المعقدة أصعب للتوليد بشكل صحيح وتزيد وقت المعالجة والتكاليف.*

### Don't Use Strict Mode Unnecessarily
Avoid strict mode when some flexibility is acceptable. Strict mode increases retry costs and may be unnecessary for use cases that can tolerate minor variations.

*تجنب الوضع الصارم عندما تكون بعض المرونة مقبولة. الوضع الصارم يزيد تكاليف إعادة المحاولة وقد يكون غير ضروري لحالات الاستخدام التي يمكنها تحمل الاختلافات الطفيفة.*

### Don't Ignore Validation Errors
Don't ignore schema validation errors. Implement proper error handling and retry logic. Validation errors indicate issues that need to be addressed.

*لا تتجاهل أخطاء التحقق من المخطط. نفذ معالجة أخطاء مناسبة ومنطق إعادة المحاولة. أخطاء التحقق تشير إلى مشاكل تحتاج إلى معالجة.*

## Troubleshooting

### Schema Validation Failures
If schemas fail validation, review schema definitions for errors. Check data types, required fields, and constraints. Test schemas with sample data to identify issues.

*إذا فشل التحقق من المخططات، راجع تعريفات المخطط للأخطاء. تحقق من أنواع البيانات والحقول المطلوبة والقيود. اختبر المخططات مع بيانات عينة لتحديد المشاكل.*

### Output Not Matching Schema
If outputs don't match schemas, check schema definitions are correct and complete. Consider using strict mode to enforce compliance. Review prompts to ensure they guide the model correctly.

*إذا لم تطابق المخرجات المخططات، تحقق من أن تعريفات المخطط صحيحة وكاملة. فكر في استخدام الوضع الصارم لفرض الامتثال. راجع المطالب للتأكد من أنها توجه النموذج بشكل صحيح.*

### High Retry Rates
If retry rates are high, review schema complexity and strictness. Consider simplifying schemas or using non-strict mode. Ensure prompts clearly guide the model to produce correct outputs.

*إذا كانت معدلات إعادة المحاولة عالية، راجع تعقيد المخطط والصرامة. فكر في تبسيط المخططات أو استخدام الوضع غير الصارم. تأكد من أن المطالب توجه النموذج بوضوح لإنتاج مخرجات صحيحة.*

### Parsing Errors
If parsing errors occur, verify JSON output is valid. Check for malformed JSON, missing fields, or type mismatches. Use response healing plugin to automatically fix common JSON issues.

*إذا حدثت أخطاء تحليل، تحقق من أن إخراج JSON صالح. تحقق من JSON مشوه أو حقول مفقودة أو عدم تطابق الأنواع. استخدم إضافة استشفاء الاستجابة لإصلاح مشاكل JSON الشائعة تلقائياً.*

## Basic Usage

### JSON Object Output

*إخراج كائن JSON*

```python
from app.builders import ChatRequestBuilder

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("List 3 programming languages")
    .with_json_object_output()
    .build())
```

### JSON Schema Output

*إخراج مخطط JSON*

```python
schema = {
    "type": "object",
    "properties": {
        "languages": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "year": {"type": "integer"}
                }
            }
        }
    },
    "required": ["languages"]
}

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("List 3 programming languages")
    .with_structured_output(schema, name="Languages", strict=True)
    .build())
```

### Strict Mode

*الوضع الصارم*

When `strict=True`, the model must follow the schema exactly. When `strict=False`, the model can be more flexible.

*عند `strict=True`، يجب على النموذج اتباع المخطط بدقة. عند `strict=False`، يمكن للنموذج أن يكون أكثر مرونة.*

## Advanced Examples

### Complex Nested Schema

*مخطط متداخل معقد*

```python
schema = {
    "type": "object",
    "properties": {
        "user": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "email": {"type": "string"},
                "address": {
                    "type": "object",
                    "properties": {
                        "street": {"type": "string"},
                        "city": {"type": "string"},
                        "zip": {"type": "string"}
                    },
                    "required": ["street", "city", "zip"]
                }
            },
            "required": ["name", "email"]
        },
        "orders": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "total": {"type": "number"},
                    "items": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": ["id", "total"]
            }
        }
    },
    "required": ["user", "orders"]
}

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Extract user and order information from: [data]")
    .with_structured_output(schema, name="UserData", strict=True)
    .build())
```

### Data Extraction with Validation

*استخراج البيانات مع التحقق*

```python
schema = {
    "type": "object",
    "properties": {
        "products": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "price": {
                        "type": "number",
                        "minimum": 0
                    },
                    "category": {
                        "type": "string",
                        "enum": ["electronics", "clothing", "food"]
                    },
                    "in_stock": {"type": "boolean"}
                },
                "required": ["name", "price", "category"]
            },
            "minItems": 1
        }
    },
    "required": ["products"]
}

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Extract product information from: [text]")
    .with_structured_output(schema, name="Products", strict=True)
    .build())
```

### Flexible Mode

*الوضع المرن*

```python
# Non-strict mode allows flexibility
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Describe a person")
    .with_structured_output(
        schema={
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
                "description": {"type": "string"}
            }
        },
        name="Person",
        strict=False  # Allows some flexibility
    )
    .build())
```
