"""
Finish Reasons
"""
from enum import Enum


class FinishReason(str, Enum):
    """Finish reasons for completions"""
    STOP = "stop"
    LENGTH = "length"
    TOOL_CALLS = "tool_calls"
    CONTENT_FILTER = "content_filter"
    ERROR = "error"

