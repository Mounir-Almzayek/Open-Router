# Getting Started

*البدء*

## Installation

*التثبيت*

1. Clone the repository
   *استنسخ المستودع*
2. Install dependencies:
   *ثبت التبعيات:*
```bash
pip install -r requirements.txt
```

## Configuration

*التكوين*

1. Copy `.env.example` to `.env`
   *انسخ `.env.example` إلى `.env`*
2. Set your OpenRouter API key:
   *قم بتعيين مفتاح OpenRouter API الخاص بك:*
```bash
OPENROUTER_API_KEY=your_api_key_here
```

## Running the Server

*تشغيل الخادم*

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

*API سيكون متاحاً على `http://localhost:8000`*

## First Request

*الطلب الأول*

### Using Python

*استخدام Python*

```python
from app.builders import ChatRequestBuilder
from app.services import OpenRouterClient

builder = ChatRequestBuilder()
request = builder.with_model("openai/gpt-4o").with_text("Hello!").build()

client = OpenRouterClient()
response = await client.chat_completion(request)
print(response.choices[0].message.content)
```

### Using cURL

*استخدام cURL*

```bash
curl -X POST "http://localhost:8000/api/v1/chat/completions" \
  -H "Authorization: Bearer your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-4o",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Next Steps

*الخطوات التالية*

- Read [Basic Examples](../examples/basic-examples.md)
  *اقرأ [أمثلة أساسية](../examples/basic-examples.md)*
- Explore [Advanced Features](../features/advanced/tool-calling.md)
  *استكشف [ميزات متقدمة](../features/advanced/tool-calling.md)*
- Check [Best Practices](./best-practices.md)
  *تحقق من [أفضل الممارسات](./best-practices.md)*

