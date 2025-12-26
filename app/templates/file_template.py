"""
File Processing Templates
"""
from typing import Dict, Any
from app.templates.base import BaseTemplate
from app.models.requests import ChatRequest
from app.builders import ChatRequestBuilder, ContentBuilder
from app.enums import MessageRole


class FileTemplate(BaseTemplate):
    """File processing template (PDF, etc.)"""
    
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
        
        # Enable PDF processing if needed
        if "enable_pdf_processing" in user_input and user_input["enable_pdf_processing"]:
            from app.enums import PDFEngine
            builder.with_pdf_processing(PDFEngine.MISTRAL_OCR)
        
        # Add file
        if "file" in user_input:
            file_content = ContentBuilder.from_url(user_input["file"], "file")
            builder.with_message(MessageRole.USER, [file_content])
        elif "file_base64" in user_input:
            file_content = ContentBuilder.from_base64_string(
                user_input["file_base64"],
                "file",
                user_input.get("mime_type", "application/pdf")
            )
            builder.with_message(MessageRole.USER, [file_content])
        
        # Add text if provided
        if "text" in user_input:
            from app.models.requests.content import TextContent
            text_content = TextContent(text=user_input["text"])
            if builder._request.messages:
                last_message = builder._request.messages[-1]
                if isinstance(last_message.content, list):
                    last_message.content.insert(0, text_content)
                else:
                    last_message.content = [text_content, last_message.content]
        
        # Apply kwargs
        for key, value in kwargs.items():
            if hasattr(builder, f"with_{key}"):
                getattr(builder, f"with_{key}")(value)
        
        return builder.build()

