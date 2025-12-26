"""
Retry decorator
"""
import asyncio
import logging
from functools import wraps
from typing import Callable, TypeVar, Optional
from app.strategies.retry_strategy import RetryStrategy, ExponentialBackoffStrategy

logger = logging.getLogger(__name__)

T = TypeVar('T')


def retry_on_failure(
    max_attempts: int = 3,
    strategy: Optional[RetryStrategy] = None
):
    """Retry decorator for async functions"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> T:
            strategy_instance = strategy or ExponentialBackoffStrategy()
            
            for attempt in range(1, max_attempts + 1):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if not strategy_instance.should_retry(attempt, e):
                        logger.error(f"Retry failed after {attempt} attempts: {e}")
                        raise
                    
                    delay = strategy_instance.get_delay(attempt)
                    logger.warning(f"Attempt {attempt} failed, retrying in {delay}s: {e}")
                    await asyncio.sleep(delay)
            
            raise Exception(f"Max retries ({max_attempts}) exceeded")
        
        return wrapper
    return decorator

