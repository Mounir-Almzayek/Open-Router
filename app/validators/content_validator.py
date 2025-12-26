"""
Content Validator
"""
from typing import List
from app.validators.base_validator import BaseValidator, ValidationResult
from app.models.base import BaseRequest
from app.models.requests.content import BaseContent


class ContentValidator(BaseValidator):
    """Validate content"""
    
    def validate(self, request: BaseRequest) -> ValidationResult:
        """Validate content in messages"""
        errors = []
        
        if hasattr(request, 'messages') and request.messages:
            for i, message in enumerate(request.messages):
                if hasattr(message, 'content'):
                    content = message.content
                    if isinstance(content, list):
                        for j, content_item in enumerate(content):
                            content_errors = self._validate_content_item(content_item, i, j)
                            errors.extend(content_errors)
                    elif isinstance(content, str):
                        # String content is valid
                        pass
                    else:
                        errors.append(f"Message {i}: Invalid content type")
        
        if errors:
            return ValidationResult(is_valid=False, errors=errors)
        
        return self._validate_next(request)
    
    def _validate_content_item(self, content_item: any, message_index: int, content_index: int) -> List[str]:
        """Validate individual content item"""
        errors = []
        
        if isinstance(content_item, BaseContent):
            if hasattr(content_item, 'type'):
                # Validate based on content type
                if hasattr(content_item, 'image_url'):
                    if not content_item.image_url or not content_item.image_url.url:
                        errors.append(f"Message {message_index}, Content {content_index}: Image URL is required")
                elif hasattr(content_item, 'video_url'):
                    if not content_item.video_url or not content_item.video_url.url:
                        errors.append(f"Message {message_index}, Content {content_index}: Video URL is required")
                elif hasattr(content_item, 'input_audio'):
                    if not content_item.input_audio or not content_item.input_audio.data:
                        errors.append(f"Message {message_index}, Content {content_index}: Audio data is required")
                elif hasattr(content_item, 'file'):
                    if not content_item.file or not content_item.file.file_data:
                        errors.append(f"Message {message_index}, Content {content_index}: File data is required")
                elif hasattr(content_item, 'text'):
                    if not content_item.text:
                        errors.append(f"Message {message_index}, Content {content_index}: Text content is required")
        
        return errors

