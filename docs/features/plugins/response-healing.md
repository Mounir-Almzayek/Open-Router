# Response Healing Plugin

## Feature Overview

The response healing plugin automatically repairs malformed JSON responses, ensuring valid output even when the model produces invalid JSON. This plugin detects common JSON errors like missing quotes, trailing commas, unclosed brackets, and type mismatches, then automatically fixes them to produce valid JSON. This feature is essential for reliable structured output generation.

*إضافة استشفاء الاستجابة تصلح تلقائياً استجابات JSON المشوهة، مما يضمن إخراجاً صالحاً حتى عندما ينتج النموذج JSON غير صالح. هذه الإضافة تكتشف أخطاء JSON الشائعة مثل علامات الاقتباس المفقودة والفاصلات الزائدة والأقواس غير المغلقة وعدم تطابق الأنواع، ثم تصلحها تلقائياً لإنتاج JSON صالح. هذه الميزة ضرورية لتوليد المخرجات المنظمة الموثوقة.*

## Feature Importance

Response healing is crucial for production applications that rely on structured outputs. Without healing, malformed JSON responses cause parsing errors, application failures, and poor user experience. Response healing ensures reliability by automatically fixing common JSON issues, reducing retries, and improving success rates for structured output generation.

*استشفاء الاستجابة ضروري لتطبيقات الإنتاج التي تعتمد على المخرجات المنظمة. بدون الاستشفاء، استجابات JSON المشوهة تسبب أخطاء تحليل وفشل التطبيقات وتجربة مستخدم ضعيفة. استشفاء الاستجابة يضمن الموثوقية عن طريق إصلاح مشاكل JSON الشائعة تلقائياً، مما يقلل إعادة المحاولة ويحسن معدلات النجاح لتوليد المخرجات المنظمة.*

## Enable Response Healing

```python
from app.builders import ChatRequestBuilder

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Return JSON with user data")
    .with_response_healing()
    .build())
```

## Use Cases

### JSON Object Output
When requesting JSON output, response healing ensures valid JSON:

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("List 3 programming languages as JSON")
    .with_json_object_output()
    .with_response_healing()
    .build())
```

### Structured Output with Schema
Response healing works with JSON Schema:

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
    }
}

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("List programming languages")
    .with_structured_output(schema, name="Languages")
    .with_response_healing()
    .build())
```

## How It Works

1. Model generates response (may be malformed JSON)
2. Response healing plugin detects issues
3. Automatically repairs JSON structure
4. Returns valid JSON response

## Common Repairs

- **Missing quotes**: Adds quotes to unquoted keys
- **Trailing commas**: Removes invalid trailing commas
- **Unclosed brackets**: Closes brackets and braces
- **Invalid escape sequences**: Fixes escape characters
- **Type mismatches**: Converts types to match schema

## Key Benefits

### Reliability
Ensures valid JSON output even when models produce malformed JSON. This prevents parsing errors and application failures, ensuring consistent, reliable structured outputs.

*يضمن إخراج JSON صالح حتى عندما تنتج النماذج JSON مشوهاً. هذا يمنع أخطاء التحليل وفشل التطبيقات، مما يضمن مخرجات منظمة متسقة وموثوقة.*

### Reduced Retries
Fewer failed requests due to JSON errors means less retry overhead and lower costs. Response healing fixes common issues automatically, reducing the need for retries.

*طلبات فاشلة أقل بسبب أخطاء JSON يعني حمل إعادة محاولة أقل وتكاليف أقل. استشفاء الاستجابة يصلح المشاكل الشائعة تلقائياً، مما يقلل الحاجة لإعادة المحاولة.*

### Better User Experience
Consistent response format ensures applications work reliably. Users don't experience errors from malformed JSON, improving overall application quality.

*تنسيق الاستجابة المتسق يضمن عمل التطبيقات بشكل موثوق. المستخدمون لا يواجهون أخطاء من JSON مشوه، مما يحسن جودة التطبيق الإجمالية.*

### Error Prevention
Catches and fixes common JSON errors before they cause problems. This proactive error handling prevents downstream issues and improves system reliability.

*يكتشف ويصلح أخطاء JSON الشائعة قبل أن تسبب مشاكل. هذه المعالجة الاستباقية للأخطاء تمنع مشاكل المصب وتحسن موثوقية النظام.*

## Performance Considerations

### Minimal Overhead
Response healing adds minimal processing overhead. The healing process is fast and efficient, adding negligible latency to responses.

*استشفاء الاستجابة يضيف حمل معالجة ضئيل. عملية الاستشفاء سريعة وفعالة، مما يضيف زمن انتظار ضئيل للاستجابات.*

### Works Best with Structured Outputs
Response healing is most effective when combined with structured outputs. The combination ensures both schema compliance and valid JSON formatting.

*استشفاء الاستجابة أكثر فعالية عند دمجه مع المخرجات المنظمة. المزيج يضمن كل من الامتثال للمخطط وتنسيق JSON صالح.*

## Cost Implications

### Reduced Retry Costs
By fixing JSON errors automatically, response healing reduces the need for retries, saving costs associated with failed requests and retry attempts.

*عن طريق إصلاح أخطاء JSON تلقائياً، استشفاء الاستجابة يقلل الحاجة لإعادة المحاولة، مما يوفر التكاليف المرتبطة بالطلبات الفاشلة ومحاولات إعادة المحاولة.*

### Improved Success Rates
Higher success rates mean fewer wasted tokens on failed requests. Response healing improves overall cost efficiency by ensuring more requests succeed on the first attempt.

*معدلات النجاح الأعلى تعني رموزاً مميزة مهدرة أقل على الطلبات الفاشلة. استشفاء الاستجابة يحسن كفاءة التكلفة الإجمالية عن طريق ضمان نجاح المزيد من الطلبات في المحاولة الأولى.*

## Best Practices

### Always Enable for JSON Output
Always enable response healing when using JSON output or structured outputs. The benefits far outweigh the minimal overhead, ensuring reliable JSON generation.

*قم دائماً بتمكين استشفاء الاستجابة عند استخدام إخراج JSON أو المخرجات المنظمة. الفوائد تفوق بكثير الحمل الضئيل، مما يضمن توليد JSON موثوق.*

### Combine with Structured Outputs
Use response healing together with structured outputs for best results. Structured outputs ensure schema compliance, while healing ensures valid JSON formatting.

*استخدم استشفاء الاستجابة مع المخرجات المنظمة للحصول على أفضل النتائج. المخرجات المنظمة تضمن الامتثال للمخطط، بينما الاستشفاء يضمن تنسيق JSON صالح.*

### Monitor Response Quality
Monitor response quality to ensure healing is effective. Track healing success rates and identify patterns in JSON errors to improve prompts or configurations.

*راقب جودة الاستجابة لضمان فعالية الاستشفاء. تتبع معدلات نجاح الاستشفاء وتحديد أنماط أخطاء JSON لتحسين المطالب أو التكوينات.*

## When NOT to Use

### Don't Rely Solely on Healing
Don't rely solely on response healing to fix all JSON issues. Some complex errors may still require manual handling. Use healing as a safety net, not the primary solution.

*لا تعتمد فقط على استشفاء الاستجابة لإصلاح جميع مشاكل JSON. بعض الأخطاء المعقدة قد لا تزال تتطلب معالجة يدوية. استخدم الاستشفاء كشبكة أمان، وليس الحل الأساسي.*

### Don't Ignore Root Causes
Don't ignore why models produce malformed JSON. Investigate and fix root causes—improve prompts, adjust configurations, or use better models. Healing fixes symptoms but doesn't address underlying issues.

*لا تتجاهل سبب إنتاج النماذج لـ JSON مشوه. تحقق وأصلح الأسباب الجذرية—حسّن المطالب أو اضبط التكوينات أو استخدم نماذج أفضل. الاستشفاء يصلح الأعراض لكنه لا يعالج المشاكل الأساسية.*

## Troubleshooting

### Healing Not Working
If healing isn't fixing JSON errors, verify it's enabled correctly. Check that errors are within healing capabilities. Some complex errors may require manual handling or prompt improvements.

*إذا لم يصلح الاستشفاء أخطاء JSON، تحقق من أنه مفعّل بشكل صحيح. تحقق من أن الأخطاء ضمن قدرات الاستشفاء. بعض الأخطاء المعقدة قد تتطلب معالجة يدوية أو تحسينات المطالب.*

### Complex Errors Persist
If complex errors persist after healing, review error patterns. Improve prompts to guide models to produce better JSON. Consider using stricter structured output settings.

*إذا استمرت الأخطاء المعقدة بعد الاستشفاء، راجع أنماط الأخطاء. حسّن المطالب لتوجيه النماذج لإنتاج JSON أفضل. فكر في استخدام إعدادات مخرجات منظمة أكثر صرامة.*

## Important Notes

- Response healing adds minimal overhead
  *استشفاء الاستجابة يضيف حمل ضئيل*
- Works best with structured outputs
  *يعمل بشكل أفضل مع المخرجات المنظمة*
- May not fix all JSON errors
  *قد لا يصلح جميع أخطاء JSON*
- Some complex errors may still require manual handling
  *بعض الأخطاء المعقدة قد لا تزال تتطلب معالجة يدوية*

## Example

```python
# Without response healing - may fail
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Return JSON")
    .with_json_object_output()
    .build())

# With response healing - more reliable
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Return JSON")
    .with_json_object_output()
    .with_response_healing()
    .build())
```

