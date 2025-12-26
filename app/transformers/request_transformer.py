"""
Request Transformer
"""
from typing import Dict, Any
from app.models.base import BaseRequest
from app.models.requests import ChatRequest
from app.transformers.base_transformer import BaseTransformer
from app.transformers.message_transformer import MessageTransformer
from app.transformers.middle_out_transformer import MiddleOutTransformer


class RequestTransformer:
    """Main request transformer"""
    
    def __init__(self):
        self.message_transformer = MessageTransformer()
        self.middle_out_transformer = MiddleOutTransformer()
    
    def transform(self, request: BaseRequest) -> BaseRequest:
        """Transform request"""
        # Apply middle-out compression if enabled
        if isinstance(request, ChatRequest) and request.transforms:
            request = self.middle_out_transformer.transform(request)
        
        return request
    
    def add_system_prompt(self, request: BaseRequest, prompt: str) -> BaseRequest:
        """Add system prompt"""
        return self.message_transformer.add_system_prompt(request, prompt)
    
    def merge_user_input_to_template(
        self,
        request: BaseRequest,
        user_input: Dict[str, Any]
    ) -> BaseRequest:
        """Merge user input with template"""
        # This will be implemented in template service
        return request

