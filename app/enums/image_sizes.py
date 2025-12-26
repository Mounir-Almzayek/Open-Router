"""
Image Generation Sizes
"""
from enum import Enum


class ImageSize(str, Enum):
    """Image sizes for generation"""
    SIZE_1K = "1K"
    SIZE_2K = "2K"
    SIZE_4K = "4K"

