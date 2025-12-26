"""
Plugin Types
"""
from enum import Enum


class PluginType(str, Enum):
    """Available plugin types"""
    WEB = "web"
    FILE_PARSER = "file-parser"
    RESPONSE_HEALING = "response-healing"

