"""
Retry Strategy
"""
from abc import ABC, abstractmethod
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class RetryStrategy(ABC):
    """Strategy for retry logic"""
    
    @abstractmethod
    def should_retry(self, attempt: int, error: Exception) -> bool:
        """Determine if should retry"""
        pass
    
    @abstractmethod
    def get_delay(self, attempt: int) -> float:
        """Get delay before retry"""
        pass


class ExponentialBackoffStrategy(RetryStrategy):
    """Exponential backoff retry strategy"""
    
    def should_retry(self, attempt: int, error: Exception) -> bool:
        """Determine if should retry based on error type"""
        # Retry on network errors, timeouts, and rate limits
        retryable_errors = (
            TimeoutError,
            ConnectionError,
            OSError,
        )
        
        # Check error type
        if isinstance(error, retryable_errors):
            return attempt < 3
        
        # Check for rate limit errors (429)
        if hasattr(error, 'status_code') and error.status_code == 429:
            return attempt < 5
        
        return False
    
    def get_delay(self, attempt: int) -> float:
        """Get exponential backoff delay"""
        return 2 ** attempt


class LinearBackoffStrategy(RetryStrategy):
    """Linear backoff retry strategy"""
    
    def __init__(self, base_delay: float = 1.0):
        self.base_delay = base_delay
    
    def should_retry(self, attempt: int, error: Exception) -> bool:
        """Determine if should retry"""
        return attempt < 3
    
    def get_delay(self, attempt: int) -> float:
        """Get linear delay"""
        return self.base_delay * attempt


class NoRetryStrategy(RetryStrategy):
    """No retry strategy"""
    
    def should_retry(self, attempt: int, error: Exception) -> bool:
        """Never retry"""
        return False
    
    def get_delay(self, attempt: int) -> float:
        """No delay"""
        return 0.0

