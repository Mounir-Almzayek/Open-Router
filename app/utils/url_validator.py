"""
URL validators
"""
from urllib.parse import urlparse
from typing import Optional


def is_valid_url(url: str) -> bool:
    """Validate URL format"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def is_data_url(url: str) -> bool:
    """Check if string is a data URL"""
    return url.startswith("data:")


def is_base64_string(string: str) -> bool:
    """Check if string is base64 encoded"""
    try:
        import base64
        # Remove data URL prefix if present
        if string.startswith("data:"):
            string = string.split(",", 1)[1]
        base64.b64decode(string, validate=True)
        return True
    except Exception:
        return False

