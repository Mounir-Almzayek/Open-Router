# Model Selection

## Feature Overview

Model selection is the foundation of every AI interaction. This feature allows you to choose which AI model processes your requests, configure fallback options for reliability, and use model variants to optimize for cost, speed, or specific capabilities.

*اختيار النموذج هو أساس كل تفاعل مع الذكاء الاصطناعي. تتيح لك هذه الميزة اختيار النموذج الذي يعالج طلباتك، وتكوين خيارات النسخ الاحتياطي للاعتمادية، واستخدام متغيرات النموذج لتحسين التكلفة أو السرعة أو القدرات المحددة.*

## Key Benefits

### High Availability Through Fallbacks
Model fallbacks ensure your application continues working even if your primary model is unavailable. When the first model fails, the system automatically tries the next one in your fallback chain, providing seamless failover without user-visible errors.

*ضمانات النسخ الاحتياطي للنموذج استمرار عمل تطبيقك حتى لو كان النموذج الأساسي غير متاح. عند فشل النموذج الأول، يحاول النظام تلقائياً النموذج التالي في سلسلة النسخ الاحتياطي، مما يوفر تبديلاً سلساً دون أخطاء مرئية للمستخدم.*

### Cost Optimization with Variants
Model variants allow you to access the same model with different configurations optimized for specific needs. The `:free` variant provides cost-free access for testing, while `:floor` finds the lowest-priced provider, helping you minimize expenses without sacrificing functionality.

*تسمح متغيرات النموذج بالوصول إلى نفس النموذج بإعدادات مختلفة محسّنة لاحتياجات محددة. يوفر المتغير `:free` وصولاً مجانياً للاختبار، بينما يجد `:floor` المزود الأقل سعراً، مما يساعدك على تقليل النفقات دون التضحية بالوظائف.*

### Performance Tuning
Different models and variants offer different performance characteristics. Use `:nitro` for fastest responses, `:extended` for longer context windows, or `:thinking` for complex reasoning tasks. This flexibility lets you match the model to your specific performance requirements.

*تقدم النماذج والمتغيرات المختلفة خصائص أداء مختلفة. استخدم `:nitro` للحصول على أسرع الاستجابات، أو `:extended` لنوافذ سياق أطول، أو `:thinking` لمهام التفكير المعقدة. هذه المرونة تتيح لك مطابقة النموذج مع متطلبات الأداء المحددة.*

## Use Cases

### Production Applications with High Reliability Requirements
For critical production systems, use model fallbacks to ensure 99.9% uptime. Configure your primary model (e.g., GPT-4) with fallbacks to Claude and Gemini, so if one provider experiences issues, your application automatically switches to another.

*لأنظمة الإنتاج الحرجة، استخدم النسخ الاحتياطي للنموذج لضمان وقت تشغيل 99.9%. قم بتكوين نموذجك الأساسي (مثل GPT-4) مع نسخ احتياطية إلى Claude و Gemini، بحيث إذا واجه مزود مشاكل، ينتقل تطبيقك تلقائياً إلى آخر.*

### Development and Testing
Use the `:free` variant during development to test functionality without incurring costs. This is especially valuable when iterating on prompts or testing new features, allowing unlimited experimentation within free tier limits.

*استخدم المتغير `:free` أثناء التطوير لاختبار الوظائف دون تكبد تكاليف. هذا مفيد بشكل خاص عند التكرار على المطالبات أو اختبار الميزات الجديدة، مما يسمح بتجارب غير محدودة ضمن حدود الطبقة المجانية.*

### Cost-Sensitive Applications
For applications processing high volumes of requests, use `:floor` variant to automatically route to the cheapest available provider. Combine this with fallbacks to maintain quality while minimizing costs across thousands of requests.

*للتطبيقات التي تعالج أحجاماً كبيرة من الطلبات، استخدم متغير `:floor` للتوجيه تلقائياً إلى أرخص مزود متاح. اجمع هذا مع النسخ الاحتياطي للحفاظ على الجودة مع تقليل التكاليف عبر آلاف الطلبات.*

### Real-Time Applications
Use `:nitro` variant for chat applications, customer support bots, or any scenario requiring sub-second response times. This variant prioritizes speed over other factors, ensuring users get immediate feedback.

*استخدم متغير `:nitro` لتطبيقات الدردشة، أو روبوتات دعم العملاء، أو أي سيناريو يتطلب أوقات استجابة أقل من الثانية. يعطي هذا المتغير الأولوية للسرعة على العوامل الأخرى، مما يضمن حصول المستخدمين على ردود فورية.*

## Performance Considerations

### Fallback Latency
Model fallbacks add minimal latency (typically 50-200ms) when the primary model fails. However, this is far better than complete request failure. The system only attempts fallbacks on actual errors, not for slow responses, so successful requests maintain their original speed.

*يضيف النسخ الاحتياطي للنموذج حد أدنى من زمن الانتظار (عادة 50-200 مللي ثانية) عند فشل النموذج الأساسي. ومع ذلك، هذا أفضل بكثير من فشل الطلب الكامل. يحاول النظام النسخ الاحتياطي فقط عند الأخطاء الفعلية، وليس للاستجابات البطيئة، لذا تحافظ الطلبات الناجحة على سرعتها الأصلية.*

### Variant Performance Impact
Different variants have different performance characteristics:
- `:nitro` - Fastest response times, optimized for speed
- `:extended` - Slightly slower but supports much longer contexts
- `:thinking` - Slower due to additional reasoning steps, but produces better results for complex tasks
- `:free` - May have rate limits and slower response times

*للمتغيرات المختلفة خصائص أداء مختلفة:*
*- `:nitro` - أسرع أوقات الاستجابة، محسّن للسرعة*
*- `:extended` - أبطأ قليلاً لكنه يدعم سياقات أطول بكثير*
*- `:thinking` - أبطأ بسبب خطوات التفكير الإضافية، لكنه ينتج نتائج أفضل للمهام المعقدة*
*- `:free` - قد يكون له حدود معدل وأوقات استجابة أبطأ*

## Cost Implications

### Fallback Costs
Fallbacks only incur costs when they're actually used. If your primary model succeeds, you only pay for that model. Fallbacks provide insurance against failures without adding costs to successful requests.

*النسخ الاحتياطي يتحمل التكاليف فقط عند استخدامه فعلياً. إذا نجح نموذجك الأساسي، تدفع فقط مقابل ذلك النموذج. يوفر النسخ الاحتياطي تأميناً ضد الفشل دون إضافة تكاليف للطلبات الناجحة.*

### Variant Cost Savings
Model variants can significantly reduce costs:
- `:free` - Zero cost (within rate limits)
- `:floor` - Automatically finds cheapest provider (can save 20-50% vs default)
- Standard variants - Same pricing as base model

*يمكن لمتغيرات النموذج تقليل التكاليف بشكل كبير:*
*- `:free` - تكلفة صفر (ضمن حدود المعدل)*
*- `:floor` - يجد تلقائياً أرخص مزود (يمكن أن يوفر 20-50% مقابل الافتراضي)*
*- المتغيرات القياسية - نفس التسعير كنموذج الأساس*

### Optimization Strategy
For cost optimization, start with `:floor` variant to minimize per-request costs. Add fallbacks only for critical paths where reliability is more important than cost. Use `:free` extensively during development to reduce testing costs.

*لتحسين التكلفة، ابدأ بمتغير `:floor` لتقليل تكاليف كل طلب. أضف النسخ الاحتياطي فقط للمسارات الحرجة حيث تكون الموثوقية أكثر أهمية من التكلفة. استخدم `:free` بشكل واسع أثناء التطوير لتقليل تكاليف الاختبار.*

## Best Practices

### Fallback Configuration
Always configure at least one fallback model for production applications. Choose fallbacks from different providers (e.g., OpenAI → Anthropic → Google) to avoid provider-wide outages affecting all your fallbacks simultaneously.

*قم دائماً بتكوين نموذج نسخ احتياطي واحد على الأقل لتطبيقات الإنتاج. اختر النسخ الاحتياطية من مزودين مختلفين (مثل OpenAI → Anthropic → Google) لتجنب تأثير انقطاعات المزود على جميع النسخ الاحتياطية في نفس الوقت.*

### Variant Selection
Match variants to your use case:
- Use `:free` for development and non-critical features
- Use `:floor` for high-volume, cost-sensitive applications
- Use `:nitro` for real-time user-facing applications
- Use `:extended` when processing long documents or conversations
- Use `:thinking` for complex analysis, math, or reasoning tasks

*طابق المتغيرات مع حالة الاستخدام:*
*- استخدم `:free` للتطوير والميزات غير الحرجة*
*- استخدم `:floor` للتطبيقات عالية الحجم والحساسة للتكلفة*
*- استخدم `:nitro` للتطبيقات الموجهة للمستخدم في الوقت الفعلي*
*- استخدم `:extended` عند معالجة المستندات أو المحادثات الطويلة*
*- استخدم `:thinking` للتحليل المعقد، الرياضيات، أو مهام التفكير*

### Model Selection Strategy
Choose your primary model based on task requirements:
- GPT-4o: Best overall performance, great for general tasks
- Claude Sonnet 4: Excellent for long context and analysis
- Gemini 2.5 Flash: Fast and cost-effective for simple tasks
- Specialized models: Use domain-specific models (e.g., Whisper for audio) when available

*اختر نموذجك الأساسي بناءً على متطلبات المهمة:*
*- GPT-4o: أفضل أداء عام، رائع للمهام العامة*
*- Claude Sonnet 4: ممتاز للسياق الطويل والتحليل*
*- Gemini 2.5 Flash: سريع وفعال من حيث التكلفة للمهام البسيطة*
*- النماذج المتخصصة: استخدم النماذج الخاصة بالمجال (مثل Whisper للصوت) عند التوفر*

## When NOT to Use

### Don't Use Too Many Fallbacks
Avoid configuring more than 3-4 fallback models. Each additional fallback adds complexity and potential latency. For most applications, 1-2 fallbacks provide sufficient reliability without over-engineering.

*تجنب تكوين أكثر من 3-4 نماذج نسخ احتياطي. كل نسخ احتياطي إضافي يضيف تعقيداً وزمن انتظار محتملاً. لمعظم التطبيقات، يوفر 1-2 نسخ احتياطي موثوقية كافية دون هندسة زائدة.*

### Don't Use Free Variant in Production
The `:free` variant has strict rate limits and may be slower. Never use it for production workloads where reliability and performance matter. Reserve it exclusively for development and testing.

*المتغير `:free` له حدود معدل صارمة وقد يكون أبطأ. لا تستخدمه أبداً لأحمال عمل الإنتاج حيث تكون الموثوقية والأداء مهمة. احتفظ به حصرياً للتطوير والاختبار.*

### Don't Mix Incompatible Variants
Some variant combinations don't make sense. For example, don't use `:nitro` (speed) with `:thinking` (thoroughness) - they optimize for opposite goals. Choose the variant that matches your primary requirement.

*بعض مجموعات المتغيرات لا معنى لها. على سبيل المثال، لا تستخدم `:nitro` (السرعة) مع `:thinking` (الدقة) - فهما يحسنان لأهداف متعارضة. اختر المتغير الذي يطابق متطلبك الأساسي.*

## Troubleshooting

### Fallbacks Not Triggering
If fallbacks aren't being used when expected, check:
1. The primary model may be succeeding (fallbacks only trigger on errors)
2. Verify your fallback models are correctly specified
3. Check that fallback models support the same features (e.g., multimodal)

*إذا لم يتم استخدام النسخ الاحتياطي عند التوقع، تحقق من:*
*1. قد يكون النموذج الأساسي ينجح (النسخ الاحتياطي يحدث فقط عند الأخطاء)*
*2. تحقق من أن نماذج النسخ الاحتياطي محددة بشكل صحيح*
*3. تحقق من أن نماذج النسخ الاحتياطي تدعم نفس الميزات (مثل متعدد الوسائط)*

### Variant Not Available
If a variant isn't working, it may not be supported for your chosen model. Check OpenRouter documentation for variant availability. Some variants are model-specific (e.g., `:thinking` only works with Claude models).

*إذا لم يعمل متغير، قد لا يكون مدعوماً للنموذج المختار. تحقق من وثائق OpenRouter لتوفر المتغير. بعض المتغيرات خاصة بالنموذج (مثل `:thinking` يعمل فقط مع نماذج Claude).*

### High Costs with Floor Variant
If `:floor` isn't saving money, verify it's actually finding cheaper providers. Some models may not have cheaper alternatives available. Consider using specific cheaper models directly instead of relying on `:floor`.

*إذا لم يوفر `:floor` المال، تحقق من أنه يجد فعلياً مزودين أرخص. قد لا يكون لبعض النماذج بدائل أرخص متاحة. فكر في استخدام نماذج أرخص محددة مباشرة بدلاً من الاعتماد على `:floor`.*

## Basic Usage

```python
from app.builders import ChatRequestBuilder

builder = ChatRequestBuilder()
request = builder.with_model("openai/gpt-4o").build()
```

## Model Fallbacks

Configure multiple models as fallbacks to ensure high availability:

*قم بتكوين نماذج متعددة كنسخ احتياطي لضمان توفر عالي:*

```python
request = builder.with_model("openai/gpt-4o").with_model_fallbacks(
    "anthropic/claude-sonnet-4",
    "google/gemini-2.5-flash"
).build()
```

This configuration will try GPT-4o first, then Claude if GPT-4o fails, then Gemini if Claude fails. This provides three layers of redundancy for critical applications.

*سيحاول هذا التكوين GPT-4o أولاً، ثم Claude إذا فشل GPT-4o، ثم Gemini إذا فشل Claude. يوفر هذا ثلاث طبقات من التكرار للتطبيقات الحرجة.*

## Model Variants

Model variants provide optimized configurations for specific use cases:

*توفر متغيرات النموذج إعدادات محسّنة لحالات استخدام محددة:*

```python
from app.enums import ModelVariant

request = builder.with_model("openai/gpt-4o").with_model_variant(
    ModelVariant.FREE
).build()
```

### Available Variants

- `:free` - Free tier access (limited rate, for development/testing)
  *`:free` - وصول الطبقة المجانية (معدل محدود، للتطوير/الاختبار)*
- `:extended` - Extended context window (for long documents/conversations)
  *`:extended` - نافذة سياق ممتدة (للمستندات/المحادثات الطويلة)*
- `:thinking` - Thinking mode (for complex reasoning, Claude models only)
  *`:thinking` - وضع التفكير (للتفكير المعقد، نماذج Claude فقط)*
- `:online` - Online search enabled (access to real-time web information)
  *`:online` - البحث عبر الإنترنت مفعّل (الوصول إلى معلومات الويب في الوقت الفعلي)*
- `:nitro` - Fast mode (optimized for speed and low latency)
  *`:nitro` - وضع سريع (محسّن للسرعة وزمن الانتظار المنخفض)*
- `:floor` - Lowest price (automatically routes to cheapest provider)
  *`:floor` - أقل سعر (يوجه تلقائياً إلى أرخص مزود)*

## Advanced Example: Production-Ready Configuration

Here's a complete example for a production application with cost optimization and reliability:

*إليك مثال كامل لتطبيق إنتاج مع تحسين التكلفة والموثوقية:*

```python
from app.builders import ChatRequestBuilder
from app.enums import ModelVariant

# Production configuration with fallbacks and cost optimization
# تكوين الإنتاج مع النسخ الاحتياطي وتحسين التكلفة
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_model_variant(ModelVariant.FLOOR)  # Find cheapest provider
    .with_model_fallbacks(
        "anthropic/claude-sonnet-4",  # First fallback
        "google/gemini-2.5-flash"     # Second fallback
    )
    .with_text("Analyze this data")
    .build())
```

This configuration:
- Uses `:floor` to minimize costs
- Has two fallback models from different providers for reliability
- Automatically handles failures gracefully

*هذا التكوين:*
*- يستخدم `:floor` لتقليل التكاليف*
*- لديه نموذجان نسخ احتياطي من مزودين مختلفين للموثوقية*
*- يتعامل تلقائياً مع الفشل بشكل سلس*
