"""
Reasoning Effort Levels
"""
from enum import Enum


class ReasoningEffort(str, Enum):
    """Reasoning effort levels"""
    XHIGH = "xhigh"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    MINIMAL = "minimal"
    NONE = "none"

