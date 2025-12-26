# Data Flow

## Request Flow

```
1. Client Request (FastAPI)
   ↓
2. Router (app/routers/)
   ↓
3. Builder (app/builders/) - Build request
   ↓
4. Validator (app/validators/) - Validate request
   ↓
5. Transformer (app/transformers/) - Transform if needed
   ↓
6. OpenRouter Client (app/services/)
   ↓
7. OpenRouter API
   ↓
8. Response Processor (app/processors/)
   ↓
9. Response to Client
```

## File Upload Flow

```
1. UploadFile from FastAPI
   ↓
2. DirectFileHandler (app/utils/file_handler.py)
   - Read file in memory
   - Encode to base64
   - Create data URL
   ↓
3. ContentBuilder (app/builders/content_builder.py)
   - Create ImageContent/VideoContent/etc.
   ↓
4. ChatRequestBuilder
   - Add to message content
   ↓
5. OpenRouter API (direct, no local storage)
```

## Streaming Flow

```
1. Request with stream=True
   ↓
2. OpenRouter Client streams response
   ↓
3. StreamProcessor processes chunks
   ↓
4. StreamingResponse to client
```

## Error Handling Flow

```
1. Exception occurs
   ↓
2. Custom exception raised
   ↓
3. Retry strategy (if applicable)
   ↓
4. Error response to client
```

