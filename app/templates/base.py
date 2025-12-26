"""
Base Template Class
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from app.models.requests import ChatRequest


class BaseTemplate(ABC):
    """Base template class"""
    
    def __init__(self, template_id: str, prompt: str):
        self.template_id = template_id
        self.prompt = prompt
    
    @abstractmethod
    def render(self, variables: Dict[str, Any]) -> str:
        """Render template with variables"""
        pass
    
    @abstractmethod
    def create_request(
        self,
        model: str,
        user_input: Dict[str, Any],
        **kwargs
    ) -> ChatRequest:
        """Create request from template"""
        pass
    
    def merge_with_user_input(
        self,
        user_input: Dict[str, Any]
    ) -> str:
        """Merge template prompt with user input"""
        rendered = self.render(user_input)
        return rendered

