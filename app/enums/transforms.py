"""
Message Transform Types
"""
from enum import Enum


class TransformType(str, Enum):
    """Message transform types"""
    MIDDLE_OUT = "middle-out"

