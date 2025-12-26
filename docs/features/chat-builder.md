# ChatRequestBuilder Features

*ميزات ChatRequestBuilder*

## Overview

*نظرة عامة*

`ChatRequestBuilder` provides a fluent API for building chat requests with all OpenRouter features.

*`ChatRequestBuilder` يوفر API سلس لبناء طلبات الدردشة مع جميع ميزات OpenRouter.*

## Basic Usage

*الاستخدام الأساسي*

```python
from app.builders import ChatRequestBuilder

builder = ChatRequestBuilder()
request = builder.with_model("openai/gpt-4o").with_text("Hello!").build()
```

## Available Methods

*الطرق المتاحة*

### Model Selection

*اختيار النموذج*

- `with_model(model: str)` - Set model
  *`with_model(model: str)` - تعيين النموذج*
- `with_model_fallbacks(*models: str)` - Add fallback models
  *`with_model_fallbacks(*models: str)` - إضافة نماذج نسخ احتياطي*
- `with_model_variant(variant: ModelVariant)` - Add model variant
  *`with_model_variant(variant: ModelVariant)` - إضافة متغير النموذج*

### Messages

*الرسائل*

- `with_text(text: str)` - Add text message
  *`with_text(text: str)` - إضافة رسالة نصية*
- `with_system_prompt(prompt: str)` - Add system prompt
  *`with_system_prompt(prompt: str)` - إضافة مطلب النظام*
- `with_message(role: MessageRole, content)` - Add custom message
  *`with_message(role: MessageRole, content)` - إضافة رسالة مخصصة*

### Generation Parameters

*معاملات التوليد*

- `with_temperature(temperature: float)`
- `with_top_p(top_p: float)`
- `with_max_tokens(max_tokens: int)`
- `with_stop(stop: Union[str, List[str]])`
- `with_seed(seed: int)`

### Streaming

*البث التدفقي*

- `with_streaming(stream: bool = True)`

### Provider Routing

*توجيه المزود*

- `with_provider_order(providers: List[str])`
- `with_zdr(enabled: bool = True)`
- `with_data_collection(policy: DataCollection)`

### Plugins

*الإضافات*

- `with_web_search(max_results: int = 5, engine: Optional[str] = None)`
- `with_pdf_processing(engine: PDFEngine = PDFEngine.MISTRAL_OCR)`
- `with_response_healing()`

### Advanced Features

*الميزات المتقدمة*

- `with_reasoning(effort: ReasoningEffort, exclude: bool = False)`
- `with_structured_output(schema: Dict, name: str, strict: bool = True)`
- `with_tools(tools: List[ToolDefinition], tool_choice: Optional[Union[str, ToolChoiceConfig]] = "auto")`
- `with_image_generation(aspect_ratio: Optional[AspectRatio] = None, image_size: Optional[ImageSize] = None)`
- `with_middle_out_compression()`
- `with_prompt_caching(text: str, ttl: Optional[CacheTTL] = None)`

## Examples

*أمثلة*

See [Examples](../examples/README.md) for detailed usage examples.

*راجع [أمثلة](../examples/README.md) لأمثلة استخدام مفصلة.*

