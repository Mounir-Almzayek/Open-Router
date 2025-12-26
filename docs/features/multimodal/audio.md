# Audio

## Feature Overview

Audio processing enables AI models to understand, transcribe, and analyze audio content including speech, music, and environmental sounds. This feature allows you to send audio files to AI models for transcription, language understanding, sentiment analysis, and audio content analysis. Audio can be provided via base64 encoding or direct file uploads.

*معالجة الصوت تمكن نماذج الذكاء الاصطناعي من فهم ونسخ وتحليل محتوى الصوت بما في ذلك الكلام والموسيقى والأصوات البيئية. تتيح لك هذه الميزة إرسال ملفات الصوت إلى نماذج الذكاء الاصطناعي للنسخ وفهم اللغة وتحليل المشاعر وتحليل محتوى الصوت. يمكن توفير الصوت عبر ترميز base64 أو رفع الملفات مباشرة.*

## Feature Importance

Audio understanding enables applications that need to process spoken content, analyze audio signals, and extract information from audio sources. From transcription services and voice assistants to content analysis and accessibility features, audio processing is essential for creating inclusive and voice-enabled applications.

*فهم الصوت يتيح التطبيقات التي تحتاج إلى معالجة المحتوى المنطوق وتحليل إشارات الصوت واستخراج المعلومات من مصادر الصوت. من خدمات النسخ والمساعدين الصوتيين إلى تحليل المحتوى وميزات إمكانية الوصول، معالجة الصوت ضرورية لإنشاء تطبيقات شاملة ومدعومة بالصوت.*

## Key Benefits

### Speech Transcription
AI models can transcribe spoken words into text with high accuracy, enabling applications like meeting notes, interview transcripts, and voice-to-text conversion. This makes audio content searchable and accessible.

*يمكن لنماذج الذكاء الاصطناعي نسخ الكلمات المنطوقة إلى نص بدقة عالية، مما يتيح التطبيقات مثل ملاحظات الاجتماعات ونسخ المقابلات وتحويل الصوت إلى نص. هذا يجعل محتوى الصوت قابلاً للبحث والوصول.*

### Language Understanding
Audio processing enables understanding of spoken language, including sentiment, intent, and meaning. This enables voice assistants, customer service bots, and applications that need to understand human speech.

*معالجة الصوت تمكن من فهم اللغة المنطوقة، بما في ذلك المشاعر والنية والمعنى. هذا يتيح المساعدين الصوتيين وروبوتات خدمة العملاء والتطبيقات التي تحتاج إلى فهم الكلام البشري.*

### Content Analysis
Audio content can be analyzed for music identification, sound classification, speaker identification, and content moderation. This enables applications that need to understand and categorize audio content.

*يمكن تحليل محتوى الصوت لتحديد الموسيقى وتصنيف الصوت وتحديد المتحدث وإدارة المحتوى. هذا يتيح التطبيقات التي تحتاج إلى فهم وتصنيف محتوى الصوت.*

### Accessibility Features
Audio transcription makes content accessible to hearing-impaired users. Automatic captions and transcripts enable inclusive access to audio and video content.

*نسخ الصوت يجعل المحتوى قابلاً للوصول للمستخدمين ضعاف السمع. التسميات التوضيحية والنسخ التلقائية تمكن الوصول الشامل لمحتوى الصوت والفيديو.*

### Multimodal Integration
Combining audio with other modalities (text, images, video) enables rich understanding of multimedia content. This allows for comprehensive analysis of content that includes audio components.

*دمج الصوت مع الوسائط الأخرى (النص، الصور، الفيديو) يتيح فهماً غنياً للمحتوى متعدد الوسائط. هذا يسمح بتحليل شامل للمحتوى الذي يتضمن مكونات صوتية.*

## Use Cases

### Meeting Transcription
Transcribe meeting recordings to create searchable notes, action items, and summaries. This enables better meeting documentation and follow-up without manual note-taking.

*انسخ تسجيلات الاجتماعات لإنشاء ملاحظات قابلة للبحث وعناصر العمل والملخصات. هذا يتيح توثيق اجتماع أفضل والمتابعة دون تدوين يدوي.*

### Customer Service Analysis
Analyze customer service calls to understand sentiment, identify issues, extract key information, and improve service quality. This enables data-driven customer service improvements.

*حلل مكالمات خدمة العملاء لفهم المشاعر وتحديد المشاكل واستخراج المعلومات الرئيسية وتحسين جودة الخدمة. هذا يتيح تحسينات خدمة العملاء القائمة على البيانات.*

### Podcast and Media Transcription
Transcribe podcasts, interviews, and media content to make them searchable and accessible. Generate summaries, extract key points, and enable content discovery through text search.

*انسخ البودكاست والمقابلات ومحتوى الوسائط لجعلها قابلة للبحث والوصول. أنشئ ملخصات واستخرج النقاط الرئيسية ومكن اكتشاف المحتوى من خلال البحث النصي.*

### Language Learning
Analyze pronunciation, provide feedback, and support language learning through audio analysis. This enables interactive language learning applications.

*حلل النطق ووفر ردود فعل وادعم تعلم اللغة من خلال تحليل الصوت. هذا يتيح تطبيقات تعلم اللغة التفاعلية.*

### Content Moderation
Analyze audio content for inappropriate language, hate speech, or policy violations. This enables automated content moderation for audio platforms and services.

*حلل محتوى الصوت للغة غير مناسبة أو خطاب الكراهية أو انتهاكات السياسة. هذا يتيح إدارة المحتوى الآلية لمنصات وخدمات الصوت.*

## Performance Considerations

### Audio Length Impact
Longer audio files consume more tokens and processing time. Audio processing is computationally intensive—even short audio clips can consume significant tokens. Optimize audio length based on actual needs.

*ملفات الصوت الأطول تستهلك المزيد من الرموز المميزة ووقت المعالجة. معالجة الصوت مكثفة حسابياً—حتى مقاطع الصوت القصيرة يمكن أن تستهلك رموزاً مميزة كبيرة. قم بتحسين طول الصوت بناءً على الاحتياجات الفعلية.*

### Sample Rate and Quality
Higher sample rates and bit depths provide better quality but increase file size and processing requirements. Most transcription tasks work well with standard quality (16kHz, 16-bit). Higher quality is rarely necessary.

*معدلات العينة وأعماق البت الأعلى توفر جودة أفضل لكنها تزيد حجم الملف ومتطلبات المعالجة. معظم مهام النسخ تعمل بشكل جيد مع الجودة القياسية (16kHz، 16-bit). الجودة الأعلى نادراً ما تكون ضرورية.*

### Format Selection
Different audio formats have different compression and quality characteristics. WAV is uncompressed and high quality but large. MP3 is compressed and smaller but may have quality loss. Choose formats based on quality requirements and file size constraints.

*تنسيقات الصوت المختلفة لها خصائص ضغط وجودة مختلفة. WAV غير مضغوط وجودة عالية لكنه كبير. MP3 مضغوط وأصغر لكنه قد يكون لديه فقدان جودة. اختر التنسيقات بناءً على متطلبات الجودة وقيود حجم الملف.*

### Processing Time
Audio processing takes time proportional to audio length. Longer audio files require more processing time. Consider asynchronous processing for audio-heavy applications.

*معالجة الصوت تستغرق وقتاً متناسباً مع طول الصوت. ملفات الصوت الأطول تتطلب وقت معالجة أكثر. فكر في المعالجة غير المتزامنة للتطبيقات الثقيلة بالصوت.*

### Language Detection
Some models can automatically detect language, while others require language specification. Automatic detection adds processing overhead but improves usability. Specify language when known to improve accuracy and speed.

*بعض النماذج يمكنها اكتشاف اللغة تلقائياً، بينما تتطلب نماذج أخرى تحديد اللغة. الاكتشاف التلقائي يضيف حمل معالجة لكنه يحسن سهولة الاستخدام. حدد اللغة عند المعرفة لتحسين الدقة والسرعة.*

## Cost Implications

### Token Consumption
Audio files consume tokens based on duration and quality. Longer audio and higher quality consume more tokens. Audio transcription typically consumes hundreds to thousands of tokens per minute of audio.

*ملفات الصوت تستهلك الرموز المميزة بناءً على المدة والجودة. الصوت الأطول والجودة الأعلى تستهلك المزيد من الرموز المميزة. النسخ الصوتي عادة ما يستهلك مئات إلى آلاف الرموز المميزة لكل دقيقة من الصوت.*

### Quality and Cost Trade-offs
Higher quality audio (higher sample rate, bit depth) increases file size and token consumption. Standard quality (16kHz, 16-bit) is usually sufficient for transcription and provides good cost-quality balance.

*الصوت عالي الجودة (معدل عينة أعلى، عمق بت أعلى) يزيد حجم الملف واستهلاك الرموز المميزة. الجودة القياسية (16kHz، 16-bit) عادة ما تكون كافية للنسخ وتوفر توازن جودة-تكلفة جيد.*

### Format Impact
Uncompressed formats (WAV) are larger and consume more tokens than compressed formats (MP3, AAC). However, compression may slightly reduce transcription accuracy. Balance file size and quality based on your needs.

*التنسيقات غير المضغوطة (WAV) أكبر وتستهلك رموزاً مميزة أكثر من التنسيقات المضغوطة (MP3، AAC). ومع ذلك، قد يقلل الضغط دقة النسخ قليلاً. وازن حجم الملف والجودة بناءً على احتياجاتك.*

### Base64 Overhead
Base64 encoding increases audio file size by ~33%, increasing token consumption. For large audio files, consider using file uploads instead of base64 to reduce overhead.

*ترميز base64 يزيد حجم ملف الصوت بنحو 33%، مما يزيد استهلاك الرموز المميزة. لملفات الصوت الكبيرة، فكر في استخدام رفع الملفات بدلاً من base64 لتقليل الحمل.*

## Best Practices

### Optimize Audio Length
Keep audio files as short as possible while maintaining necessary content. Extract relevant segments rather than sending entire long recordings. Most transcription tasks don't need full-length audio.

*حافظ على ملفات الصوت قصيرة قدر الإمكان مع الحفاظ على المحتوى الضروري. استخرج المقاطع ذات الصلة بدلاً من إرسال التسجيلات الطويلة الكاملة. معظم مهام النسخ لا تحتاج صوتاً كامل الطول.*

### Quality Selection
Use standard quality (16kHz sample rate, 16-bit depth) for most transcription tasks. Higher quality is rarely necessary and significantly increases costs. Only use high quality when audio clarity is critical.

*استخدم الجودة القياسية (معدل عينة 16kHz، عمق 16-bit) لمعظم مهام النسخ. الجودة الأعلى نادراً ما تكون ضرورية وتزيد التكاليف بشكل كبير. استخدم الجودة العالية فقط عندما تكون وضوح الصوت حرجاً.*

### Format Choice
Use MP3 or AAC for compressed audio with good quality. Use WAV only when uncompressed quality is required. Balance file size and quality based on your specific needs.

*استخدم MP3 أو AAC للصوت المضغوط بجودة جيدة. استخدم WAV فقط عندما تكون الجودة غير المضغوطة مطلوبة. وازن حجم الملف والجودة بناءً على احتياجاتك المحددة.*

### Language Specification
Specify language when known to improve accuracy and reduce processing time. Use automatic language detection only when language is unknown. Language specification typically improves transcription quality.

*حدد اللغة عند المعرفة لتحسين الدقة وتقليل وقت المعالجة. استخدم اكتشاف اللغة التلقائي فقط عندما تكون اللغة غير معروفة. تحديد اللغة عادة ما يحسن جودة النسخ.*

### Preprocessing
Remove background noise, normalize volume, and ensure clear audio before sending. Poor audio quality reduces transcription accuracy and may require retries, increasing costs.

*أزل ضوضاء الخلفية وطبيعي الصوت وتأكد من وضوح الصوت قبل الإرسال. جودة الصوت الضعيفة تقلل دقة النسخ وقد تتطلب إعادة المحاولة، مما يزيد التكاليف.*

## When NOT to Use

### Don't Send Full-Length Recordings
Avoid sending entire long audio recordings when only specific segments are needed. Extract relevant portions to reduce costs and processing time. Full-length audio is rarely necessary for analysis.

*تجنب إرسال التسجيلات الصوتية الطويلة الكاملة عندما تكون المقاطع المحددة فقط مطلوبة. استخرج الأجزاء ذات الصلة لتقليل التكاليف ووقت المعالجة. الصوت كامل الطول نادراً ما يكون ضرورياً للتحليل.*

### Don't Use Unnecessarily High Quality
Avoid high sample rates and bit depths unless audio clarity is critical. Standard quality (16kHz, 16-bit) is sufficient for most transcription tasks and significantly reduces costs.

*تجنب معدلات العينة وأعماق البت العالية ما لم تكن وضوح الصوت حرجاً. الجودة القياسية (16kHz، 16-bit) كافية لمعظم مهام النسخ وتقلل التكاليف بشكل كبير.*

### Don't Use Base64 for Large Files
Avoid base64 encoding for audio files larger than 5MB. Base64 increases size by 33% and makes requests very large. Use file uploads for large audio files instead.

*تجنب ترميز base64 لملفات الصوت الأكبر من 5MB. base64 يزيد الحجم بنسبة 33% ويجعل الطلبات كبيرة جداً. استخدم رفع الملفات لملفات الصوت الكبيرة بدلاً من ذلك.*

### Don't Process Poor Quality Audio
Avoid processing audio with excessive background noise, low volume, or poor clarity. Poor quality audio produces inaccurate transcriptions and wastes tokens. Preprocess audio to improve quality first.

*تجنب معالجة الصوت مع ضوضاء خلفية مفرطة أو حجم منخفض أو وضوح ضعيف. الصوت ذو الجودة الضعيفة ينتج نسخاً غير دقيقة ويهدر الرموز المميزة. قم بمعالجة مسبقة للصوت لتحسين الجودة أولاً.*

## Troubleshooting

### Audio Not Processing
If audio isn't being processed, verify the model supports audio inputs. Check audio format is supported (WAV, MP3, AIFF, AAC, OGG, FLAC, M4A). Ensure audio is properly encoded and not corrupted. Check file size limits.

*إذا لم تتم معالجة الصوت، تحقق من أن النموذج يدعم مدخلات الصوت. تحقق من أن تنسيق الصوت مدعوم (WAV، MP3، AIFF، AAC، OGG، FLAC، M4A). تأكد من ترميز الصوت بشكل صحيح وعدم تلفه. تحقق من حدود حجم الملف.*

### Poor Transcription Accuracy
If transcription accuracy is poor, check audio quality—ensure clear speech, minimal background noise, and adequate volume. Specify language if known. Use higher quality audio if necessary. Ensure proper audio format.

*إذا كانت دقة النسخ ضعيفة، تحقق من جودة الصوت—تأكد من وضوح الكلام وضوضاء خلفية قليلة وحجم كافٍ. حدد اللغة إذا كانت معروفة. استخدم صوتاً عالي الجودة إذا لزم الأمر. تأكد من تنسيق الصوت الصحيح.*

### High Token Costs
If token costs are high, review audio length, quality, and format. Shorten audio to necessary segments. Use standard quality (16kHz, 16-bit). Use compressed formats (MP3, AAC) instead of uncompressed (WAV). Ensure you're using file uploads instead of base64 for large files.

*إذا كانت تكاليف الرموز المميزة عالية، راجع طول الصوت والجودة والتنسيق. قصر الصوت على المقاطع الضرورية. استخدم الجودة القياسية (16kHz، 16-bit). استخدم التنسيقات المضغوطة (MP3، AAC) بدلاً من غير المضغوطة (WAV). تأكد من استخدام رفع الملفات بدلاً من base64 للملفات الكبيرة.*

### Processing Timeouts
If audio processing times out, the audio file may be too long or too large. Segment long audio into shorter clips. Reduce quality and file size. Consider asynchronous processing for audio-heavy applications.

*إذا انتهت مهلة معالجة الصوت، قد يكون ملف الصوت طويلاً جداً أو كبيراً جداً. قسّم الصوت الطويل إلى مقاطع أقصر. قلل الجودة وحجم الملف. فكر في المعالجة غير المتزامنة للتطبيقات الثقيلة بالصوت.*

## Basic Usage

### From Base64

*من Base64*

```python
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole

audio_content = ContentBuilder.from_base64_string(
    base64_data, "audio", "audio/wav"
)
request = (ChatRequestBuilder()
    .with_model("openai/whisper-large-v3")
    .with_message(MessageRole.USER, [audio_content])
    .build())
```

### From Upload File

*من ملف مرفوع*

```python
from fastapi import UploadFile

async def transcribe_audio(upload_file: UploadFile):
    audio_content = await ContentBuilder.from_upload_file(upload_file, "audio")
    request = (ChatRequestBuilder()
        .with_model("openai/whisper-large-v3")
        .with_message(MessageRole.USER, [audio_content])
        .build())
```

### Supported Formats

*التنسيقات المدعومة*

- WAV
- MP3
- AIFF
- AAC
- OGG
- FLAC
- M4A

### Audio Format Detection

*اكتشاف تنسيق الصوت*

The handler automatically detects format from MIME type:

*المعالج يكتشف تنسيق الصوت تلقائياً من نوع MIME:*

```python
# MIME type: audio/wav -> format: wav
# MIME type: audio/mpeg -> format: mp3
```

### Transcription Example

*مثال النسخ*

```python
request = (ChatRequestBuilder()
    .with_model("openai/whisper-large-v3")
    .with_message(MessageRole.USER, [audio_content])
    .with_text("Transcribe this audio")
    .build())
```

## Advanced Examples

### Meeting Transcription with Summary

*نسخ الاجتماع مع الملخص*

```python
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole

audio_content = ContentBuilder.from_url("https://example.com/meeting.mp3", "audio")

request = (ChatRequestBuilder()
    .with_model("openai/whisper-large-v3")
    .with_message(MessageRole.USER, [audio_content])
    .with_text("Transcribe this meeting and extract key points, action items, and decisions made.")
    .with_structured_output(
        schema={
            "type": "object",
            "properties": {
                "transcript": {"type": "string"},
                "key_points": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "action_items": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "item": {"type": "string"},
                            "assignee": {"type": "string"}
                        }
                    }
                },
                "decisions": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        },
        name="MeetingTranscript"
    )
    .build())
```

### Sentiment Analysis from Audio

*تحليل المشاعر من الصوت*

```python
audio_content = ContentBuilder.from_url("https://example.com/call.mp3", "audio")

request = (ChatRequestBuilder()
    .with_model("openai/whisper-large-v3")
    .with_message(MessageRole.USER, [audio_content])
    .with_text("Transcribe this customer service call and analyze the sentiment. Identify if the customer is satisfied, frustrated, or neutral.")
    .with_structured_output(
        schema={
            "type": "object",
            "properties": {
                "transcript": {"type": "string"},
                "sentiment": {"type": "string"},
                "emotions": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "key_issues": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        },
        name="CallAnalysis"
    )
    .build())
```

### Multi-Language Transcription

*نسخ متعدد اللغات*

```python
audio_content = ContentBuilder.from_url("https://example.com/multilang.mp3", "audio")

request = (ChatRequestBuilder()
    .with_model("openai/whisper-large-v3")
    .with_message(MessageRole.USER, [audio_content])
    .with_text("Transcribe this audio. It may contain multiple languages. Detect and transcribe each language separately.")
    .build())
```
