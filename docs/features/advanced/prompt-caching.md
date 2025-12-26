# Prompt Caching

## Feature Overview

Prompt caching allows you to cache parts of your prompts to reduce costs and improve response times. By caching frequently used prompt content (like system prompts or templates), you only pay for those tokens once, significantly reducing costs for repeated interactions. Different providers support different caching mechanisms, but all provide substantial cost savings for content that doesn't change frequently.

*التخزين المؤقت للمطالب يسمح لك بتخزين أجزاء من مطالبك مؤقتاً لتقليل التكاليف وتحسين أوقات الاستجابة. من خلال تخزين محتوى المطالب المستخدم بشكل متكرر (مثل مطالب النظام أو القوالب) مؤقتاً، تدفع مقابل تلك الرموز المميزة مرة واحدة فقط، مما يقلل التكاليف بشكل كبير للتفاعلات المتكررة. المزودون المختلفون يدعمون آليات تخزين مؤقت مختلفة، لكن جميعهم يوفرون توفيراً كبيراً في التكاليف للمحتوى الذي لا يتغير بشكل متكرر.*

## Feature Importance

Prompt caching is one of the most effective ways to reduce AI API costs, especially for applications with repeated system prompts, templates, or instructions. For high-volume applications, caching can reduce costs by 30-70% while improving response times. This makes prompt caching essential for production applications with cost constraints.

*التخزين المؤقت للمطالب هو أحد أكثر الطرق فعالية لتقليل تكاليف AI API، خاصة للتطبيقات مع مطالب النظام المتكررة أو القوالب أو التعليمات. للتطبيقات عالية الحجم، التخزين المؤقت يمكن أن يقلل التكاليف بنسبة 30-70% مع تحسين أوقات الاستجابة. هذا يجعل التخزين المؤقت للمطالب ضرورياً لتطبيقات الإنتاج مع قيود التكلفة.*

## Supported Providers

### OpenAI
Automatic caching for repeated prompts.

```python
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import CacheTTL

# Add cache control to text content
text_content = ContentBuilder.create_text_with_cache(
    "This is a system prompt that will be cached",
    ttl=CacheTTL.ONE_HOUR
)

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_message(MessageRole.SYSTEM, [text_content])
    .with_text("User query")
    .build())
```

### Anthropic
Cache control with TTL options.

```python
from app.models.requests.content import CacheControl
from app.enums import CacheControlType, CacheTTL

cache_control = CacheControl(
    type=CacheControlType.EPHEMERAL,
    ttl=CacheTTL.FIVE_MINUTES
)

text_content = TextContent(
    text="Cached prompt text",
    cache_control=cache_control
)
```

### Gemini
Implicit caching for repeated content.

## Cache TTL Options

```python
from app.enums import CacheTTL

# Available options:
# - CacheTTL.FIVE_MINUTES: 5 minutes
# - CacheTTL.ONE_HOUR: 1 hour
```

## Basic Usage

```python
from app.builders import ChatRequestBuilder
from app.enums import CacheTTL

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_prompt_caching(
        "This system prompt will be cached",
        ttl=CacheTTL.ONE_HOUR
    )
    .with_text("User query")
    .build())
```

## Key Benefits

### Significant Cost Reduction
Caching frequently used prompt content can reduce costs by 30-70% for high-volume applications. System prompts, templates, and instructions that don't change are charged only once, regardless of how many times they're used.

*التخزين المؤقت لمحتوى المطالب المستخدم بشكل متكرر يمكن أن يقلل التكاليف بنسبة 30-70% للتطبيقات عالية الحجم. مطالب النظام والقوالب والتعليمات التي لا تتغير يتم تحصيلها مرة واحدة فقط، بغض النظر عن عدد مرات استخدامها.*

### Improved Response Times
Cached content is retrieved faster than generating it from scratch, reducing latency for repeated requests. This improves user experience, especially for applications with consistent system prompts.

*المحتوى المخزن مؤقتاً يتم استرجاعه بشكل أسرع من توليده من الصفر، مما يقلل زمن الانتظار للطلبات المتكررة. هذا يحسن تجربة المستخدم، خاصة للتطبيقات مع مطالب نظام متسقة.*

### Scalability
Caching enables better scalability by reducing token consumption per request. As request volume increases, caching benefits compound, making high-volume applications more cost-effective.

*التخزين المؤقت يتيح قابلية توسع أفضل من خلال تقليل استهلاك الرموز المميزة لكل طلب. مع زيادة حجم الطلبات، تتراكم فوائد التخزين المؤقت، مما يجعل التطبيقات عالية الحجم أكثر فعالية من حيث التكلفة.*

## Use Cases

### System Prompts
Cache system prompts that don't change frequently. Long system prompts that define AI behavior, constraints, or instructions are perfect candidates for caching, providing substantial cost savings.

*قم بتخزين مطالب النظام التي لا تتغير بشكل متكرر مؤقتاً. مطالب النظام الطويلة التي تحدد سلوك الذكاء الاصطناعي أو القيود أو التعليمات هي مرشحة مثالية للتخزين المؤقت، مما يوفر توفيراً كبيراً في التكاليف.*

### Template Content
Cache template content that's reused across multiple requests. Document analysis templates, data extraction formats, and reusable instruction patterns benefit significantly from caching.

*قم بتخزين محتوى القالب المستخدم عبر طلبات متعددة مؤقتاً. قوالب تحليل المستندات وتنسيقات استخراج البيانات وأنماط التعليمات القابلة لإعادة الاستخدام تستفيد بشكل كبير من التخزين المؤقت.*

### High-Volume Applications
Applications processing thousands of requests with similar prompts benefit enormously from caching. Customer support bots, content moderation systems, and data processing pipelines can reduce costs significantly.

*التطبيقات التي تعالج آلاف الطلبات مع مطالب مماثلة تستفيد بشكل كبير من التخزين المؤقت. روبوتات دعم العملاء وأنظمة إدارة المحتوى وخطوط معالجة البيانات يمكن أن تقلل التكاليف بشكل كبير.*

### Multi-Tenant Systems
Systems serving multiple users with shared system prompts or templates can cache shared content once and reuse it across all users, maximizing cost efficiency.

*الأنظمة التي تخدم مستخدمين متعددين مع مطالب نظام أو قوالب مشتركة يمكنها تخزين المحتوى المشترك مؤقتاً مرة واحدة وإعادة استخدامه عبر جميع المستخدمين، مما يعظم كفاءة التكلفة.*

## Performance Considerations

### Cache Hit Rate
Higher cache hit rates provide more cost savings. Design prompts to maximize cacheable content. Keep variable content separate from cacheable content to improve hit rates.

*معدلات ضربات التخزين المؤقت الأعلى توفر المزيد من توفير التكاليف. صمم المطالب لتعظيم المحتوى القابل للتخزين المؤقت. حافظ على المحتوى المتغير منفصلاً عن المحتوى القابل للتخزين المؤقت لتحسين معدلات الضربات.*

### TTL Selection
Choose TTL based on how frequently content changes. Longer TTLs provide more savings but may serve stale content. Shorter TTLs ensure freshness but reduce caching benefits. Balance freshness with cost savings.

*اختر TTL بناءً على مدى تكرار تغيير المحتوى. TTLs الأطول توفر المزيد من التوفير لكنها قد تخدم محتوى قديم. TTLs الأقصر تضمن الحداثة لكنها تقلل فوائد التخزين المؤقت. وازن الحداثة مع توفير التكاليف.*

### Exact Match Requirement
Cached content must match exactly—even small changes invalidate the cache. Keep cacheable content stable and separate from variable content to maximize cache effectiveness.

*المحتوى المخزن مؤقتاً يجب أن يطابق بدقة—حتى التغييرات الصغيرة تبطل التخزين المؤقت. حافظ على المحتوى القابل للتخزين المؤقت مستقراً ومنفصلاً عن المحتوى المتغير لتعظيم فعالية التخزين المؤقت.*

### Provider Differences
Different providers have different caching implementations and TTL options. Understand your provider's caching behavior to optimize usage. Some providers cache automatically, while others require explicit configuration.

*المزودون المختلفون لديهم تطبيقات تخزين مؤقت وخيارات TTL مختلفة. افهم سلوك التخزين المؤقت لمزودك لتحسين الاستخدام. بعض المزودين يخزنون مؤقتاً تلقائياً، بينما يتطلب آخرون تكويناً صريحاً.*

## Cost Implications

### Token Cost Savings
Cached content is charged only once, regardless of how many times it's used. For a system prompt used in 1000 requests, caching saves 999x the token cost of that prompt. This compounds significantly for high-volume applications.

*المحتوى المخزن مؤقتاً يتم تحصيله مرة واحدة فقط، بغض النظر عن عدد مرات استخدامه. لمطلب نظام مستخدم في 1000 طلب، التخزين المؤقت يوفر 999x تكلفة الرموز المميزة لذلك المطلب. هذا يتراكم بشكل كبير للتطبيقات عالية الحجم.*

### Cost Reduction Potential
For applications with repeated system prompts or templates, caching can reduce costs by 30-70%. The exact savings depend on the ratio of cacheable to variable content and request volume.

*للتطبيقات مع مطالب النظام أو القوالب المتكررة، التخزين المؤقت يمكن أن يقلل التكاليف بنسبة 30-70%. التوفير الدقيق يعتمد على نسبة المحتوى القابل للتخزين المؤقت إلى المحتوى المتغير وحجم الطلب.*

### TTL Impact on Costs
Longer TTLs provide more cost savings by keeping content cached longer. However, balance TTL length with content freshness requirements. Very long TTLs may serve outdated content.

*TTLs الأطول توفر المزيد من توفير التكاليف من خلال الحفاظ على المحتوى مخزناً مؤقتاً لفترة أطول. ومع ذلك، وازن طول TTL مع متطلبات حداثة المحتوى. TTLs الطويلة جداً قد تخدم محتوى قديم.*

## Best Practices

### Cache System Prompts
Always cache system prompts that don't change. System prompts are typically long and used in every request, making them ideal candidates for caching and providing substantial cost savings.

*قم دائماً بتخزين مطالب النظام التي لا تتغير مؤقتاً. مطالب النظام عادة ما تكون طويلة ومستخدمة في كل طلب، مما يجعلها مرشحة مثالية للتخزين المؤقت وتوفر توفيراً كبيراً في التكاليف.*

### Use Appropriate TTL
Choose TTL based on content update frequency. Use longer TTLs (1 hour) for stable content like system prompts. Use shorter TTLs (5 minutes) for content that changes more frequently.

*اختر TTL بناءً على تكرار تحديث المحتوى. استخدم TTLs أطول (ساعة واحدة) للمحتوى المستقر مثل مطالب النظام. استخدم TTLs أقصر (5 دقائق) للمحتوى الذي يتغير بشكل أكثر تكراراً.*

### Monitor Cache Hit Rates
Track cache hit rates to understand caching effectiveness. High hit rates indicate good caching strategy. Low hit rates suggest content changes too frequently or caching isn't configured correctly.

*تتبع معدلات ضربات التخزين المؤقت لفهم فعالية التخزين المؤقت. معدلات الضربات العالية تشير إلى استراتيجية تخزين مؤقت جيدة. معدلات الضربات المنخفضة تشير إلى أن المحتوى يتغير بشكل متكرر جداً أو أن التخزين المؤقت غير مكون بشكل صحيح.*

### Separate Cacheable Content
Keep cacheable content (system prompts, templates) separate from variable content (user queries, dynamic data). This maximizes cache hit rates and ensures content is cached effectively.

*حافظ على المحتوى القابل للتخزين المؤقت (مطالب النظام، القوالب) منفصلاً عن المحتوى المتغير (استفسارات المستخدم، البيانات الديناميكية). هذا يعظم معدلات ضربات التخزين المؤقت ويضمن تخزين المحتوى مؤقتاً بفعالية.*

### Test Cache Behavior
Test caching with your specific use case to understand provider behavior and optimize TTL settings. Different providers may cache differently, so testing helps optimize configuration.

*اختبر التخزين المؤقت مع حالة الاستخدام المحددة لفهم سلوك المزود وتحسين إعدادات TTL. المزودون المختلفون قد يخزنون مؤقتاً بشكل مختلف، لذا الاختبار يساعد في تحسين التكوين.*

## When NOT to Use

### Don't Cache Frequently Changing Content
Avoid caching content that changes frequently or is unique to each request. Caching such content provides no benefit and may serve stale data. Only cache stable, reusable content.

*تجنب تخزين المحتوى الذي يتغير بشكل متكرر أو فريد لكل طلب مؤقتاً. تخزين مثل هذا المحتوى مؤقتاً لا يوفر فائدة وقد يخدم بيانات قديمة. قم بتخزين المحتوى المستقر والقابل لإعادة الاستخدام مؤقتاً فقط.*

### Don't Use Very Short TTLs
Avoid very short TTLs (under 1 minute) unless content changes very frequently. Very short TTLs provide minimal caching benefits and may not be worth the configuration overhead.

*تجنب TTLs قصيرة جداً (أقل من دقيقة واحدة) ما لم يتغير المحتوى بشكل متكرر جداً. TTLs القصيرة جداً توفر فوائد تخزين مؤقت ضئيلة وقد لا تستحق حمل التكوين.*

### Don't Ignore Cache Invalidation
Don't assume cached content stays valid indefinitely. Cache invalidation happens automatically after TTL expires. Plan for cache misses and ensure your application handles both cached and uncached scenarios.

*لا تفترض أن المحتوى المخزن مؤقتاً يبقى صالحاً إلى ما لا نهاية. إبطال التخزين المؤقت يحدث تلقائياً بعد انتهاء TTL. خطط لعدم وجود التخزين المؤقت وتأكد من أن تطبيقك يتعامل مع سيناريوهات التخزين المؤقت وغير المخزنة مؤقتاً.*

## Troubleshooting

### Low Cache Hit Rates
If cache hit rates are low, review content stability. Ensure cacheable content doesn't change between requests. Check that caching is configured correctly. Verify content matches exactly for cache hits.

*إذا كانت معدلات ضربات التخزين المؤقت منخفضة، راجع استقرار المحتوى. تأكد من أن المحتوى القابل للتخزين المؤقت لا يتغير بين الطلبات. تحقق من أن التخزين المؤقت مكون بشكل صحيح. تحقق من تطابق المحتوى بدقة لضربات التخزين المؤقت.*

### Unexpected Costs
If costs aren't reducing as expected, verify caching is working. Check cache hit rates and ensure content is being cached. Review TTL settings and ensure they're appropriate for your use case.

*إذا لم تنخفض التكاليف كما هو متوقع، تحقق من أن التخزين المؤقت يعمل. تحقق من معدلات ضربات التخزين المؤقت وتأكد من أن المحتوى يتم تخزينه مؤقتاً. راجع إعدادات TTL وتأكد من أنها مناسبة لحالة الاستخدام.*

### Stale Content Issues
If cached content becomes stale, reduce TTL or ensure content updates invalidate cache. Balance freshness requirements with cost savings. Consider shorter TTLs for content that needs frequent updates.

*إذا أصبح المحتوى المخزن مؤقتاً قديماً، قلل TTL أو تأكد من أن تحديثات المحتوى تبطل التخزين المؤقت. وازن متطلبات الحداثة مع توفير التكاليف. فكر في TTLs أقصر للمحتوى الذي يحتاج تحديثات متكررة.*

### Provider-Specific Issues
If caching isn't working, check provider-specific requirements. Some providers require explicit cache configuration. Verify your provider supports caching and that configuration is correct.

*إذا لم يعمل التخزين المؤقت، تحقق من المتطلبات الخاصة بالمزود. بعض المزودين يتطلبون تكوين تخزين مؤقت صريح. تحقق من أن مزودك يدعم التخزين المؤقت وأن التكوين صحيح.*

## Example

```python
# System prompt that will be cached
system_prompt = """You are a data analyst. 
Analyze the provided data and return insights in JSON format."""

# User queries (system prompt is cached)
request1 = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_prompt_caching(system_prompt, ttl=CacheTTL.ONE_HOUR)
    .with_text("Analyze sales data: [data]")
    .build())

request2 = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_prompt_caching(system_prompt, ttl=CacheTTL.ONE_HOUR)
    .with_text("Analyze customer data: [data]")
    .build())
# System prompt is cached, only user queries are charged
```

