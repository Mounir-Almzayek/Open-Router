"""
Video Formats
"""
from enum import Enum


class VideoFormat(str, Enum):
    """Supported video formats"""
    MP4 = "mp4"
    MPEG = "mpeg"
    MOV = "mov"
    WEBM = "webm"

