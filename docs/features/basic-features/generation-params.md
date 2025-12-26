# Generation Parameters

## Feature Overview

Generation parameters give you fine-grained control over how AI models generate responses. These parameters allow you to adjust creativity, determinism, length, and other aspects of output to match your specific needs. Understanding and properly configuring these parameters is essential for achieving the desired output quality and behavior.

*معاملات التوليد تمنحك تحكماً دقيقاً في كيفية توليد نماذج الذكاء الاصطناعي للاستجابات. تسمح لك هذه المعاملات بتعديل الإبداع والحتمية والطول وجوانب أخرى من الإخراج لتطابق احتياجاتك المحددة. فهم وتكوين هذه المعاملات بشكل صحيح ضروري لتحقيق جودة وسلوك الإخراج المطلوب.*

## Feature Importance

Generation parameters are the primary way to control AI behavior without changing prompts. They allow you to fine-tune responses for different use cases—from creative writing that needs high randomness to code generation that requires determinism. Proper parameter configuration can mean the difference between useful and unusable outputs.

*معاملات التوليد هي الطريقة الأساسية للتحكم في سلوك الذكاء الاصطناعي دون تغيير المطالب. تسمح لك بضبط الاستجابات لحالات استخدام مختلفة—من الكتابة الإبداعية التي تحتاج عشوائية عالية إلى توليد الكود الذي يتطلب الحتمية. التكوين الصحيح للمعاملات يمكن أن يعني الفرق بين المخرجات المفيدة وغير القابلة للاستخدام.*

## Key Benefits

### Output Quality Control
Generation parameters let you control the quality and characteristics of AI outputs. Temperature controls creativity, top_p controls diversity, and max_tokens controls length—allowing you to fine-tune responses for your specific needs.

*معاملات التوليد تسمح لك بالتحكم في جودة وخصائص مخرجات الذكاء الاصطناعي. درجة الحرارة تتحكم في الإبداع، top_p تتحكم في التنوع، وmax_tokens تتحكم في الطول—مما يسمح لك بضبط الاستجابات لاحتياجاتك المحددة.*

### Deterministic vs Creative Outputs
You can configure parameters to produce deterministic, reproducible outputs for code generation or testing, or creative, varied outputs for content creation. This flexibility is crucial for different application types.

*يمكنك تكوين المعاملات لإنتاج مخرجات حتمية وقابلة للتكرار لتوليد الكود أو الاختبار، أو مخرجات إبداعية ومتنوعة لإنشاء المحتوى. هذه المرونة ضرورية لأنواع التطبيقات المختلفة.*

### Cost Optimization
By setting appropriate max_tokens limits, you can control response length and costs. Stop sequences allow early termination when certain conditions are met, saving tokens and reducing costs.

*عن طريق تعيين حدود max_tokens المناسبة، يمكنك التحكم في طول الاستجابة والتكاليف. تسلسلات الإيقاف تسمح بالإنهاء المبكر عند استيفاء شروط معينة، مما يوفر الرموز المميزة ويقلل التكاليف.*

### Reproducibility
Seed parameter enables reproducible outputs, which is essential for testing, debugging, and ensuring consistent behavior across runs. This is particularly valuable for development and quality assurance.

*معامل Seed يتيح مخرجات قابلة للتكرار، وهو ضروري للاختبار والتشخيص وضمان سلوك متسق عبر التشغيلات. هذا مفيد بشكل خاص للتطوير وضمان الجودة.*

### Repetition Control
Frequency and presence penalties help control repetition and encourage topic diversity. This is crucial for generating varied content and avoiding repetitive or stuck outputs.

*عقوبات التكرار والحضور تساعد في التحكم في التكرار وتشجع تنوع المواضيع. هذا ضروري لتوليد محتوى متنوع وتجنب المخرجات المتكررة أو العالقة.*

## Use Cases

### Code Generation
Use low temperature (0.0-0.3) and seed for deterministic, reproducible code. Set appropriate max_tokens to control code length. Use stop sequences to end generation at specific points (e.g., end of function).

*استخدم درجة حرارة منخفضة (0.0-0.3) وseed لكود حتمي وقابل للتكرار. قم بتعيين max_tokens المناسب للتحكم في طول الكود. استخدم تسلسلات الإيقاف لإنهاء التوليد عند نقاط محددة (مثل نهاية الدالة).*

### Creative Writing
Use higher temperature (0.7-1.2) for creative, varied outputs. Combine with top_p (0.9-0.95) for diverse vocabulary. Use frequency penalties to avoid repetitive phrases.

*استخدم درجة حرارة أعلى (0.7-1.2) لمخرجات إبداعية ومتنوعة. اجمع مع top_p (0.9-0.95) لمفردات متنوعة. استخدم عقوبات التكرار لتجنب العبارات المتكررة.*

### Data Extraction
Use low temperature (0.0-0.2) for consistent, accurate extraction. Set max_tokens based on expected output size. Use structured outputs with appropriate parameters for reliable results.

*استخدم درجة حرارة منخفضة (0.0-0.2) للاستخراج المتسق والدقيق. قم بتعيين max_tokens بناءً على حجم الإخراج المتوقع. استخدم المخرجات المنظمة مع المعاملات المناسبة لنتائج موثوقة.*

### Conversational AI
Use moderate temperature (0.7-0.9) for natural, varied conversations. Use presence penalty to encourage topic diversity. Set max_tokens to control response length and maintain natural conversation flow.

*استخدم درجة حرارة معتدلة (0.7-0.9) للمحادثات الطبيعية والمتنوعة. استخدم عقوبة الحضور لتشجيع تنوع المواضيع. قم بتعيين max_tokens للتحكم في طول الاستجابة والحفاظ على تدفق المحادثة الطبيعي.*

### Testing and Debugging
Use seed for reproducible outputs during testing. Use low temperature for consistent test results. Set stop sequences to control output length precisely.

*استخدم seed لمخرجات قابلة للتكرار أثناء الاختبار. استخدم درجة حرارة منخفضة لنتائج اختبار متسقة. قم بتعيين تسلسلات الإيقاف للتحكم في طول الإخراج بدقة.*

## Performance Considerations

### Temperature Impact on Speed
Temperature doesn't significantly affect generation speed, but lower temperatures may produce more predictable outputs faster since the model has fewer choices to consider. Higher temperatures require more computation for diverse sampling.

*درجة الحرارة لا تؤثر بشكل كبير على سرعة التوليد، لكن درجات الحرارة المنخفضة قد تنتج مخرجات أكثر قابلية للتنبؤ بشكل أسرع لأن النموذج لديه خيارات أقل للنظر فيها. درجات الحرارة الأعلى تتطلب المزيد من الحساب للعينة المتنوعة.*

### Max Tokens and Response Time
Larger max_tokens values allow longer responses but increase generation time linearly. Set max_tokens based on actual needs—don't set unnecessarily high values that waste time and tokens.

*قيم max_tokens الأكبر تسمح باستجابات أطول لكنها تزيد وقت التوليد خطياً. قم بتعيين max_tokens بناءً على الاحتياجات الفعلية—لا تقم بتعيين قيم عالية بشكل غير ضروري تهدر الوقت والرموز المميزة.*

### Stop Sequences Efficiency
Stop sequences can terminate generation early, saving tokens and time. However, the model must process tokens until it encounters the stop sequence, so choose stop sequences that appear early in desired outputs.

*تسلسلات الإيقاف يمكن أن تنهي التوليد مبكراً، مما يوفر الرموز المميزة والوقت. ومع ذلك، يجب على النموذج معالجة الرموز المميزة حتى يواجه تسلسل الإيقاف، لذا اختر تسلسلات الإيقاف التي تظهر مبكراً في المخرجات المطلوبة.*

### Seed and Caching
Using seed with the same prompt enables caching benefits since the output is deterministic. This can improve performance and reduce costs for repeated queries.

*استخدام seed مع نفس المطلب يتيح فوائد التخزين المؤقت لأن الإخراج حتمي. هذا يمكن أن يحسن الأداء ويقلل التكاليف للاستفسارات المتكررة.*

## Cost Implications

### Max Tokens and Cost
Max tokens directly controls the maximum number of tokens in the response, directly affecting cost. Set max_tokens based on actual needs—setting it too high wastes tokens and money, while setting it too low may truncate important responses.

*Max tokens يتحكم مباشرة في الحد الأقصى لعدد الرموز المميزة في الاستجابة، مما يؤثر مباشرة على التكلفة. قم بتعيين max_tokens بناءً على الاحتياجات الفعلية—تعيينه عالياً جداً يهدر الرموز المميزة والمال، بينما تعيينه منخفضاً جداً قد يقطع الاستجابات المهمة.*

### Stop Sequences Savings
Stop sequences can significantly reduce costs by terminating generation early when certain conditions are met. For example, stopping at "END" or "STOP" can save hundreds of tokens in long responses.

*تسلسلات الإيقاف يمكن أن تقلل التكاليف بشكل كبير عن طريق إنهاء التوليد مبكراً عند استيفاء شروط معينة. على سبيل المثال، الإيقاف عند "END" أو "STOP" يمكن أن يوفر مئات الرموز المميزة في الاستجابات الطويلة.*

### Temperature and Retry Costs
Higher temperature may produce less desirable outputs, requiring retries and increasing costs. Lower temperature produces more consistent results, reducing the need for retries and saving costs.

*درجة الحرارة الأعلى قد تنتج مخرجات أقل مرغوبية، مما يتطلب إعادة المحاولة ويزيد التكاليف. درجة الحرارة المنخفضة تنتج نتائج أكثر اتساقاً، مما يقلل الحاجة لإعادة المحاولة ويوفر التكاليف.*

### Seed and Caching Benefits
Using seed enables deterministic outputs, which can be cached by providers. This reduces costs for repeated queries with the same prompt and seed combination.

*استخدام seed يتيح مخرجات حتمية، والتي يمكن تخزينها مؤقتاً من قبل المزودين. هذا يقلل التكاليف للاستفسارات المتكررة مع نفس مزيج المطلب وseed.*

## Best Practices

### Temperature Selection
Choose temperature based on your use case: 0.0-0.3 for deterministic outputs (code, data extraction), 0.7-0.9 for balanced outputs (conversations), 0.9-1.5 for creative outputs (writing, brainstorming). Avoid extremes unless necessary.

*اختر درجة الحرارة بناءً على حالة الاستخدام: 0.0-0.3 للمخرجات الحتمية (الكود، استخراج البيانات)، 0.7-0.9 للمخرجات المتوازنة (المحادثات)، 0.9-1.5 للمخرجات الإبداعية (الكتابة، العصف الذهني). تجنب التطرف ما لم يكن ضرورياً.*

### Max Tokens Configuration
Set max_tokens based on expected output length, not maximum possible length. Add a buffer (10-20%) for safety, but don't set unnecessarily high values. Monitor actual token usage to optimize.

*قم بتعيين max_tokens بناءً على طول الإخراج المتوقع، وليس الحد الأقصى للطول الممكن. أضف مخزن مؤقت (10-20%) للأمان، لكن لا تقم بتعيين قيم عالية بشكل غير ضروري. راقب استخدام الرموز المميزة الفعلية للتحسين.*

### Stop Sequences Usage
Use stop sequences for structured outputs where you know the termination condition. Choose sequences that are unlikely to appear in normal output but clearly indicate completion. Test stop sequences to ensure they work as expected.

*استخدم تسلسلات الإيقاف للمخرجات المنظمة حيث تعرف شرط الإنهاء. اختر تسلسلات غير محتملة أن تظهر في الإخراج العادي لكنها تشير بوضوح إلى الاكتمال. اختبر تسلسلات الإيقاف للتأكد من أنها تعمل كما هو متوقع.*

### Seed for Reproducibility
Use seed when you need reproducible outputs for testing, debugging, or consistent behavior. Don't use seed for creative or varied outputs where you want different results each time.

*استخدم seed عندما تحتاج مخرجات قابلة للتكرار للاختبار أو التشخيص أو السلوك المتسق. لا تستخدم seed للمخرجات الإبداعية أو المتنوعة حيث تريد نتائج مختلفة في كل مرة.*

### Penalty Configuration
Use frequency penalty (0.1-0.5) to reduce repetition of words or phrases. Use presence penalty (0.1-0.4) to encourage topic diversity. Start with low values and increase if needed.

*استخدم عقوبة التكرار (0.1-0.5) لتقليل تكرار الكلمات أو العبارات. استخدم عقوبة الحضور (0.1-0.4) لتشجيع تنوع المواضيع. ابدأ بقيم منخفضة وزدها إذا لزم الأمر.*

## When NOT to Use

### Don't Use High Temperature for Critical Tasks
Avoid high temperature (above 1.0) for tasks requiring accuracy and consistency, such as code generation, data extraction, or factual responses. High temperature increases randomness and reduces reliability.

*تجنب درجة الحرارة العالية (أعلى من 1.0) للمهام التي تتطلب الدقة والاتساق، مثل توليد الكود أو استخراج البيانات أو الاستجابات الواقعية. درجة الحرارة العالية تزيد العشوائية وتقلل الموثوقية.*

### Don't Set Max Tokens Too High
Avoid setting max_tokens unnecessarily high. This wastes tokens and money. Set it based on actual needs and monitor usage to optimize. Only increase if you're consistently hitting the limit.

*تجنب تعيين max_tokens عالياً بشكل غير ضروري. هذا يهدر الرموز المميزة والمال. قم بتعيينه بناءً على الاحتياجات الفعلية وراقب الاستخدام للتحسين. قم بزيادته فقط إذا كنت تصل باستمرار إلى الحد.*

### Don't Overuse Stop Sequences
Don't use stop sequences for every request—only when you have a clear termination condition. Overusing stop sequences can interfere with natural output generation.

*لا تستخدم تسلسلات الإيقاف لكل طلب—فقط عندما يكون لديك شرط إنهاء واضح. الإفراط في استخدام تسلسلات الإيقاف يمكن أن يتداخل مع توليد الإخراج الطبيعي.*

### Don't Use Seed for Varied Outputs
Don't use seed when you want varied, creative outputs. Seed makes outputs deterministic, which defeats the purpose of creative generation. Reserve seed for testing and reproducibility needs.

*لا تستخدم seed عندما تريد مخرجات متنوعة وإبداعية. Seed يجعل المخرجات حتمية، مما يهزم الغرض من التوليد الإبداعي. احتفظ بـ seed لاحتياجات الاختبار والقابلية للتكرار.*

## Troubleshooting

### Outputs Too Random or Inconsistent
If outputs are too random, reduce temperature (try 0.3-0.7). If outputs are too repetitive, increase temperature slightly or adjust frequency/presence penalties. Test different values to find the right balance.

*إذا كانت المخرجات عشوائية جداً، قلل درجة الحرارة (جرب 0.3-0.7). إذا كانت المخرجات متكررة جداً، زد درجة الحرارة قليلاً أو اضبط عقوبات التكرار/الحضور. اختبر قيم مختلفة للعثور على التوازن الصحيح.*

### Responses Getting Cut Off
If responses are getting truncated, increase max_tokens. However, first check if you're actually hitting the limit or if stop sequences are triggering prematurely. Monitor token usage to optimize max_tokens.

*إذا كانت الاستجابات تُقطع، قم بزيادة max_tokens. ومع ذلك، تحقق أولاً مما إذا كنت تصل فعلياً إلى الحد أو إذا كانت تسلسلات الإيقاف تبدأ قبل الأوان. راقب استخدام الرموز المميزة لتحسين max_tokens.*

### Stop Sequences Not Working
If stop sequences aren't working, verify they're correctly formatted and unlikely to appear in normal output. Some models may not respect stop sequences in certain contexts. Test with simple examples first.

*إذا لم تعمل تسلسلات الإيقاف، تحقق من أنها منسقة بشكل صحيح وغير محتملة أن تظهر في الإخراج العادي. بعض النماذج قد لا تحترم تسلسلات الإيقاف في سياقات معينة. اختبر مع أمثلة بسيطة أولاً.*

### Seed Not Producing Reproducible Results
If seed isn't producing reproducible results, ensure you're using the same prompt, model, and all parameters. Some models may have slight variations even with seed. Verify seed support for your chosen model.

*إذا كان seed لا ينتج نتائج قابلة للتكرار، تأكد من أنك تستخدم نفس المطلب والنموذج وجميع المعاملات. بعض النماذج قد يكون لها اختلافات طفيفة حتى مع seed. تحقق من دعم seed للنموذج المختار.*

## Basic Usage

### Temperature

*درجة الحرارة*

Controls randomness in responses (0.0 to 2.0).

*تتحكم في العشوائية في الاستجابات (0.0 إلى 2.0).*

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Write a story")
    .with_temperature(0.7)
    .build())
```

- Lower values (0.0-0.5): More focused and deterministic
  *القيم المنخفضة (0.0-0.5): أكثر تركيزاً وحتمية*
- Higher values (0.7-2.0): More creative and random
  *القيم الأعلى (0.7-2.0): أكثر إبداعاً وعشوائية*

### Top P

*Top P*

Nucleus sampling parameter (0.0 to 1.0).

*معامل عينة النواة (0.0 إلى 1.0).*

```python
request = builder.with_top_p(0.9).build()
```

Controls diversity by considering only tokens with cumulative probability up to top_p.

*تتحكم في التنوع من خلال النظر فقط في الرموز المميزة مع الاحتمال التراكمي حتى top_p.*

### Max Tokens

*Max Tokens*

Maximum tokens in the response.

*الحد الأقصى للرموز المميزة في الاستجابة.*

```python
request = builder.with_max_tokens(500).build()
```

### Stop Sequences

*تسلسلات الإيقاف*

Stop generation when encountering these sequences.

*إيقاف التوليد عند مواجهة هذه التسلسلات.*

```python
request = builder.with_stop(["END", "STOP"]).build()
```

Or single stop sequence:

*أو تسلسل إيقاف واحد:*

```python
request = builder.with_stop("END").build()
```

### Seed

*Seed*

Set seed for reproducible outputs.

*تعيين seed للمخرجات القابلة للتكرار.*

```python
request = builder.with_seed(42).build()
```

### Frequency and Presence Penalty

*عقوبات التكرار والحضور*

Control repetition and topic diversity.

*التحكم في التكرار وتنوع المواضيع.*

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Write about AI")
    .with_frequency_penalty(0.5)
    .with_presence_penalty(0.3)
    .build())
```

## Advanced Examples

### Code Generation with Deterministic Parameters

*توليد الكود مع معاملات حتمية*

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Write a Python function to calculate factorial")
    .with_temperature(0.0)  # Deterministic
    .with_max_tokens(200)
    .with_stop(["def ", "class "])  # Stop at next function/class
    .with_seed(42)  # Reproducible
    .build())
```

### Creative Writing with High Variability

*الكتابة الإبداعية مع تنوع عالي*

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Write a creative short story")
    .with_temperature(1.2)  # High creativity
    .with_top_p(0.95)  # Diverse vocabulary
    .with_frequency_penalty(0.6)  # Avoid repetition
    .with_presence_penalty(0.4)  # Encourage diversity
    .with_max_tokens(1000)
    .build())
```

### Data Extraction with Controlled Output

*استخراج البيانات مع إخراج محكم*

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Extract: Name, Age, Email from: John, 30, john@example.com")
    .with_temperature(0.1)  # Very deterministic
    .with_max_tokens(100)
    .with_stop(["---"])  # Stop at separator
    .build())
```

### Conversation with Balanced Parameters

*محادثة مع معاملات متوازنة*

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Explain quantum computing")
    .with_temperature(0.8)  # Balanced
    .with_top_p(0.9)
    .with_max_tokens(500)
    .with_frequency_penalty(0.2)  # Light repetition control
    .build())
```
