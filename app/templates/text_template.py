"""
Text-only Templates
"""
from typing import Dict, Any
from app.templates.base import BaseTemplate
from app.models.requests import ChatRequest
from app.builders import ChatRequestBuilder
from app.enums import MessageRole


class TextTemplate(BaseTemplate):
    """Text-only template"""
    
    def render(self, variables: Dict[str, Any]) -> str:
        """Render template with variables"""
        rendered = self.prompt
        for key, value in variables.items():
            placeholder = f"{{{key}}}"
            rendered = rendered.replace(placeholder, str(value))
        return rendered
    
    def create_request(
        self,
        model: str,
        user_input: Dict[str, Any],
        **kwargs
    ) -> ChatRequest:
        """Create request from template"""
        rendered_prompt = self.merge_with_user_input(user_input)
        
        builder = ChatRequestBuilder()
        builder.with_model(model)
        builder.with_system_prompt(rendered_prompt)
        
        # Add user text if provided
        if "text" in user_input:
            builder.with_text(user_input["text"])
        
        # Apply kwargs
        for key, value in kwargs.items():
            if hasattr(builder, f"with_{key}"):
                getattr(builder, f"with_{key}")(value)
        
        return builder.build()

