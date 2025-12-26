# Messages

## Feature Overview

Messages are the fundamental building blocks of AI conversations. This feature allows you to structure conversations with different roles (user, assistant, system), combine text with multimodal content, and create rich, context-aware interactions that guide the AI's behavior and responses.

*الرسائل هي اللبنات الأساسية للمحادثات مع الذكاء الاصطناعي. تتيح لك هذه الميزة هيكلة المحادثات بأدوار مختلفة (مستخدم، مساعد، نظام)، ودمج النص مع المحتوى متعدد الوسائط، وإنشاء تفاعلات غنية وواعية بالسياق توجه سلوك واستجابات الذكاء الاصطناعي.*

## Feature Importance

Messages form the core of every AI interaction. Without proper message structure, the AI cannot understand context, maintain conversation flow, or follow instructions effectively. Well-structured messages enable the AI to provide accurate, relevant, and contextually appropriate responses.

*تشكل الرسائل جوهر كل تفاعل مع الذكاء الاصطناعي. بدون هيكل رسائل صحيح، لا يمكن للذكاء الاصطناعي فهم السياق، أو الحفاظ على تدفق المحادثة، أو اتباع التعليمات بفعالية. الرسائل ذات الهيكل الجيد تمكن الذكاء الاصطناعي من تقديم استجابات دقيقة وذات صلة ومناسبة سياقياً.*

## Key Benefits

### Context Preservation
Messages maintain conversation history, allowing the AI to remember previous exchanges and build upon them. This creates natural, flowing conversations where context accumulates over multiple turns.

*تحافظ الرسائل على تاريخ المحادثة، مما يسمح للذكاء الاصطناعي بتذكر التبادلات السابقة والبناء عليها. هذا يخلق محادثات طبيعية وتدفقية حيث يتراكم السياق عبر عدة جولات.*

### Role-Based Control
Different message roles (system, user, assistant) give you precise control over the AI's behavior. System prompts set the AI's personality and instructions, user messages provide queries, and assistant messages maintain conversation context.

*الأدوار المختلفة للرسائل (نظام، مستخدم، مساعد) تمنحك تحكماً دقيقاً في سلوك الذكاء الاصطناعي. مطالب النظام تحدد شخصية وتعليمات الذكاء الاصطناعي، ورسائل المستخدم توفر الاستفسارات، ورسائل المساعد تحافظ على سياق المحادثة.*

### Multimodal Capabilities
Messages can combine text with images, videos, audio, and files, enabling rich interactions where the AI can see, hear, and analyze various content types in a single conversation.

*يمكن للرسائل دمج النص مع الصور والفيديو والصوت والملفات، مما يتيح تفاعلات غنية حيث يمكن للذكاء الاصطناعي رؤية وسماع وتحليل أنواع محتوى مختلفة في محادثة واحدة.*

### Instruction Precision
System prompts allow you to define the AI's role, constraints, output format, and behavior patterns with precision, ensuring consistent and predictable responses across all interactions.

*تسمح مطالب النظام بتحديد دور الذكاء الاصطناعي، والقيود، وتنسيق الإخراج، وأنماط السلوك بدقة، مما يضمن استجابات متسقة وقابلة للتنبؤ عبر جميع التفاعلات.*

## Use Cases

### Customer Support Chatbots
Use system prompts to define the chatbot's personality and knowledge base, user messages for customer queries, and assistant messages to maintain conversation context across multiple interactions.

*استخدم مطالب النظام لتحديد شخصية قاعدة المعرفة للروبوت، ورسائل المستخدم لاستفسارات العملاء، ورسائل المساعد للحفاظ على سياق المحادثة عبر تفاعلات متعددة.*

### Content Analysis Applications
Combine system prompts with multimodal messages to analyze documents, images, or videos. The system prompt defines analysis criteria, while multimodal content provides the material to analyze.

*اجمع مطالب النظام مع الرسائل متعددة الوسائط لتحليل المستندات أو الصور أو الفيديو. يحدد مطلب النظام معايير التحليل، بينما يوفر المحتوى متعدد الوسائط المادة للتحليل.*

### Educational Tutoring Systems
Use system prompts to define the tutor's teaching style and expertise level, user messages for student questions, and assistant messages to maintain learning context throughout the session.

*استخدم مطالب النظام لتحديد أسلوب التدريس ومستوى الخبرة للمعلم، ورسائل المستخدم لأسئلة الطلاب، ورسائل المساعد للحفاظ على سياق التعلم طوال الجلسة.*

### Code Generation and Review
System prompts can define coding standards and best practices, while user messages provide requirements. Assistant messages maintain code context across multiple iterations.

*يمكن لمطالب النظام تحديد معايير الترميز وأفضل الممارسات، بينما توفر رسائل المستخدم المتطلبات. تحافظ رسائل المساعد على سياق الكود عبر عدة تكرارات.*

### Multimodal Content Creation
Combine text instructions with images, videos, or audio in messages to create content that references and analyzes visual or audio elements, enabling rich creative workflows.

*اجمع تعليمات النص مع الصور أو الفيديو أو الصوت في الرسائل لإنشاء محتوى يشير إلى العناصر المرئية أو الصوتية ويحللها، مما يتيح سير عمل إبداعي غني.*

## Performance Considerations

### Message Length Impact
Longer messages consume more tokens, increasing cost and processing time. Keep messages concise while maintaining necessary context. System prompts are typically cached, so longer system prompts have minimal impact on subsequent requests.

*الرسائل الأطول تستهلك المزيد من الرموز المميزة، مما يزيد التكلفة ووقت المعالجة. حافظ على الرسائل موجزة مع الحفاظ على السياق الضروري. عادة ما يتم تخزين مطالب النظام مؤقتاً، لذا فإن مطالب النظام الأطول لها تأثير ضئيل على الطلبات اللاحقة.*

### Context Window Management
Each message consumes context window space. For long conversations, consider using message transforms (middle-out compression) to reduce context size while preserving important information.

*كل رسالة تستهلك مساحة نافذة السياق. للمحادثات الطويلة، فكر في استخدام تحويلات الرسائل (الضغط من الوسط) لتقليل حجم السياق مع الحفاظ على المعلومات المهمة.*

### Multimodal Processing Overhead
Messages with images, videos, or audio require additional processing time. Large media files increase latency and token consumption. Optimize media size and resolution based on your needs.

*الرسائل التي تحتوي على صور أو فيديو أو صوت تتطلب وقت معالجة إضافي. الملفات الإعلامية الكبيرة تزيد زمن الانتظار واستهلاك الرموز المميزة. قم بتحسين حجم وضوح الوسائط بناءً على احتياجاتك.*

### System Prompt Efficiency
System prompts are often cached by providers, making them cost-effective for repeated use. Design comprehensive system prompts that don't need frequent changes to maximize caching benefits.

*غالباً ما يتم تخزين مطالب النظام مؤقتاً من قبل المزودين، مما يجعلها فعالة من حيث التكلفة للاستخدام المتكرر. صمم مطالب نظام شاملة لا تحتاج إلى تغييرات متكررة لتعظيم فوائد التخزين المؤقت.*

## Cost Implications

### Token Consumption
Each message token costs money. Longer messages, especially with multimodal content, consume more tokens. System prompts are typically cached, reducing costs for repeated interactions.

*كل رمز مميز في الرسالة يكلف المال. الرسائل الأطول، خاصة مع المحتوى متعدد الوسائط، تستهلك المزيد من الرموز المميزة. عادة ما يتم تخزين مطالب النظام مؤقتاً، مما يقلل التكاليف للتفاعلات المتكررة.*

### Multimodal Content Costs
Images, videos, and audio consume significantly more tokens than text. A single high-resolution image can consume thousands of tokens. Optimize media size and resolution to balance quality and cost.

*الصور والفيديو والصوت تستهلك رموزاً مميزة أكثر بكثير من النص. يمكن لصورة واحدة عالية الدقة أن تستهلك آلاف الرموز المميزة. قم بتحسين حجم وضوح الوسائط لتحقيق التوازن بين الجودة والتكلفة.*

### Context Window Costs
Long conversation histories consume more tokens. Use message compression or selective context retention to manage costs while maintaining conversation quality.

*تاريخ المحادثات الطويل يستهلك المزيد من الرموز المميزة. استخدم ضغط الرسائل أو الاحتفاظ الانتقائي بالسياق لإدارة التكاليف مع الحفاظ على جودة المحادثة.*

## Best Practices

### System Prompt Design
Create clear, specific system prompts that define the AI's role, constraints, and output format. Keep them focused and avoid unnecessary verbosity. Use system prompts for instructions that don't change frequently.

*أنشئ مطالب نظام واضحة ومحددة تحدد دور الذكاء الاصطناعي والقيود وتنسيق الإخراج. حافظ عليها مركزة وتجنب الإسهاب غير الضروري. استخدم مطالب النظام للتعليمات التي لا تتغير بشكل متكرر.*

### Message Role Usage
Use appropriate roles for each message type: system for instructions, user for queries, assistant for maintaining context. Don't mix roles unnecessarily, as this can confuse the AI.

*استخدم أدواراً مناسبة لكل نوع رسالة: النظام للتعليمات، المستخدم للاستفسارات، المساعد للحفاظ على السياق. لا تخلط الأدوار بشكل غير ضروري، لأن هذا يمكن أن يربك الذكاء الاصطناعي.*

### Context Management
Maintain conversation context by including relevant previous messages. However, don't include every message—select the most important ones that provide necessary context for the current query.

*حافظ على سياق المحادثة من خلال تضمين الرسائل السابقة ذات الصلة. ومع ذلك، لا تتضمن كل رسالة—اختر الأكثر أهمية التي توفر السياق الضروري للاستفسار الحالي.*

### Multimodal Optimization
When using images, videos, or audio, optimize file sizes and resolutions. Use appropriate detail levels (low/high/auto) for images based on your needs. Consider using URLs instead of base64 for large files.

*عند استخدام الصور أو الفيديو أو الصوت، قم بتحسين أحجام الملفات والدقة. استخدم مستويات التفاصيل المناسبة (منخفض/عالي/تلقائي) للصور بناءً على احتياجاتك. فكر في استخدام عناوين URL بدلاً من base64 للملفات الكبيرة.*

### Message Clarity
Write clear, unambiguous messages. Avoid overly complex instructions that might confuse the AI. Break complex requests into simpler, sequential messages if needed.

*اكتب رسائل واضحة وغير غامضة. تجنب التعليمات المعقدة للغاية التي قد تربك الذكاء الاصطناعي. قسّم الطلبات المعقدة إلى رسائل أبسط ومتسلسلة إذا لزم الأمر.*

## When NOT to Use

### Don't Overload System Prompts
Avoid putting too much information in system prompts. If instructions change frequently, consider using user messages instead. System prompts work best for stable, reusable instructions.

*تجنب وضع الكثير من المعلومات في مطالب النظام. إذا تغيرت التعليمات بشكل متكرر، فكر في استخدام رسائل المستخدم بدلاً من ذلك. تعمل مطالب النظام بشكل أفضل للتعليمات المستقرة والقابلة لإعادة الاستخدام.*

### Don't Include Unnecessary Context
Avoid including every previous message in the conversation. Only include messages that are directly relevant to the current query. Excessive context increases costs without adding value.

*تجنب تضمين كل رسالة سابقة في المحادثة. قم بتضمين الرسائل ذات الصلة المباشرة بالاستفسار الحالي فقط. السياق المفرط يزيد التكاليف دون إضافة قيمة.*

### Don't Mix Roles Inappropriately
Don't use assistant role for user queries or user role for system instructions. This confuses the AI and leads to poor responses. Stick to the intended purpose of each role.

*لا تستخدم دور المساعد لاستفسارات المستخدم أو دور المستخدم لتعليمات النظام. هذا يربك الذكاء الاصطناعي ويؤدي إلى استجابات ضعيفة. التزم بالغرض المقصود من كل دور.*

### Don't Use High-Resolution Media Unnecessarily
Avoid using high-resolution images or videos when lower resolution would suffice. High-resolution media significantly increases token consumption and costs without always improving results.

*تجنب استخدام الصور أو الفيديو عالية الدقة عندما تكون الدقة المنخفضة كافية. الوسائط عالية الدقة تزيد بشكل كبير من استهلاك الرموز المميزة والتكاليف دون تحسين النتائج دائماً.*

## Troubleshooting

### AI Not Following Instructions
If the AI isn't following your instructions, check that your system prompt is clear and specific. Ensure it's in a system message, not a user message. Try making instructions more explicit and adding examples.

*إذا كان الذكاء الاصطناعي لا يتبع تعليماتك، تحقق من أن مطلب النظام واضح ومحدد. تأكد من أنه في رسالة نظام، وليس في رسالة مستخدم. حاول جعل التعليمات أكثر وضوحاً وإضافة أمثلة.*

### Context Loss in Long Conversations
If the AI loses context in long conversations, ensure you're including relevant previous messages. Consider using message compression or increasing the context window. Some models have limited context windows.

*إذا فقد الذكاء الاصطناعي السياق في المحادثات الطويلة، تأكد من تضمين الرسائل السابقة ذات الصلة. فكر في استخدام ضغط الرسائل أو زيادة نافذة السياق. بعض النماذج لها نوافذ سياق محدودة.*

### Multimodal Content Not Processing
If images, videos, or audio aren't being processed, verify the model supports multimodal inputs. Check file formats are supported and file sizes are within limits. Ensure content is properly encoded (base64 or URL).

*إذا لم تتم معالجة الصور أو الفيديو أو الصوت، تحقق من أن النموذج يدعم المدخلات متعددة الوسائط. تحقق من أن تنسيقات الملفات مدعومة وأحجام الملفات ضمن الحدود. تأكد من ترميز المحتوى بشكل صحيح (base64 أو URL).*

### High Token Costs
If token costs are high, review message lengths and multimodal content usage. Optimize system prompts for caching. Consider using message compression for long conversations. Use appropriate media resolutions.

*إذا كانت تكاليف الرموز المميزة عالية، راجع أطوال الرسائل واستخدام المحتوى متعدد الوسائط. قم بتحسين مطالب النظام للتخزين المؤقت. فكر في استخدام ضغط الرسائل للمحادثات الطويلة. استخدم دقة الوسائط المناسبة.*

## Basic Usage

### Simple Text Message

*رسالة نصية بسيطة*

```python
from app.builders import ChatRequestBuilder

builder = ChatRequestBuilder()
request = builder.with_model("openai/gpt-4o").with_text("Hello!").build()
```

### System Prompt

*مطلب النظام*

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_system_prompt("You are a helpful assistant.")
    .with_text("What is Python?")
    .build())
```

### Custom Messages

*رسائل مخصصة*

```python
from app.models.requests.base_request import Message
from app.enums import MessageRole

message = Message(role=MessageRole.USER.value, content="Hello!")
request = builder.with_model("openai/gpt-4o").add_message(message).build()
```

### Multimodal Messages

*رسائل متعددة الوسائط*

```python
from app.models.requests.content import TextContent, ImageContent
from app.builders import ContentBuilder
from app.enums import MessageRole

text = TextContent(text="What is in this image?")
image = ContentBuilder.from_url("https://example.com/image.jpg", "image")

request = (ChatRequestBuilder()
    .with_model("google/gemini-2.5-flash")
    .with_message(MessageRole.USER, [text, image])
    .build())
```

## Advanced Examples

### Conversation with Context

*محادثة مع سياق*

```python
from app.builders import ChatRequestBuilder
from app.enums import MessageRole

# First message
request1 = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_system_prompt("You are a coding tutor.")
    .with_text("Explain what a decorator is in Python")
    .build())

# Follow-up message maintaining context
request2 = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_system_prompt("You are a coding tutor.")
    .add_message(Message(role=MessageRole.USER, content="Explain what a decorator is in Python"))
    .add_message(Message(role=MessageRole.ASSISTANT, content="[Previous response]"))
    .with_text("Can you show me a practical example?")
    .build())
```

### Complex Multimodal Analysis

*تحليل متعدد الوسائط معقد*

```python
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole

# Analyze document with image
document = ContentBuilder.from_url("https://example.com/report.pdf", "file")
chart_image = ContentBuilder.from_url("https://example.com/chart.png", "image")

request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_system_prompt("You are a data analyst. Analyze documents and images to extract insights.")
    .with_message(MessageRole.USER, [
        TextContent(text="Analyze this report and chart:"),
        document,
        chart_image
    ])
    .build())
```

### Structured Output with Messages

*إخراج منظم مع الرسائل*

```python
request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_system_prompt("Extract information and return as JSON.")
    .with_text("Extract key information from: John Doe, age 30, works at Tech Corp")
    .with_structured_output(
        schema={
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
                "company": {"type": "string"}
            }
        },
        name="PersonInfo"
    )
    .build())
```
