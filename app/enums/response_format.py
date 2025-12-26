"""
Response Format Types
"""
from enum import Enum


class ResponseFormatType(str, Enum):
    """Response format types"""
    JSON_OBJECT = "json_object"
    JSON_SCHEMA = "json_schema"

