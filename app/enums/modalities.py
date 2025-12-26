"""
Input and Output Modalities
"""
from enum import Enum


class InputModality(str, Enum):
    """Input modalities supported by OpenRouter"""
    TEXT = "text"
    IMAGE = "image"
    FILE = "file"
    AUDIO = "audio"
    VIDEO = "video"


class OutputModality(str, Enum):
    """Output modalities supported by OpenRouter"""
    TEXT = "text"
    IMAGE = "image"
    EMBEDDINGS = "embeddings"

