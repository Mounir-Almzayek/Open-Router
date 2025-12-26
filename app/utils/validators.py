"""
Input validators
"""
from typing import List, Optional
from app.enums import AudioFormat, VideoFormat, ImageFormat


def validate_audio_format(format_str: str) -> bool:
    """Validate audio format"""
    try:
        AudioFormat(format_str)
        return True
    except ValueError:
        return False


def validate_video_format(format_str: str) -> bool:
    """Validate video format"""
    try:
        VideoFormat(format_str)
        return True
    except ValueError:
        return False


def validate_image_format(format_str: str) -> bool:
    """Validate image format"""
    try:
        ImageFormat(format_str)
        return True
    except ValueError:
        return False

