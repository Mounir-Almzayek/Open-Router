"""
Client exceptions
"""
from typing import Optional


class ClientException(Exception):
    """Base client exception"""
    def __init__(self, message: str, status_code: Optional[int] = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class ConnectionError(ClientException):
    """Connection error"""
    pass


class TimeoutError(ClientException):
    """Timeout error"""
    pass


class FileProcessingError(ClientException):
    """File processing error"""
    pass


class ContentBuilderError(ClientException):
    """Content builder error"""
    pass

