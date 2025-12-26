"""
Template Management Service
"""
from typing import Dict, Optional
from app.templates import BaseTemplate, TextTemplate, ImageTemplate, AudioTemplate, VideoTemplate, FileTemplate
from app.models.requests import ChatRequest


class TemplateService:
    """Template management service"""
    
    def __init__(self):
        self.templates: Dict[str, BaseTemplate] = {}
    
    def register_template(self, template: BaseTemplate) -> None:
        """Register a template"""
        self.templates[template.template_id] = template
    
    def get_template(self, template_id: str) -> Optional[BaseTemplate]:
        """Get template by ID"""
        return self.templates.get(template_id)
    
    def create_request_from_template(
        self,
        template_id: str,
        model: str,
        user_input: Dict,
        **kwargs
    ) -> ChatRequest:
        """Create request from template"""
        template = self.get_template(template_id)
        if not template:
            raise ValueError(f"Template not found: {template_id}")
        
        return template.create_request(model, user_input, **kwargs)
    
    def create_text_template(self, template_id: str, prompt: str) -> TextTemplate:
        """Create and register text template"""
        template = TextTemplate(template_id, prompt)
        self.register_template(template)
        return template
    
    def create_image_template(self, template_id: str, prompt: str) -> ImageTemplate:
        """Create and register image template"""
        template = ImageTemplate(template_id, prompt)
        self.register_template(template)
        return template
    
    def create_audio_template(self, template_id: str, prompt: str) -> AudioTemplate:
        """Create and register audio template"""
        template = AudioTemplate(template_id, prompt)
        self.register_template(template)
        return template
    
    def create_video_template(self, template_id: str, prompt: str) -> VideoTemplate:
        """Create and register video template"""
        template = VideoTemplate(template_id, prompt)
        self.register_template(template)
        return template
    
    def create_file_template(self, template_id: str, prompt: str) -> FileTemplate:
        """Create and register file template"""
        template = FileTemplate(template_id, prompt)
        self.register_template(template)
        return template

