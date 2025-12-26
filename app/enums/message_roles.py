"""
Message Roles
"""
from enum import Enum


class MessageRole(str, Enum):
    """Roles in conversation messages"""
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"

