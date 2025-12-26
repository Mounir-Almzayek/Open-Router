"""
Timeout decorator
"""
import asyncio
from functools import wraps
from typing import Callable, TypeVar, Optional
from app.config import settings

T = TypeVar('T')


def timeout(seconds: Optional[float] = None):
    """Timeout decorator for async functions"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> T:
            timeout_seconds = seconds or settings.openrouter_timeout
            
            try:
                return await asyncio.wait_for(
                    func(*args, **kwargs),
                    timeout=timeout_seconds
                )
            except asyncio.TimeoutError:
                raise TimeoutError(f"Function {func.__name__} exceeded timeout of {timeout_seconds}s")
        
        return wrapper
    return decorator

