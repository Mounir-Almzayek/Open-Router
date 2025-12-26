"""
Template Request Model
"""
from typing import Optional, Dict, Any
from app.models.requests.chat_request import ChatRequest


class TemplateRequest(ChatRequest):
    """Request with template support"""
    template_id: Optional[str] = None
    template_variables: Optional[Dict[str, Any]] = None
    
    def merge_template(self, template_prompt: str, user_input: Dict[str, Any]) -> 'TemplateRequest':
        """Merge template prompt with user input"""
        # This will be implemented in template service
        return self

