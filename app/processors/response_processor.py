"""
Main Response Processor
"""
from typing import Dict, Any
from app.models.responses import ChatResponse
from app.processors.content_extractor import ContentExtractor
from app.processors.usage_analyzer import UsageAnalyzer
from app.processors.reasoning_extractor import ReasoningExtractor
from app.processors.tool_call_processor import ToolCallProcessor
from app.processors.annotation_processor import AnnotationProcessor


class ResponseProcessor:
    """Main response processor that combines all processors"""
    
    def __init__(self):
        self.content_extractor = ContentExtractor()
        self.usage_analyzer = UsageAnalyzer()
        self.reasoning_extractor = ReasoningExtractor()
        self.tool_call_processor = ToolCallProcessor()
        self.annotation_processor = AnnotationProcessor()
    
    def process(self, response: ChatResponse) -> Dict[str, Any]:
        """Process response with all processors"""
        return {
            "content": self.content_extractor.process(response),
            "usage": self.usage_analyzer.process(response),
            "reasoning": self.reasoning_extractor.process(response),
            "tool_calls": self.tool_call_processor.process(response),
            "annotations": self.annotation_processor.process(response),
            "model": response.model,
            "provider": response.provider
        }

