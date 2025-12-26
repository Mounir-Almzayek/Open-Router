"""Pydantic models with OOP patterns"""
from app.models.base import BaseRequest, BaseResponse, BaseContent
from app.models.requests import (
    Message,
    ChatRequest,
    MultimodalRequest,
    TemplateRequest,
    ProviderConfig,
    PluginConfig,
    ReasoningConfig,
    ResponseFormatConfig,
)
from app.models.responses import (
    ChatResponse,
    MessageResponse,
    ChoiceResponse,
    Usage,
    StreamChunk,
    ReasoningDetail,
    Annotation,
    GeneratedImage,
)
from app.models.tools import ToolDefinition, ToolChoiceConfig, ToolCall
from app.models.openrouter import ModelInfo, CreditsInfo

__all__ = [
    "BaseRequest",
    "BaseResponse",
    "BaseContent",
    "Message",
    "ChatRequest",
    "MultimodalRequest",
    "TemplateRequest",
    "ProviderConfig",
    "PluginConfig",
    "ReasoningConfig",
    "ResponseFormatConfig",
    "ChatResponse",
    "MessageResponse",
    "ChoiceResponse",
    "Usage",
    "StreamChunk",
    "ReasoningDetail",
    "Annotation",
    "GeneratedImage",
    "ToolDefinition",
    "ToolChoiceConfig",
    "ToolCall",
    "ModelInfo",
    "CreditsInfo",
]
