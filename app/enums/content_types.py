"""
Content Types for messages
"""
from enum import Enum


class ContentType(str, Enum):
    """Content types in message content array"""
    TEXT = "text"
    IMAGE_URL = "image_url"
    INPUT_AUDIO = "input_audio"
    VIDEO_URL = "video_url"
    FILE = "file"

