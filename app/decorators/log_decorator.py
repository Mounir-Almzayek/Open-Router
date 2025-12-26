"""
Logging decorator
"""
import logging
import time
from functools import wraps
from typing import Callable, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar('T')


def log_request(func: Callable) -> Callable:
    """Log request decorator"""
    @wraps(func)
    async def wrapper(*args, **kwargs) -> T:
        start_time = time.time()
        func_name = func.__name__
        
        logger.info(f"Starting {func_name}", extra={"func_args": str(args), "func_kwargs": str(kwargs)})
        
        try:
            result = await func(*args, **kwargs)
            duration = time.time() - start_time
            logger.info(f"Completed {func_name} in {duration:.3f}s")
            return result
        except Exception as e:
            duration = time.time() - start_time
            logger.error(f"Failed {func_name} after {duration:.3f}s: {e}", exc_info=True)
            raise
    
    return wrapper

