"""
OpenRouter API Client
"""
from typing import Optional, Dict, Any, AsyncIterator
import httpx
from app.config import settings
from app.models.requests import ChatRequest
from app.models.responses import ChatResponse, StreamChunk
from app.models.openrouter import ModelInfo, CreditsInfo
from app.validators import ValidatorChain
from app.exceptions import (
    OpenRouterAPIError,
    OpenRouterRateLimitError,
    OpenRouterAuthenticationError,
    OpenRouterModelNotFoundError,
    OpenRouterTimeoutError,
    ValidationError
)
from app.decorators import retry_on_failure, log_request, monitor_performance
from app.strategies import ExponentialBackoffStrategy
from app.transformers import RequestTransformer


class OpenRouterClient:
    """Enhanced OpenRouter API client"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None
    ):
        self.api_key = api_key or settings.openrouter_api_key
        self.base_url = base_url or settings.openrouter_base_url
        self.session = httpx.AsyncClient(timeout=settings.openrouter_timeout)
        self.validator = ValidatorChain()
        self.retry_strategy = ExponentialBackoffStrategy()
        self.transformer = RequestTransformer()
    
    def _get_headers(self, extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """Get request headers"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": settings.app_url or "https://github.com/your-org/your-repo",
            "X-Title": settings.app_title or settings.app_name,
        }
        
        if extra_headers:
            headers.update(extra_headers)
        
        return headers
    
    def _handle_error(self, response: httpx.Response) -> None:
        """Handle API errors"""
        if response.status_code == 401:
            raise OpenRouterAuthenticationError("Invalid API key")
        elif response.status_code == 404:
            raise OpenRouterModelNotFoundError("Model not found")
        elif response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            raise OpenRouterRateLimitError(retry_after=int(retry_after) if retry_after else None)
        elif response.status_code == 504:
            raise OpenRouterTimeoutError("Request timeout")
        else:
            try:
                error_data = response.json()
                error_message = error_data.get("error", {}).get("message", "Unknown error")
            except Exception:
                error_message = response.text or "Unknown error"
            raise OpenRouterAPIError(error_message, status_code=response.status_code)
    
    @retry_on_failure(max_attempts=3)
    @log_request
    @monitor_performance
    async def chat_completion(
        self,
        request: ChatRequest,
        headers: Optional[Dict[str, str]] = None
    ) -> ChatResponse:
        """Send chat completion request"""
        # Validate
        validation_result = self.validator.validate(request)
        if not validation_result.is_valid:
            raise ValidationError(validation_result.errors)
        
        # Transform request
        request = self.transformer.transform(request)
        
        # Convert to OpenRouter format
        payload = request.to_openrouter_format()
        
        # Prepare headers
        request_headers = self._get_headers(headers or request.extra_headers)
        
        # Send request
        try:
            response = await self.session.post(
                f"{self.base_url}/chat/completions",
                json=payload,
                headers=request_headers
            )
            
            if not response.is_success:
                self._handle_error(response)
            
            # Parse response
            data = response.json()
            return ChatResponse(**data)
        
        except httpx.TimeoutException:
            raise OpenRouterTimeoutError("Request timeout")
        except httpx.ConnectError:
            raise OpenRouterAPIError("Connection error", status_code=0)
    
    async def stream_chat_completion(
        self,
        request: ChatRequest,
        headers: Optional[Dict[str, str]] = None
    ) -> AsyncIterator[StreamChunk]:
        """Stream chat completion"""
        # Validate
        validation_result = self.validator.validate(request)
        if not validation_result.is_valid:
            raise ValidationError(validation_result.errors)
        
        # Transform request
        request = self.transformer.transform(request)
        
        # Convert to OpenRouter format
        payload = request.to_openrouter_format()
        payload["stream"] = True
        
        # Prepare headers
        request_headers = self._get_headers(headers or request.extra_headers)
        
        # Send request
        async with self.session.stream(
            "POST",
            f"{self.base_url}/chat/completions",
            json=payload,
            headers=request_headers
        ) as response:
            if not response.is_success:
                await self._handle_error(response)
            
            async for line in response.aiter_lines():
                if line.startswith("data: "):
                    data_str = line[6:]
                    if data_str == "[DONE]":
                        break
                    try:
                        import json
                        data = json.loads(data_str)
                        yield StreamChunk(**data)
                    except Exception:
                        continue
    
    async def list_models(self) -> list[ModelInfo]:
        """List available models"""
        try:
            response = await self.session.get(f"{self.base_url}/models")
            response.raise_for_status()
            data = response.json()
            return [ModelInfo(**model) for model in data.get("data", [])]
        except Exception as e:
            raise OpenRouterAPIError(f"Failed to list models: {str(e)}")
    
    async def get_credits(self) -> CreditsInfo:
        """Get credits information"""
        try:
            response = await self.session.get(
                f"{self.base_url}/credits",
                headers=self._get_headers()
            )
            response.raise_for_status()
            data = response.json()
            return CreditsInfo(**data)
        except Exception as e:
            raise OpenRouterAPIError(f"Failed to get credits: {str(e)}")
    
    async def close(self):
        """Close client session"""
        await self.session.aclose()

