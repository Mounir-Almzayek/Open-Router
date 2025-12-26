# Streaming

## Feature Overview

Streaming enables real-time, incremental response delivery from AI models. Instead of waiting for the complete response, you receive tokens as they're generated, providing immediate feedback to users and improving perceived performance. This feature is essential for chat applications, real-time assistants, and any scenario where user experience depends on quick response times.

*يتيح البث التدفقي تسليم الاستجابات من نماذج الذكاء الاصطناعي بشكل تدريجي وفي الوقت الفعلي. بدلاً من انتظار الاستجابة الكاملة، تتلقى الرموز المميزة أثناء توليدها، مما يوفر ردود فعل فورية للمستخدمين ويحسن الأداء المتصور. هذه الميزة ضرورية لتطبيقات الدردشة والمساعدين في الوقت الفعلي وأي سيناريو يعتمد فيه تجربة المستخدم على أوقات استجابة سريعة.*

## Feature Importance

Streaming transforms the user experience from waiting for complete responses to seeing content appear in real-time. This psychological effect significantly improves perceived performance, even when total response time remains the same. For chat applications, streaming is not just a nice-to-have—it's essential for creating natural, conversational interactions.

*يحول البث التدفقي تجربة المستخدم من انتظار الاستجابات الكاملة إلى رؤية المحتوى يظهر في الوقت الفعلي. هذا التأثير النفسي يحسن بشكل كبير الأداء المتصور، حتى عندما يبقى إجمالي وقت الاستجابة كما هو. لتطبيقات الدردشة، البث التدفقي ليس مجرد ميزة إضافية—إنه ضروري لإنشاء تفاعلات محادثة طبيعية.*

## Key Benefits

### Immediate User Feedback
Users see responses start appearing within milliseconds, creating a sense of responsiveness and engagement. This immediate feedback is crucial for maintaining user attention and creating a natural conversation flow.

*يرى المستخدمون بدء ظهور الاستجابات في غضون أجزاء من الثانية، مما يخلق إحساساً بالاستجابة والتفاعل. هذه التغذية الراجعة الفورية ضرورية للحفاظ على انتباه المستخدم وإنشاء تدفق محادثة طبيعي.*

### Perceived Performance Improvement
Even if total response time is identical, streaming makes applications feel faster because users start seeing results immediately. This psychological benefit significantly improves user satisfaction and engagement.

*حتى لو كان إجمالي وقت الاستجابة متطابقاً، يجعل البث التدفقي التطبيقات تبدو أسرع لأن المستخدمين يبدأون في رؤية النتائج فوراً. هذه الفائدة النفسية تحسن بشكل كبير رضا المستخدم والتفاعل.*

### Better Error Handling
With streaming, you can detect errors early and handle them gracefully before the entire response is generated. This allows for better error recovery and user communication.

*مع البث التدفقي، يمكنك اكتشاف الأخطاء مبكراً والتعامل معها بشكل سلس قبل توليد الاستجابة الكاملة. هذا يسمح بتحسين استعادة الأخطاء والتواصل مع المستخدم.*

### Resource Efficiency
Streaming allows you to process and display content incrementally, reducing memory usage for long responses. You can also cancel streams early if needed, saving resources.

*يسمح البث التدفقي بمعالجة وعرض المحتوى بشكل تدريجي، مما يقلل استخدام الذاكرة للاستجابات الطويلة. يمكنك أيضاً إلغاء التدفقات مبكراً إذا لزم الأمر، مما يوفر الموارد.*

### Natural Conversation Flow
For chat applications, streaming creates a natural conversation rhythm where responses appear word-by-word, mimicking human typing patterns. This creates a more engaging and human-like interaction.

*لتطبيقات الدردشة، يخلق البث التدفقي إيقاع محادثة طبيعي حيث تظهر الاستجابات كلمة بكلمة، مما يحاكي أنماط الكتابة البشرية. هذا يخلق تفاعلاً أكثر جاذبية وشبهاً بالإنسان.*

## Use Cases

### Chat Applications
Real-time chat interfaces require streaming to provide immediate feedback. Users expect to see responses appear progressively, creating a natural conversation experience similar to messaging apps.

*واجهات الدردشة في الوقت الفعلي تتطلب البث التدفقي لتوفير ردود فعل فورية. يتوقع المستخدمون رؤية الاستجابات تظهر تدريجياً، مما يخلق تجربة محادثة طبيعية مشابهة لتطبيقات المراسلة.*

### Customer Support Bots
Support chatbots benefit from streaming to show they're actively processing requests. Users see responses forming in real-time, reducing perceived wait time and improving satisfaction.

*تستفيد روبوتات دعم العملاء من البث التدفقي لإظهار أنها تعالج الطلبات بنشاط. يرى المستخدمون الاستجابات تتشكل في الوقت الفعلي، مما يقلل وقت الانتظار المتصور ويحسن الرضا.*

### Code Generation Tools
When generating code, streaming allows developers to see code appear incrementally, enabling early review and potential interruption if the direction is wrong. This improves the development workflow.

*عند توليد الكود، يسمح البث التدفقي للمطورين برؤية الكود يظهر تدريجياً، مما يتيح المراجعة المبكرة والانقطاع المحتمل إذا كان الاتجاه خاطئاً. هذا يحسن سير عمل التطوير.*

### Content Creation Assistants
Writing assistants that generate long-form content benefit from streaming, allowing users to see content develop in real-time and make adjustments as needed.

*مساعدو الكتابة الذين يولدون محتوى طويل الشكل يستفيدون من البث التدفقي، مما يسمح للمستخدمين برؤية المحتوى يتطور في الوقت الفعلي وإجراء التعديلات حسب الحاجة.*

### Real-Time Translation Services
Translation services use streaming to show translations appearing word-by-word, providing immediate feedback and allowing users to see progress even for long texts.

*تستخدم خدمات الترجمة البث التدفقي لإظهار الترجمات تظهر كلمة بكلمة، مما يوفر ردود فعل فورية ويسمح للمستخدمين برؤية التقدم حتى للنصوص الطويلة.*

## Performance Considerations

### Network Efficiency
Streaming reduces perceived latency but doesn't necessarily reduce total response time. The first token arrives faster, but network overhead for multiple small chunks can slightly increase total bandwidth usage compared to a single large response.

*يقلل البث التدفقي زمن الانتظار المتصور لكنه لا يقلل بالضرورة إجمالي وقت الاستجابة. يصل الرمز المميز الأول بشكل أسرع، لكن حمل الشبكة لعدة أجزاء صغيرة يمكن أن يزيد قليلاً من استخدام النطاق الترددي الإجمالي مقارنة باستجابة واحدة كبيرة.*

### Processing Overhead
Streaming requires continuous connection management and chunk processing. For applications with many concurrent streams, this can increase server load. However, the user experience benefits usually outweigh this overhead.

*يتطلب البث التدفقي إدارة اتصال مستمرة ومعالجة أجزاء. للتطبيقات مع العديد من التدفقات المتزامنة، يمكن أن يزيد هذا من حمل الخادم. ومع ذلك، عادة ما تفوق فوائد تجربة المستخدم هذا الحمل.*

### Buffer Management
Proper buffer management is crucial for streaming. Small buffers can cause choppy output, while large buffers delay initial response. Balance buffer size based on your use case and network conditions.

*إدارة المخزن المؤقت الصحيحة ضرورية للبث التدفقي. المخازن المؤقتة الصغيرة يمكن أن تسبب إخراجاً متقطعاً، بينما المخازن المؤقتة الكبيرة تؤخر الاستجابة الأولية. وازن حجم المخزن المؤقت بناءً على حالة الاستخدام وظروف الشبكة.*

### Error Recovery
Streaming requires robust error handling since errors can occur mid-stream. Implement retry logic and graceful degradation to handle network interruptions or API errors during streaming.

*يتطلب البث التدفقي معالجة أخطاء قوية لأن الأخطاء يمكن أن تحدث في منتصف التدفق. نفذ منطق إعادة المحاولة والتدهور السلس للتعامل مع انقطاعات الشبكة أو أخطاء API أثناء البث التدفقي.*

## Cost Implications

### Token Costs
Streaming doesn't change token costs—you pay for the same number of tokens whether streaming or not. However, streaming may allow you to cancel early if you detect the response isn't what you need, potentially saving tokens.

*البث التدفقي لا يغير تكاليف الرموز المميزة—تدفع مقابل نفس عدد الرموز المميزة سواء كان البث التدفقي أم لا. ومع ذلك، قد يسمح البث التدفقي بالإلغاء المبكر إذا اكتشفت أن الاستجابة ليست ما تحتاجه، مما قد يوفر الرموز المميزة.*

### Infrastructure Costs
Streaming requires maintaining persistent connections, which can increase infrastructure costs slightly compared to request-response patterns. However, this is usually minimal and offset by improved user experience.

*يتطلب البث التدفقي الحفاظ على اتصالات مستمرة، مما يمكن أن يزيد تكاليف البنية التحتية قليلاً مقارنة بأنماط الطلب-الاستجابة. ومع ذلك، هذا عادة ما يكون ضئيلاً ويعوضه تحسين تجربة المستخدم.*

### Early Cancellation Savings
If you can detect unwanted responses early through streaming, you can cancel the request and save tokens. This is particularly valuable for expensive models where early cancellation can significantly reduce costs.

*إذا تمكنت من اكتشاف الاستجابات غير المرغوب فيها مبكراً من خلال البث التدفقي، يمكنك إلغاء الطلب وتوفير الرموز المميزة. هذا مفيد بشكل خاص للنماذج باهظة الثمن حيث يمكن أن يقلل الإلغاء المبكر التكاليف بشكل كبير.*

## Best Practices

### Enable Streaming for User-Facing Applications
Always enable streaming for chat applications, customer support bots, and any user-facing interface where immediate feedback improves experience. The user experience benefits are significant.

*قم دائماً بتمكين البث التدفقي لتطبيقات الدردشة وروبوتات دعم العملاء وأي واجهة موجهة للمستخدم حيث تحسن التغذية الراجعة الفورية التجربة. فوائد تجربة المستخدم كبيرة.*

### Handle Stream Chunks Properly
Process stream chunks incrementally and display them to users immediately. Don't wait for complete responses before showing content. Handle empty chunks and partial content gracefully.

*قم بمعالجة أجزاء التدفق تدريجياً وعرضها للمستخدمين فوراً. لا تنتظر الاستجابات الكاملة قبل عرض المحتوى. تعامل مع الأجزاء الفارغة والمحتوى الجزئي بشكل سلس.*

### Implement Proper Error Handling
Handle network errors, API errors, and stream interruptions gracefully. Provide user feedback when streams fail and implement retry logic where appropriate.

*تعامل مع أخطاء الشبكة وأخطاء API وانقطاعات التدفق بشكل سلس. وفر ردود فعل للمستخدم عند فشل التدفقات ونفذ منطق إعادة المحاولة حيثما كان ذلك مناسباً.*

### Use Appropriate Buffer Sizes
Choose buffer sizes that balance smooth output with low latency. Too small buffers cause choppy output, while too large buffers delay initial response. Test with your specific use case.

*اختر أحجام المخزن المؤقت التي توازن بين الإخراج السلس وزمن الانتظار المنخفض. المخازن المؤقتة الصغيرة جداً تسبب إخراجاً متقطعاً، بينما المخازن المؤقتة الكبيرة جداً تؤخر الاستجابة الأولية. اختبر مع حالة الاستخدام المحددة.*

### Monitor Stream Performance
Track metrics like time-to-first-token, stream completion rates, and error rates. Use this data to optimize streaming performance and identify issues early.

*تتبع مقاييس مثل وقت الوصول للرمز المميز الأول، ومعدلات اكتمال التدفق، ومعدلات الأخطاء. استخدم هذه البيانات لتحسين أداء البث التدفقي وتحديد المشاكل مبكراً.*

## When NOT to Use

### Batch Processing Scenarios
For batch processing where you need complete responses before processing, streaming adds unnecessary complexity. Use standard request-response patterns for batch operations.

*لمعالجة الدفعات حيث تحتاج إلى استجابات كاملة قبل المعالجة، يضيف البث التدفقي تعقيداً غير ضروري. استخدم أنماط الطلب-الاستجابة القياسية لعمليات الدفعات.*

### When Complete Response is Required
If your application logic requires the complete response before proceeding, streaming doesn't provide benefits. Use standard requests in these cases.

*إذا كانت منطق تطبيقك يتطلب الاستجابة الكاملة قبل المتابعة، لا يوفر البث التدفقي فوائد. استخدم الطلبات القياسية في هذه الحالات.*

### High-Latency Networks
On very high-latency networks, streaming may not provide noticeable benefits since chunks arrive slowly anyway. However, even in these cases, streaming usually improves perceived performance.

*على الشبكات عالية زمن الانتظار جداً، قد لا يوفر البث التدفقي فوائد ملحوظة لأن الأجزاء تصل ببطء على أي حال. ومع ذلك، حتى في هذه الحالات، عادة ما يحسن البث التدفقي الأداء المتصور.*

### Simple One-Shot Queries
For simple, one-shot queries where users submit and wait, streaming may not be necessary. However, it still improves perceived performance, so consider enabling it anyway.

*للاستفسارات البسيطة لمرة واحدة حيث يقدم المستخدمون وينتظرون، قد لا يكون البث التدفقي ضرورياً. ومع ذلك، لا يزال يحسن الأداء المتصور، لذا فكر في تمكينه على أي حال.*

## Troubleshooting

### Choppy or Delayed Streaming
If streaming feels choppy or delayed, check your buffer size and network conditions. Increase buffer size slightly, but not too much to avoid delaying initial response. Check for network latency issues.

*إذا كان البث التدفقي يبدو متقطعاً أو متأخراً، تحقق من حجم المخزن المؤقت وظروف الشبكة. قم بزيادة حجم المخزن المؤقت قليلاً، لكن ليس كثيراً لتجنب تأخير الاستجابة الأولية. تحقق من مشاكل زمن الانتظار في الشبكة.*

### Stream Interruptions
If streams frequently interrupt, check network stability and API reliability. Implement retry logic and handle reconnection. Monitor error rates to identify patterns.

*إذا انقطعت التدفقات بشكل متكرر، تحقق من استقرار الشبكة وموثوقية API. نفذ منطق إعادة المحاولة والتعامل مع إعادة الاتصال. راقب معدلات الأخطاء لتحديد الأنماط.*

### High Memory Usage
If streaming causes high memory usage, ensure you're processing chunks incrementally and not buffering entire responses. Release resources promptly after streams complete.

*إذا تسبب البث التدفقي في استخدام ذاكرة عالي، تأكد من معالجة الأجزاء تدريجياً وعدم تخزين الاستجابات الكاملة مؤقتاً. حرر الموارد فوراً بعد اكتمال التدفقات.*

### Incomplete Responses
If streams end prematurely, check for API errors or network issues. Implement proper error handling and retry logic. Verify that the stream wasn't cancelled unintentionally.

*إذا انتهت التدفقات قبل الأوان، تحقق من أخطاء API أو مشاكل الشبكة. نفذ معالجة أخطاء مناسبة ومنطق إعادة المحاولة. تحقق من أن التدفق لم يتم إلغاؤه عن غير قصد.*

## Basic Usage

### Enable Streaming

*تمكين البث التدفقي*

```python
from app.builders import ChatRequestBuilder
from app.services import OpenRouterClient

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Tell me a story")
    .with_streaming(True)
    .build())

client = OpenRouterClient()
async for chunk in client.stream_chat_completion(request):
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

### Using API Endpoint

*استخدام نقطة نهاية API*

```bash
curl -X POST "http://localhost:8000/api/v1/chat/completions/stream" \
  -H "Authorization: Bearer your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-4o",
    "messages": [{"role": "user", "content": "Hello!"}],
    "stream": true
  }'
```

### Processing Stream Chunks

*معالجة أجزاء التدفق*

```python
from app.processors import StreamProcessor

async for chunk in client.stream_chat_completion(request):
    processed = await StreamProcessor.process_stream_chunk(chunk)
    print(processed["content"], end="", flush=True)
```

## Advanced Examples

### Streaming with Error Handling

*البث التدفقي مع معالجة الأخطاء*

```python
from app.builders import ChatRequestBuilder
from app.services import OpenRouterClient

async def stream_with_error_handling(request):
    client = OpenRouterClient()
    try:
        async for chunk in client.stream_chat_completion(request):
            if chunk.choices:
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    yield delta.content
            elif chunk.error:
                raise Exception(f"Stream error: {chunk.error}")
    except Exception as e:
        print(f"Stream interrupted: {e}")
        # Implement retry or fallback logic
        raise

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Generate a long story")
    .with_streaming(True)
    .build())

async for content in stream_with_error_handling(request):
    print(content, end="", flush=True)
```

### Streaming with Early Cancellation

*البث التدفقي مع الإلغاء المبكر*

```python
async def stream_with_cancellation(request, max_tokens=100):
    client = OpenRouterClient()
    token_count = 0
    
    async for chunk in client.stream_chat_completion(request):
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            token_count += len(content.split())
            
            if token_count > max_tokens:
                # Cancel stream if too long
                print("\n[Stream cancelled: too long]")
                break
            
            print(content, end="", flush=True)

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Explain quantum computing")
    .with_streaming(True)
    .build())

await stream_with_cancellation(request, max_tokens=50)
```

### Streaming with Progress Tracking

*البث التدفقي مع تتبع التقدم*

```python
async def stream_with_progress(request):
    client = OpenRouterClient()
    full_response = ""
    chunk_count = 0
    
    async for chunk in client.stream_chat_completion(request):
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            full_response += content
            chunk_count += 1
            
            # Show progress every 10 chunks
            if chunk_count % 10 == 0:
                print(f"\n[Progress: {len(full_response)} characters, {chunk_count} chunks]", end="\r")
            
            print(content, end="", flush=True)
    
    print(f"\n[Complete: {len(full_response)} characters total]")
    return full_response

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Write a comprehensive guide")
    .with_streaming(True)
    .build())

response = await stream_with_progress(request)
```
