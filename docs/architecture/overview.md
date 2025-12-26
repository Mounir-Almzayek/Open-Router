# Project Architecture Overview

## General Architecture

This project is built on the following principles:
- **Object-Oriented Programming (OOP)**: Extensive use of classes and inheritance
- **Design Patterns**: Builder, Factory, Strategy, Decorator, Chain of Responsibility
- **Type Safety**: Use of Enums and Type Hints throughout
- **Separation of Concerns**: Clear separation of responsibilities

## Main Components

### 1. Enums (`app/enums/`)
All constant values are organized in Enums:
- Modalities (Input/Output)
- Content Types
- Message Roles
- Formats (Audio, Video, Image)
- Provider Options
- Model Variants
- Plugin Types

### 2. Models (`app/models/`)
Pydantic models with OOP patterns:
- Base classes with abstract methods
- Polymorphism for content types
- Built-in validation

### 3. Builders (`app/builders/`)
Builder pattern for requests:
- Fluent API
- Method chaining
- Type-safe

### 4. Services (`app/services/`)
Business logic:
- OpenRouter client
- Template service
- Model service

### 5. Routers (`app/routers/`)
FastAPI endpoints:
- Chat completions
- Multimodal
- Templates
- Models API

## Data Flow

```
Request → Router → Builder → Validator → Transformer → OpenRouter Client → Response Processor → Response
```

## Design Patterns Used

### Builder Pattern
For creating complex requests in an easy and flexible way.

### Factory Pattern
For creating different objects based on input.

### Strategy Pattern
For selecting providers and retry strategies.

### Decorator Pattern
For retry, caching, logging.

### Chain of Responsibility
For validation.

## Benefits

1. **Extensibility**: Easy to add new features
2. **Maintainability**: Well-organized and easy to maintain code
3. **Type Safety**: Reduced errors with Type Hints
4. **Testability**: Easy to write tests
5. **Performance**: Direct processing without unnecessary I/O

