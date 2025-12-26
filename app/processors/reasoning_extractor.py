"""
Reasoning Extractor
"""
from typing import List, Optional, Dict, Any
from app.models.responses import ChatResponse
from app.processors.base_processor import BaseResponseProcessor


class ReasoningExtractor(BaseResponseProcessor):
    """Extract and process reasoning tokens"""
    
    def extract_all_reasoning(self, response: ChatResponse) -> List[Dict[str, Any]]:
        """Extract all reasoning details"""
        reasoning_list = []
        if response.choices:
            message = response.choices[0].message
            if message.reasoning_details:
                for detail in message.reasoning_details:
                    reasoning_list.append({
                        "type": detail.type,
                        "text": detail.text,
                        "summary": detail.summary,
                        "data": detail.data,
                        "index": detail.index
                    })
        return reasoning_list
    
    def extract_reasoning_text(self, response: ChatResponse) -> str:
        """Extract reasoning text only"""
        reasoning_text = []
        if response.choices:
            message = response.choices[0].message
            if message.reasoning_details:
                for detail in message.reasoning_details:
                    if detail.text:
                        reasoning_text.append(detail.text)
                    elif detail.summary:
                        reasoning_text.append(detail.summary)
        return "\n".join(reasoning_text)
    
    def process(self, response: ChatResponse) -> Dict[str, Any]:
        """Process response and extract reasoning"""
        return {
            "reasoning_details": self.extract_all_reasoning(response),
            "reasoning_text": self.extract_reasoning_text(response)
        }

