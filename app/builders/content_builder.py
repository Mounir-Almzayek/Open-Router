"""
Content Builder
"""
from fastapi import UploadFile
from typing import Optional, Union
from app.models.requests.content import (
    TextContent,
    ImageContent,
    ImageURL,
    VideoContent,
    VideoURL,
    AudioContent,
    InputAudio,
    FileContent,
    FileData,
    CacheControl
)
from app.enums import ContentType, AudioFormat, CacheControlType, CacheTTL
from app.utils.file_handler import DirectFileHandler
from app.utils.url_validator import is_valid_url, is_data_url


class ContentBuilder:
    """Builder لإنشاء content objects من FastAPI request parameters"""
    
    @staticmethod
    async def from_upload_file(
        file: UploadFile,
        content_type: str  # "image", "video", "audio", "file"
    ) -> Union[ImageContent, VideoContent, AudioContent, FileContent]:
        """إنشاء content من UploadFile مباشرة"""
        handler = DirectFileHandler()
        
        if content_type == "image":
            data_url = await handler.process_image_upload(file)
            return ImageContent(image_url=ImageURL(url=data_url))
        
        elif content_type == "video":
            data_url = await handler.process_video_upload(file)
            return VideoContent(video_url=VideoURL(url=data_url))
        
        elif content_type == "audio":
            base64_data, audio_format = await handler.process_audio_upload(file)
            return AudioContent(
                input_audio=InputAudio(data=base64_data, format=AudioFormat(audio_format))
            )
        
        elif content_type == "file":
            data_url = await handler.process_pdf_upload(file)
            return FileContent(
                file=FileData(
                    filename=file.filename or "file",
                    file_data=data_url
                )
            )
        
        else:
            raise ValueError(f"Unsupported content type: {content_type}")
    
    @staticmethod
    def from_base64_string(
        base64_string: str,
        content_type: str,
        mime_type: Optional[str] = None
    ) -> Union[ImageContent, VideoContent, AudioContent, FileContent]:
        """إنشاء content من base64 string في JSON body"""
        handler = DirectFileHandler()
        data_url = handler.process_base64_string(base64_string, mime_type)
        
        if content_type == "image":
            return ImageContent(image_url=ImageURL(url=data_url))
        elif content_type == "video":
            return VideoContent(video_url=VideoURL(url=data_url))
        elif content_type == "file":
            return FileContent(
                file=FileData(filename="file", file_data=data_url)
            )
        else:
            raise ValueError(f"Unsupported content type: {content_type}")
    
    @staticmethod
    def from_url(url: str, content_type: str) -> Union[ImageContent, VideoContent, FileContent]:
        """إنشاء content من URL"""
        if not is_valid_url(url):
            raise ValueError(f"Invalid URL: {url}")
        
        if content_type == "image":
            return ImageContent(image_url=ImageURL(url=url))
        elif content_type == "video":
            return VideoContent(video_url=VideoURL(url=url))
        elif content_type == "file":
            return FileContent(file=FileData(filename="file", file_data=url))
        else:
            raise ValueError(f"Unsupported content type: {content_type}")
    
    @staticmethod
    def create_text_with_cache(text: str, ttl: Optional[CacheTTL] = None) -> TextContent:
        """Create text content with cache control"""
        cache_control = None
        if ttl:
            cache_control = CacheControl(type=CacheControlType.EPHEMERAL, ttl=ttl)
        return TextContent(text=text, cache_control=cache_control)

