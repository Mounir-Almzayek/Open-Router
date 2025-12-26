# Folder Structure

## Project Structure

```
ai-template/
├── app/
│   ├── enums/              # All Enums
│   ├── models/             # Pydantic models
│   │   ├── requests/       # Request models
│   │   ├── responses/      # Response models
│   │   ├── tools/          # Tool calling models
│   │   └── plugins/        # Plugin models
│   ├── builders/           # Builder patterns
│   ├── processors/         # Response processors
│   ├── strategies/         # Strategy patterns
│   ├── decorators/         # Decorator patterns
│   ├── validators/         # Validators (Chain of Responsibility)
│   ├── transformers/       # Request transformers
│   ├── services/           # Business logic
│   ├── routers/            # API routes
│   ├── templates/          # Prompt templates
│   ├── exceptions/         # Custom exceptions
│   ├── utils/              # Utilities
│   └── monitoring/         # Monitoring & observability
├── tests/                  # Test suite
└── docs/                   # Documentation
```

## Key Directories

### `app/enums/`
Contains all Enums for constants:
- `modalities.py` - Input/Output modalities
- `content_types.py` - Content types
- `message_roles.py` - Message roles
- And more...

### `app/models/`
Pydantic models organized by type:
- `requests/` - Request models with OOP
- `responses/` - Response models
- `tools/` - Tool calling models
- `plugins/` - Plugin configuration models

### `app/builders/`
Builder classes for fluent API:
- `chat_builder.py` - Chat request builder
- `content_builder.py` - Content builder

### `app/services/`
Business logic services:
- `openrouter_client.py` - OpenRouter API client
- `template_service.py` - Template management

### `app/routers/`
FastAPI endpoints:
- `chat.py` - Chat completions
- `multimodal.py` - Multimodal with file uploads
- `models.py` - Models API

