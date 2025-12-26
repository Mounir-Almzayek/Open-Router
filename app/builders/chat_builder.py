"""
Chat Request Builder with all OpenRouter features
"""
from typing import Optional, List, Union, Dict, Any
from app.builders.base_builder import BaseRequestBuilder
from app.models.requests.chat_request import ChatRequest
from app.models.requests.base_request import Message
from app.models.requests.provider_config import ProviderConfig
from app.models.requests.plugin_config import PluginConfig, WebPluginConfig, PDFPluginConfig
from app.models.requests.reasoning_config import ReasoningConfig
from app.models.requests.structured_output import ResponseFormatConfig, JSONSchemaConfig
from app.models.requests.chat_request import ImageConfig, WebSearchOptions
from app.models.tools import ToolDefinition, ToolChoiceConfig, ToolChoiceFunction
from app.enums import (
    MessageRole,
    PluginType,
    PDFEngine,
    ReasoningEffort,
    ModelVariant,
    OutputModality,
    TransformType,
    AspectRatio,
    ImageSize,
    DataCollection,
    CacheTTL
)
from app.models.requests.content import BaseContent, TextContent


class ChatRequestBuilder(BaseRequestBuilder[ChatRequest]):
    """Enhanced chat request builder with all features"""
    
    def __init__(self):
        super().__init__()
        self._request = ChatRequest(
            model="",
            messages=[],
            stream=False
        )
    
    def with_model(self, model: str) -> 'ChatRequestBuilder':
        """Set model"""
        self._request.model = model
        return self
    
    def with_model_fallbacks(self, *models: str) -> 'ChatRequestBuilder':
        """Add model fallbacks"""
        self._request.models = list(models)
        return self
    
    def with_message(self, role: MessageRole, content: Union[str, List[BaseContent]]) -> 'ChatRequestBuilder':
        """Add message"""
        message = Message(role=role.value, content=content)
        self._request.messages.append(message)
        return self
    
    def with_text(self, text: str) -> 'ChatRequestBuilder':
        """Add text message"""
        return self.with_message(MessageRole.USER, text)
    
    def with_system_prompt(self, prompt: str) -> 'ChatRequestBuilder':
        """Add system prompt"""
        return self.with_message(MessageRole.SYSTEM, prompt)
    
    def with_streaming(self, stream: bool = True) -> 'ChatRequestBuilder':
        """Enable streaming"""
        self._request.stream = stream
        return self
    
    # Generation parameters
    def with_temperature(self, temperature: float) -> 'ChatRequestBuilder':
        """Set temperature"""
        self._request.temperature = temperature
        return self
    
    def with_top_p(self, top_p: float) -> 'ChatRequestBuilder':
        """Set top_p"""
        self._request.top_p = top_p
        return self
    
    def with_max_tokens(self, max_tokens: int) -> 'ChatRequestBuilder':
        """Set max_tokens"""
        self._request.max_tokens = max_tokens
        return self
    
    def with_stop(self, stop: Union[str, List[str]]) -> 'ChatRequestBuilder':
        """Set stop sequences"""
        self._request.stop = stop
        return self
    
    def with_seed(self, seed: int) -> 'ChatRequestBuilder':
        """Set seed"""
        self._request.seed = seed
        return self
    
    # Provider routing
    def with_provider_order(self, providers: List[str]) -> 'ChatRequestBuilder':
        """Set provider order"""
        if not self._request.provider:
            self._request.provider = ProviderConfig()
        self._request.provider.order = providers
        return self
    
    def with_zdr(self, enabled: bool = True) -> 'ChatRequestBuilder':
        """Enable Zero Data Retention"""
        if not self._request.provider:
            self._request.provider = ProviderConfig()
        self._request.provider.zdr = enabled
        return self
    
    def with_data_collection(self, policy: DataCollection) -> 'ChatRequestBuilder':
        """Set data collection policy"""
        if not self._request.provider:
            self._request.provider = ProviderConfig()
        self._request.provider.data_collection = policy
        return self
    
    # Plugins
    def with_web_search(
        self,
        max_results: int = 5,
        engine: Optional[str] = None
    ) -> 'ChatRequestBuilder':
        """Enable web search plugin"""
        if not self._request.plugins:
            self._request.plugins = []
        self._request.plugins.append(PluginConfig(
            id=PluginType.WEB,
            web=WebPluginConfig(max_results=max_results, engine=engine)
        ))
        return self
    
    def with_pdf_processing(
        self,
        engine: PDFEngine = PDFEngine.MISTRAL_OCR
    ) -> 'ChatRequestBuilder':
        """Enable PDF processing"""
        if not self._request.plugins:
            self._request.plugins = []
        self._request.plugins.append(PluginConfig(
            id=PluginType.FILE_PARSER,
            pdf=PDFPluginConfig(engine=engine)
        ))
        return self
    
    def with_response_healing(self) -> 'ChatRequestBuilder':
        """Enable response healing"""
        if not self._request.plugins:
            self._request.plugins = []
        from app.models.requests.plugin_config import ResponseHealingPluginConfig
        self._request.plugins.append(PluginConfig(
            id=PluginType.RESPONSE_HEALING,
            enabled=True
        ))
        return self
    
    # Reasoning
    def with_reasoning(
        self,
        effort: ReasoningEffort,
        exclude: bool = False
    ) -> 'ChatRequestBuilder':
        """Enable reasoning tokens"""
        self._request.reasoning = ReasoningConfig(effort=effort, exclude=exclude)
        return self
    
    # Structured outputs
    def with_structured_output(
        self,
        schema: Dict[str, Any],
        name: str,
        strict: bool = True
    ) -> 'ChatRequestBuilder':
        """Enable structured output"""
        self._request.response_format = ResponseFormatConfig(
            type="json_schema",
            json_schema=JSONSchemaConfig(name=name, strict=strict, schema=schema)
        )
        return self
    
    def with_json_object_output(self) -> 'ChatRequestBuilder':
        """Enable JSON object output"""
        self._request.response_format = ResponseFormatConfig(type="json_object")
        return self
    
    # Tools
    def with_tools(
        self,
        tools: List[ToolDefinition],
        tool_choice: Optional[Union[str, ToolChoiceConfig]] = "auto"
    ) -> 'ChatRequestBuilder':
        """Add tools for function calling"""
        self._request.tools = tools
        self._request.tool_choice = tool_choice
        return self
    
    # Model variants
    def with_model_variant(self, variant: ModelVariant) -> 'ChatRequestBuilder':
        """Add model variant"""
        if not self._request.model.endswith(variant.value):
            self._request.model += variant.value
        return self
    
    # Image generation
    def with_image_generation(
        self,
        aspect_ratio: Optional[AspectRatio] = None,
        image_size: Optional[ImageSize] = None
    ) -> 'ChatRequestBuilder':
        """Configure image generation"""
        if not self._request.modalities:
            self._request.modalities = []
        if OutputModality.IMAGE not in self._request.modalities:
            self._request.modalities.append(OutputModality.IMAGE)
        if OutputModality.TEXT not in self._request.modalities:
            self._request.modalities.append(OutputModality.TEXT)
        
        if aspect_ratio or image_size:
            self._request.image_config = ImageConfig(
                aspect_ratio=aspect_ratio.value if aspect_ratio else None,
                image_size=image_size.value if image_size else None
            )
        return self
    
    # Message transforms
    def with_middle_out_compression(self) -> 'ChatRequestBuilder':
        """Enable middle-out compression"""
        if not self._request.transforms:
            self._request.transforms = []
        if TransformType.MIDDLE_OUT not in self._request.transforms:
            self._request.transforms.append(TransformType.MIDDLE_OUT)
        return self
    
    # Prompt caching
    def with_prompt_caching(self, text: str, ttl: Optional[CacheTTL] = None) -> 'ChatRequestBuilder':
        """Add cache control to text content"""
        from app.builders.content_builder import ContentBuilder
        text_content = ContentBuilder.create_text_with_cache(text, ttl)
        # Add to last user message or create new one
        if self._request.messages and self._request.messages[-1].role == MessageRole.USER.value:
            if isinstance(self._request.messages[-1].content, list):
                self._request.messages[-1].content.append(text_content)
            else:
                self._request.messages[-1].content = [text_content]
        else:
            self.with_message(MessageRole.USER, [text_content])
        return self

