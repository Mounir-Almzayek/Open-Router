"""
Content Extractor
"""
from typing import List, Optional
from app.models.responses import ChatResponse, MessageResponse
from app.models.responses import Usage
from app.processors.base_processor import BaseResponseProcessor


class ContentExtractor(BaseResponseProcessor):
    """Extract content from responses"""
    
    def extract_text(self, response: ChatResponse) -> str:
        """Extract text content"""
        if response.choices and len(response.choices) > 0:
            return response.choices[0].message.content or ""
        return ""
    
    def extract_images(self, response: ChatResponse) -> List[str]:
        """Extract generated images"""
        images = []
        if response.choices:
            message = response.choices[0].message
            if message.images:
                for image in message.images:
                    if image.image_url:
                        images.append(image.image_url.url)
        return images
    
    def extract_reasoning(self, response: ChatResponse) -> Optional[str]:
        """Extract reasoning tokens (legacy field)"""
        if response.choices:
            message = response.choices[0].message
            if message.reasoning:
                return message.reasoning
        return None
    
    def extract_reasoning_details(self, response: ChatResponse) -> Optional[List]:
        """Extract reasoning details"""
        if response.choices:
            message = response.choices[0].message
            if message.reasoning_details:
                return message.reasoning_details
        return None
    
    def extract_usage(self, response: ChatResponse) -> Optional[Usage]:
        """Extract usage information"""
        return response.usage
    
    def extract_tool_calls(self, response: ChatResponse) -> List:
        """Extract tool calls"""
        tool_calls = []
        if response.choices:
            message = response.choices[0].message
            if message.tool_calls:
                tool_calls = message.tool_calls
        return tool_calls
    
    def extract_annotations(self, response: ChatResponse) -> List:
        """Extract annotations (citations, etc.)"""
        annotations = []
        if response.choices:
            message = response.choices[0].message
            if message.annotations:
                annotations = message.annotations
        return annotations
    
    def process(self, response: ChatResponse) -> dict:
        """Process response and extract all content"""
        return {
            "text": self.extract_text(response),
            "images": self.extract_images(response),
            "reasoning": self.extract_reasoning(response),
            "reasoning_details": self.extract_reasoning_details(response),
            "usage": self.extract_usage(response),
            "tool_calls": self.extract_tool_calls(response),
            "annotations": self.extract_annotations(response)
        }

