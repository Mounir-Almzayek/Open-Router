"""
Tool Call Processor
"""
from typing import List, Dict, Any, Optional
from app.models.responses import ChatResponse
from app.models.tools import ToolCall
from app.processors.base_processor import BaseResponseProcessor
import json


class ToolCallProcessor(BaseResponseProcessor):
    """Process tool calls from responses"""
    
    def extract_tool_calls(self, response: ChatResponse) -> List[ToolCall]:
        """Extract tool calls"""
        tool_calls = []
        if response.choices:
            message = response.choices[0].message
            if message.tool_calls:
                tool_calls = message.tool_calls
        return tool_calls
    
    def parse_tool_arguments(self, tool_call: ToolCall) -> Dict[str, Any]:
        """Parse tool call arguments from JSON string"""
        try:
            return json.loads(tool_call.function.arguments)
        except json.JSONDecodeError:
            return {}
    
    def get_tool_name(self, tool_call: ToolCall) -> str:
        """Get tool name from tool call"""
        return tool_call.function.name
    
    def process_tool_calls(self, response: ChatResponse) -> List[Dict[str, Any]]:
        """Process all tool calls and return structured data"""
        tool_calls = self.extract_tool_calls(response)
        processed = []
        
        for tool_call in tool_calls:
            processed.append({
                "id": tool_call.id,
                "name": self.get_tool_name(tool_call),
                "arguments": self.parse_tool_arguments(tool_call)
            })
        
        return processed
    
    def process(self, response: ChatResponse) -> Dict[str, Any]:
        """Process response and extract tool calls"""
        return {
            "tool_calls": self.process_tool_calls(response),
            "has_tool_calls": len(self.extract_tool_calls(response)) > 0
        }

