# Fallbacks

## Feature Overview

Fallbacks enable automatic failover to backup models or providers when primary options fail. This feature ensures high availability and reliability by automatically trying alternative options when errors occur. Fallbacks can be configured at both the model level (multiple models) and provider level (multiple providers), providing multiple layers of redundancy.

*النسخ الاحتياطي يتيح التبديل التلقائي إلى نماذج أو مزودين احتياطيين عند فشل الخيارات الأساسية. هذه الميزة تضمن توفر عالي وموثوقية عن طريق المحاولة التلقائية للخيارات البديلة عند حدوث أخطاء. النسخ الاحتياطي يمكن تكوينه على مستوى النموذج (نماذج متعددة) ومستوى المزود (مزودون متعددون)، مما يوفر طبقات متعددة من التكرار.*

## Feature Importance

Fallbacks are essential for production applications that require high availability. Without fallbacks, a single model or provider failure can cause complete service outages. Fallbacks provide resilience, ensuring applications continue working even when individual components fail, maintaining service availability and user satisfaction.

*النسخ الاحتياطي ضروري لتطبيقات الإنتاج التي تتطلب توفر عالي. بدون النسخ الاحتياطي، فشل نموذج أو مزود واحد يمكن أن يسبب انقطاعات خدمة كاملة. النسخ الاحتياطي يوفر المرونة، مما يضمن استمرار عمل التطبيقات حتى عند فشل المكونات الفردية، مما يحافظ على توفر الخدمة ورضا المستخدم.*

## Key Benefits

### High Availability
Ensure requests succeed even if primary models or providers fail. Fallbacks automatically try alternatives, providing seamless failover without user-visible errors.

*تأكد من نجاح الطلبات حتى إذا فشلت النماذج أو المزودون الأساسيون. النسخ الاحتياطي يحاول تلقائياً البدائل، مما يوفر تبديلاً سلساً دون أخطاء مرئية للمستخدم.*

### Reliability
Multiple fallback layers provide redundancy, ensuring service continues even with multiple failures. This reliability is crucial for critical applications.

*طبقات النسخ الاحتياطي المتعددة توفر التكرار، مما يضمن استمرار الخدمة حتى مع فشل متعدد. هذه الموثوقية ضرورية للتطبيقات الحرجة.*

### Cost Optimization
Try cheaper models first, falling back to more expensive options only when needed. This optimizes costs while maintaining quality.

*جرب النماذج الأرخص أولاً، مع التراجع إلى الخيارات الأغلى فقط عند الحاجة. هذا يحسن التكاليف مع الحفاظ على الجودة.*

## Model Fallbacks

Use multiple models as fallbacks.

*استخدم نماذج متعددة كنسخ احتياطي.*

```python
from app.builders import ChatRequestBuilder

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_model_fallbacks(
        "anthropic/claude-sonnet-4",
        "google/gemini-2.5-flash"
    )
    .build())
```

## How It Works

1. First tries "openai/gpt-4o"
   *يحاول أولاً "openai/gpt-4o"*
2. If fails, tries "anthropic/claude-sonnet-4"
   *إذا فشل، يحاول "anthropic/claude-sonnet-4"*
3. If fails, tries "google/gemini-2.5-flash"
   *إذا فشل، يحاول "google/gemini-2.5-flash"*

## Provider Fallbacks

Provider fallbacks are handled automatically by OpenRouter when `allow_fallbacks` is enabled (default).

*النسخ الاحتياطي للمزود يتم التعامل معه تلقائياً من قبل OpenRouter عندما يكون `allow_fallbacks` مفعلاً (افتراضي).*

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_provider_order(["anthropic", "openai"])
    .build())
```

## Disable Fallbacks

*تعطيل النسخ الاحتياطي*

```python
from app.models.requests import ProviderConfig

provider_config = ProviderConfig(allow_fallbacks=False)
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .build())
request.provider = provider_config
```

## Use Cases

- **High Availability**: Ensure requests succeed even if one model/provider fails
  *التوفر العالي: تأكد من نجاح الطلبات حتى إذا فشل نموذج/مزود واحد*
- **Cost Optimization**: Try cheaper models first
  *تحسين التكلفة: جرب النماذج الأرخص أولاً*
- **Performance**: Try faster models first
  *الأداء: جرب النماذج الأسرع أولاً*

