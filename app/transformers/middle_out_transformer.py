"""
Middle-Out Compression Transformer
"""
from typing import List
from app.models.base import BaseRequest
from app.models.requests.base_request import Message
from app.transformers.base_transformer import BaseTransformer


class MiddleOutTransformer(BaseTransformer):
    """Middle-out compression transformer"""
    
    def transform(self, request: BaseRequest) -> BaseRequest:
        """Apply middle-out compression if enabled"""
        if not hasattr(request, 'transforms') or not request.transforms:
            return request
        
        from app.enums import TransformType
        if TransformType.MIDDLE_OUT not in request.transforms:
            return request
        
        # Apply middle-out compression
        if hasattr(request, 'messages') and request.messages:
            request.messages = self._compress_messages(request.messages)
        
        return request
    
    def _compress_messages(self, messages: List[Message]) -> List[Message]:
        """
        Compress messages using middle-out strategy
        Keeps first and last messages, compresses middle
        """
        if len(messages) <= 2:
            return messages
        
        # Keep first message (usually system)
        first = messages[0]
        
        # Keep last message (current user input)
        last = messages[-1]
        
        # Compress middle messages
        middle = messages[1:-1]
        compressed_middle = self._compress_middle_messages(middle)
        
        return [first] + compressed_middle + [last]
    
    def _compress_middle_messages(self, messages: List[Message]) -> List[Message]:
        """Compress middle messages by truncating content"""
        if not messages:
            return []
        
        # Keep only summary or truncate
        compressed = []
        for msg in messages:
            if hasattr(msg, 'content'):
                if isinstance(msg.content, str):
                    # Truncate long content
                    if len(msg.content) > 500:
                        msg.content = msg.content[:250] + "..." + msg.content[-250:]
                # For list content, keep only first and last items
                elif isinstance(msg.content, list) and len(msg.content) > 2:
                    msg.content = [msg.content[0], msg.content[-1]]
            compressed.append(msg)
        
        return compressed

