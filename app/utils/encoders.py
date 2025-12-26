"""
Base64 encoders/decoders
"""
import base64
from typing import Optional


def encode_to_base64(data: bytes) -> str:
    """Encode bytes to base64 string"""
    return base64.b64encode(data).decode('utf-8')


def decode_from_base64(base64_string: str) -> bytes:
    """Decode base64 string to bytes"""
    # Remove data URL prefix if present
    if base64_string.startswith("data:"):
        base64_string = base64_string.split(",", 1)[1]
    return base64.b64decode(base64_string)


def create_data_url(data: bytes, mime_type: str) -> str:
    """Create data URL from bytes and MIME type"""
    base64_data = encode_to_base64(data)
    return f"data:{mime_type};base64,{base64_data}"

