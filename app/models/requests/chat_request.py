"""
Chat Request Model with all OpenRouter features
"""
from typing import Optional, List, Union, Dict, Any
from pydantic import BaseModel
from app.models.base import BaseRequest
from app.models.requests.base_request import Message
from app.models.requests.provider_config import ProviderConfig
from app.models.requests.plugin_config import PluginConfig
from app.models.requests.reasoning_config import ReasoningConfig
from app.models.requests.structured_output import ResponseFormatConfig
from app.models.tools import ToolDefinition, ToolChoiceConfig
from app.enums import OutputModality, TransformType


class ImageConfig(BaseModel):
    """Image generation configuration"""
    aspect_ratio: Optional[str] = None  # AspectRatio
    image_size: Optional[str] = None  # ImageSize
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {}
        if self.aspect_ratio is not None:
            result["aspect_ratio"] = self.aspect_ratio
        if self.image_size is not None:
            result["image_size"] = self.image_size
        return result


class WebSearchOptions(BaseModel):
    """Web search options for native search"""
    search_context_size: Optional[str] = None  # "low", "medium", "high"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {}
        if self.search_context_size is not None:
            result["search_context_size"] = self.search_context_size
        return result


class ChatRequest(BaseRequest):
    """Enhanced chat request with all OpenRouter features"""
    model: str
    models: Optional[List[str]] = None  # Model fallbacks
    messages: List[Message]
    stream: bool = False
    
    # Generation parameters
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    max_tokens: Optional[int] = None
    stop: Optional[Union[str, List[str]]] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    seed: Optional[int] = None
    
    # Advanced features
    provider: Optional[ProviderConfig] = None
    plugins: Optional[List[PluginConfig]] = None
    tools: Optional[List[ToolDefinition]] = None
    tool_choice: Optional[Union[str, ToolChoiceConfig]] = None
    parallel_tool_calls: Optional[bool] = None
    reasoning: Optional[ReasoningConfig] = None
    response_format: Optional[ResponseFormatConfig] = None
    modalities: Optional[List[OutputModality]] = None  # For image generation
    image_config: Optional[ImageConfig] = None  # For image generation
    transforms: Optional[List[TransformType]] = None  # Message transforms
    usage: Optional[Dict[str, bool]] = None  # Include usage in response
    web_search_options: Optional[WebSearchOptions] = None  # Native web search
    
    # Provider-specific headers
    extra_headers: Optional[Dict[str, str]] = None  # e.g., x-anthropic-beta
    
    def validate(self) -> bool:
        """Validate request"""
        if not self.model:
            raise ValueError("Model is required")
        if not self.messages:
            raise ValueError("At least one message is required")
        return True
    
    def to_openrouter_format(self) -> Dict[str, Any]:
        """Convert to OpenRouter API format"""
        result = {
            "model": self.model,
            "messages": [msg.to_dict() for msg in self.messages],
            "stream": self.stream
        }
        
        # Add optional fields
        if self.models is not None:
            result["models"] = self.models
        if self.temperature is not None:
            result["temperature"] = self.temperature
        if self.top_p is not None:
            result["top_p"] = self.top_p
        if self.max_tokens is not None:
            result["max_tokens"] = self.max_tokens
        if self.stop is not None:
            result["stop"] = self.stop
        if self.frequency_penalty is not None:
            result["frequency_penalty"] = self.frequency_penalty
        if self.presence_penalty is not None:
            result["presence_penalty"] = self.presence_penalty
        if self.seed is not None:
            result["seed"] = self.seed
        
        # Advanced features
        if self.provider is not None:
            result["provider"] = self.provider.to_dict()
        if self.plugins is not None:
            result["plugins"] = [p.to_dict() for p in self.plugins]
        if self.tools is not None:
            result["tools"] = [t.to_dict() for t in self.tools]
        if self.tool_choice is not None:
            if isinstance(self.tool_choice, str):
                result["tool_choice"] = self.tool_choice
            else:
                result["tool_choice"] = self.tool_choice.to_dict()
        if self.parallel_tool_calls is not None:
            result["parallel_tool_calls"] = self.parallel_tool_calls
        if self.reasoning is not None:
            result["reasoning"] = self.reasoning.to_dict()
        if self.response_format is not None:
            result["response_format"] = self.response_format.to_dict()
        if self.modalities is not None:
            result["modalities"] = [m.value for m in self.modalities]
        if self.image_config is not None:
            result["image_config"] = self.image_config.to_dict()
        if self.transforms is not None:
            result["transforms"] = [t.value for t in self.transforms]
        if self.usage is not None:
            result["usage"] = self.usage
        if self.web_search_options is not None:
            result["web_search_options"] = self.web_search_options.to_dict()
        
        return result

