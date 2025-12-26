"""
File upload/encoding utilities for direct handling from FastAPI requests
"""
from fastapi import UploadFile
from typing import Optional, Tuple
import base64
import mimetypes
from app.config import settings


class DirectFileHandler:
    """Handler للتعامل مع الملفات مباشرة من FastAPI request"""
    
    @staticmethod
    async def process_upload_file(
        file: UploadFile,
        max_size: int = None
    ) -> Tuple[bytes, str, str]:
        """
        معالجة UploadFile مباشرة وإرجاع (content, mime_type, filename)
        بدون حفظ على القرص
        """
        if max_size is None:
            max_size = settings.max_file_size
        
        # قراءة الملف مباشرة في الذاكرة
        content = await file.read()
        
        # التحقق من الحجم
        if len(content) > max_size:
            raise ValueError(f"File size exceeds maximum {max_size} bytes")
        
        # تحديد MIME type
        mime_type = file.content_type or mimetypes.guess_type(file.filename or "")[0] or "application/octet-stream"
        
        return content, mime_type, file.filename or "file"
    
    @staticmethod
    def encode_to_base64(content: bytes, mime_type: str) -> str:
        """تحويل content إلى base64 data URL"""
        base64_data = base64.b64encode(content).decode('utf-8')
        return f"data:{mime_type};base64,{base64_data}"
    
    @staticmethod
    async def process_image_upload(
        file: UploadFile
    ) -> str:
        """معالجة صورة وإرجاع base64 data URL"""
        content, mime_type, _ = await DirectFileHandler.process_upload_file(file)
        return DirectFileHandler.encode_to_base64(content, mime_type)
    
    @staticmethod
    async def process_video_upload(
        file: UploadFile
    ) -> str:
        """معالجة فيديو وإرجاع base64 data URL"""
        content, mime_type, _ = await DirectFileHandler.process_upload_file(
            file, 
            max_size=settings.max_video_size
        )
        return DirectFileHandler.encode_to_base64(content, mime_type)
    
    @staticmethod
    async def process_audio_upload(
        file: UploadFile
    ) -> Tuple[str, str]:
        """معالجة صوت وإرجاع (base64_data, format)"""
        content, mime_type, _ = await DirectFileHandler.process_upload_file(file)
        
        # تحديد format من MIME type
        format_map = {
            "audio/wav": "wav",
            "audio/mpeg": "mp3",
            "audio/mp3": "mp3",
            "audio/aiff": "aiff",
            "audio/aac": "aac",
            "audio/ogg": "ogg",
            "audio/flac": "flac",
            "audio/m4a": "m4a",
        }
        audio_format = format_map.get(mime_type, "wav")
        
        base64_data = base64.b64encode(content).decode('utf-8')
        return base64_data, audio_format
    
    @staticmethod
    async def process_pdf_upload(
        file: UploadFile
    ) -> str:
        """معالجة PDF وإرجاع base64 data URL"""
        content, mime_type, filename = await DirectFileHandler.process_upload_file(file)
        return DirectFileHandler.encode_to_base64(content, mime_type)
    
    @staticmethod
    def process_base64_string(
        base64_string: str,
        mime_type: Optional[str] = None
    ) -> str:
        """معالجة base64 string موجود في JSON body"""
        # إذا كان data URL كامل
        if base64_string.startswith("data:"):
            return base64_string
        
        # إذا كان base64 فقط، إضافة data URL prefix
        if mime_type:
            return f"data:{mime_type};base64,{base64_string}"
        
        # محاولة تخمين MIME type
        return f"data:application/octet-stream;base64,{base64_string}"

