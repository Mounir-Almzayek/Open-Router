"""
Message Transformer
"""
from typing import List
from app.models.base import BaseRequest
from app.models.requests.base_request import Message
from app.enums import MessageRole
from app.transformers.base_transformer import BaseTransformer


class MessageTransformer(BaseTransformer):
    """Transform messages in requests"""
    
    def add_system_prompt(self, request: BaseRequest, prompt: str) -> BaseRequest:
        """Add system prompt to request"""
        system_message = Message(role=MessageRole.SYSTEM.value, content=prompt)
        if not hasattr(request, 'messages') or request.messages is None:
            request.messages = []
        request.messages.insert(0, system_message)
        return request
    
    def merge_messages(self, request: BaseRequest, messages: List[Message]) -> BaseRequest:
        """Merge additional messages"""
        if not hasattr(request, 'messages') or request.messages is None:
            request.messages = []
        request.messages.extend(messages)
        return request
    
    def transform(self, request: BaseRequest) -> BaseRequest:
        """Transform request (default: no transformation)"""
        return request

