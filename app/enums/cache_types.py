"""
Cache Control Types
"""
from enum import Enum


class CacheControlType(str, Enum):
    """Cache control types"""
    EPHEMERAL = "ephemeral"

