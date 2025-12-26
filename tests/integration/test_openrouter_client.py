"""
Integration tests for OpenRouter client
"""
import pytest
from unittest.mock import AsyncMock, patch
from app.services import OpenRouterClient
from app.models.requests import ChatRequest
from app.builders import ChatRequestBuilder


@pytest.mark.asyncio
class TestOpenRouterClient:
    """Tests for OpenRouterClient"""
    
    async def test_chat_completion_success(self):
        """Test successful chat completion"""
        client = OpenRouterClient(api_key="test-key")
        
        builder = ChatRequestBuilder()
        request = builder.with_model("openai/gpt-4o").with_text("Hello!").build()
        
        # Mock response
        mock_response = {
            "id": "test-id",
            "model": "openai/gpt-4o",
            "choices": [{
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "Hello! How can I help you?"
                }
            }]
        }
        
        with patch.object(client.session, 'post', new_callable=AsyncMock) as mock_post:
            mock_response_obj = AsyncMock()
            mock_response_obj.is_success = True
            mock_response_obj.json.return_value = mock_response
            mock_post.return_value = mock_response_obj
            
            response = await client.chat_completion(request)
            
            assert response.id == "test-id"
            assert response.model == "openai/gpt-4o"
            assert len(response.choices) == 1
    
    async def test_chat_completion_validation_error(self):
        """Test chat completion with validation error"""
        client = OpenRouterClient(api_key="test-key")
        
        # Invalid request (empty model)
        request = ChatRequest(model="", messages=[], stream=False)
        
        with pytest.raises(Exception):  # Should raise ValidationError
            await client.chat_completion(request)
    
    async def test_list_models(self):
        """Test listing models"""
        client = OpenRouterClient(api_key="test-key")
        
        mock_response = {
            "data": [
                {
                    "id": "openai/gpt-4o",
                    "name": "GPT-4o"
                }
            ]
        }
        
        with patch.object(client.session, 'get', new_callable=AsyncMock) as mock_get:
            mock_response_obj = AsyncMock()
            mock_response_obj.raise_for_status = AsyncMock()
            mock_response_obj.json.return_value = mock_response
            mock_get.return_value = mock_response_obj
            
            models = await client.list_models()
            
            assert len(models) == 1
            assert models[0].id == "openai/gpt-4o"

