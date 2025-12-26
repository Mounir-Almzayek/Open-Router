# Web Search Plugin

## Feature Overview

The web search plugin enables AI models to search the internet and retrieve real-time information to answer queries. Instead of relying solely on training data, models can access current information from the web, providing up-to-date answers with source citations. This feature transforms AI from a static knowledge system into a dynamic information assistant that can access the latest data.

*إضافة البحث على الويب تمكن نماذج الذكاء الاصطناعي من البحث على الإنترنت واسترجاع المعلومات في الوقت الفعلي للإجابة على الاستفسارات. بدلاً من الاعتماد فقط على بيانات التدريب، يمكن للنماذج الوصول إلى المعلومات الحالية من الويب، مما يوفر إجابات حديثة مع استشهادات المصدر. هذه الميزة تحول الذكاء الاصطناعي من نظام معرفة ثابت إلى مساعد معلومات ديناميكي يمكنه الوصول إلى أحدث البيانات.*

## Feature Importance

Web search is essential for applications that need current information—news, prices, events, or any data that changes over time. Without web search, AI models are limited to their training data cutoff date, making them unable to answer questions about recent events or current information. Web search bridges this gap, enabling AI to stay current and provide accurate, timely information.

*البحث على الويب ضروري للتطبيقات التي تحتاج معلومات حالية—الأخبار والأسعار والأحداث أو أي بيانات تتغير بمرور الوقت. بدون البحث على الويب، نماذج الذكاء الاصطناعي محدودة ببيانات التدريب حتى تاريخ القطع، مما يجعلها غير قادرة على الإجابة على الأسئلة حول الأحداث الأخيرة أو المعلومات الحالية. البحث على الويب يربط هذه الفجوة، مما يتيح للذكاء الاصطناعي البقاء محدثاً وتوفير معلومات دقيقة وفي الوقت المناسب.*

## Key Benefits

### Real-time Information
Get up-to-date information from the web, enabling answers about current events, latest news, recent prices, and contemporary information that wasn't available during model training.

*احصل على معلومات حديثة من الويب، مما يتيح الإجابات حول الأحداث الحالية وأحدث الأخبار والأسعار الحديثة والمعلومات المعاصرة التي لم تكن متاحة أثناء تدريب النموذج.*

### Grounding and Citations
Connect model answers to real sources with citations, providing transparency and verifiability. Users can verify information by checking cited sources, building trust in AI responses.

*اربط إجابات النموذج بمصادر حقيقية مع استشهادات، مما يوفر الشفافية والقابلية للتحقق. يمكن للمستخدمين التحقق من المعلومات عن طريق فحص المصادر المستشهد بها، مما يبني الثقة في استجابات الذكاء الاصطناعي.*

### Improved Accuracy
Access current information improves answer accuracy for time-sensitive queries. Instead of potentially outdated training data, models use real-time web information for more accurate responses.

*الوصول إلى المعلومات الحالية يحسن دقة الإجابات للاستفسارات الحساسة للوقت. بدلاً من بيانات التدريب المحتمل أن تكون قديمة، تستخدم النماذج معلومات الويب في الوقت الفعلي لاستجابات أكثر دقة.*

### Comprehensive Coverage
Web search enables coverage of topics not well-represented in training data. Models can find and use information about niche topics, recent developments, or specialized domains.

*البحث على الويب يتيح تغطية مواضيع غير ممثلة جيداً في بيانات التدريب. يمكن للنماذج العثور على واستخدام معلومات حول مواضيع متخصصة أو التطورات الأخيرة أو المجالات المتخصصة.*

## Use Cases

### Latest News and Events
Search for latest news, current events, and recent developments. This enables applications that need to stay current with world events, industry news, or specific topics.

*ابحث عن أحدث الأخبار والأحداث الحالية والتطورات الأخيرة. هذا يتيح التطبيقات التي تحتاج إلى البقاء محدثة مع أحداث العالم أو أخبار الصناعة أو مواضيع محددة.*

### Current Prices and Market Data
Get current prices, stock quotes, exchange rates, and market data. This enables financial applications, e-commerce tools, and market analysis systems that need real-time pricing information.

*احصل على الأسعار الحالية وعروض الأسهم وأسعار الصرف وبيانات السوق. هذا يتيح التطبيقات المالية وأدوات التجارة الإلكترونية وأنظمة تحليل السوق التي تحتاج معلومات تسعير في الوقت الفعلي.*

### Product Information
Find information about new products, specifications, reviews, and availability. This enables product research tools, comparison services, and shopping assistants.

*ابحث عن معلومات حول المنتجات الجديدة والمواصفات والمراجعات والتوفر. هذا يتيح أدوات بحث المنتجات وخدمات المقارنة والمساعدين التسوق.*

### Research and Fact-Checking
Verify facts, check information accuracy, and research topics with current sources. This enables fact-checking tools, research assistants, and information verification systems.

*تحقق من الحقائق وتحقق من دقة المعلومات وابحث عن مواضيع بمصادر حالية. هذا يتيح أدوات التحقق من الحقائق والمساعدين البحث وأنظمة التحقق من المعلومات.*

## How to Use

### Basic Method
```python
from app.builders import ChatRequestBuilder

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("What are the latest developments in AI?")
    .with_web_search(max_results=5)
    .build())
```

### Advanced Method

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("What are the latest developments in AI?")
    .with_web_search(
        max_results=3,
        engine="native",  # or "exa"
        search_prompt="Custom search prompt"
    )
    .build())
```

## Practical Examples

### Example 1: News Search

```python
# Search for latest news in a specific field
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("What are the latest news about quantum computing?")
    .with_web_search(max_results=5)
    .build())
```

### Example 2: Search with Structured Output

```python
# Search with structured output to get organized information
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Find the latest AI research papers")
    .with_web_search(max_results=10)
    .with_structured_output(
        schema={
            "type": "object",
            "properties": {
                "papers": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "url": {"type": "string"},
                            "summary": {"type": "string"}
                        }
                    }
                }
            }
        },
        name="ResearchPapers"
    )
    .build())
```

## Performance Considerations

### Search Latency
Web search adds latency to responses as the model must search the web and process results. Expect longer response times compared to standard queries. The additional time is usually worth it for current information needs.

*البحث على الويب يضيف زمن انتظار للاستجابات لأن النموذج يجب أن يبحث على الويب ويعالج النتائج. توقع أوقات استجابة أطول مقارنة بالاستفسارات القياسية. الوقت الإضافي عادة ما يستحق ذلك لاحتياجات المعلومات الحالية.*

### Result Quality
Search result quality depends on query formulation and search engine capabilities. Clear, specific queries produce better results. Some search engines may provide more relevant results than others.

*جودة نتائج البحث تعتمد على صياغة الاستفسار وقدرات محرك البحث. الاستفسارات الواضحة والمحددة تنتج نتائج أفضل. بعض محركات البحث قد توفر نتائج أكثر صلة من غيرها.*

## Cost Implications

### Additional Costs
Web search adds additional costs beyond standard API calls. Search operations consume extra tokens and may have separate pricing. Consider costs when enabling web search for high-volume applications.

*البحث على الويب يضيف تكاليف إضافية تتجاوز استدعاءات API القياسية. عمليات البحث تستهلك رموزاً مميزة إضافية وقد يكون لها تسعير منفصل. ضع في الاعتبار التكاليف عند تمكين البحث على الويب للتطبيقات عالية الحجم.*

### Result Size Impact
More search results (higher max_results) consume more tokens and increase costs. Balance result quantity with cost considerations. Often 3-5 results provide sufficient information without excessive costs.

*المزيد من نتائج البحث (max_results أعلى) تستهلك المزيد من الرموز المميزة وتزيد التكاليف. وازن كمية النتائج مع اعتبارات التكلفة. غالباً ما توفر 3-5 نتائج معلومات كافية دون تكاليف مفرطة.*

## Best Practices

### Query Formulation
Write clear, specific queries to get better search results. Vague queries may return irrelevant results. Include context and specific information needs in your queries.

*اكتب استفسارات واضحة ومحددة للحصول على نتائج بحث أفضل. الاستفسارات الغامضة قد تعيد نتائج غير ذات صلة. اشمل السياق واحتياجات المعلومات المحددة في استفساراتك.*

### Result Count Optimization
Use appropriate max_results values—typically 3-5 results are sufficient. More results increase costs without proportional benefits. Test different values to find optimal settings.

*استخدم قيم max_results مناسبة—عادة ما تكون 3-5 نتائج كافية. المزيد من النتائج يزيد التكاليف دون فوائد متناسبة. اختبر قيم مختلفة للعثور على الإعدادات المثلى.*

### Engine Selection
Choose search engines based on your needs. Native search may be faster but limited to certain models. Exa search is available for all models and may provide different result quality.

*اختر محركات البحث بناءً على احتياجاتك. البحث الأصلي قد يكون أسرع لكنه محدود لنماذج معينة. بحث Exa متاح لجميع النماذج وقد يوفر جودة نتائج مختلفة.*

## When NOT to Use

### Don't Use for Static Information
Avoid web search for information that doesn't change or is well-covered in training data. Web search adds cost and latency without benefit for static information.

*تجنب البحث على الويب للمعلومات التي لا تتغير أو مغطاة جيداً في بيانات التدريب. البحث على الويب يضيف تكلفة وزمن انتظار دون فائدة للمعلومات الثابتة.*

### Don't Overuse Search
Avoid enabling web search for every query. Use it selectively for queries that need current information. Overuse increases costs and latency unnecessarily.

*تجنب تمكين البحث على الويب لكل استفسار. استخدمه بشكل انتقائي للاستفسارات التي تحتاج معلومات حالية. الإفراط في الاستخدام يزيد التكاليف وزمن الانتظار بشكل غير ضروري.*

## Troubleshooting

### Poor Search Results
If search results are poor, improve query formulation. Make queries more specific and include relevant context. Try different search engines or adjust max_results.

*إذا كانت نتائج البحث ضعيفة، حسّن صياغة الاستفسار. اجعل الاستفسارات أكثر تحديداً واشمل السياق ذي الصلة. جرب محركات بحث مختلفة أو اضبط max_results.*

### High Costs
If costs are high, reduce max_results. Use web search selectively only when current information is needed. Consider caching search results when appropriate.

*إذا كانت التكاليف عالية، قلل max_results. استخدم البحث على الويب بشكل انتقائي فقط عندما تكون المعلومات الحالية مطلوبة. فكر في تخزين نتائج البحث مؤقتاً عند الاقتضاء.*

## Important Notes

- Web search adds additional cost
  *البحث على الويب يضيف تكلفة إضافية*
- Native search is only available for some models
  *البحث الأصلي متاح فقط لبعض النماذج*
- Exa search is available for all models
  *بحث Exa متاح لجميع النماذج*

