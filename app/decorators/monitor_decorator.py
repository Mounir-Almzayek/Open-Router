"""
Monitoring decorator
"""
import time
from functools import wraps
from typing import Callable, TypeVar
from app.config import settings

T = TypeVar('T')


def monitor_performance(func: Callable) -> Callable:
    """Monitor performance decorator"""
    @wraps(func)
    async def wrapper(*args, **kwargs) -> T:
        if not settings.enable_metrics:
            return await func(*args, **kwargs)
        
        start_time = time.time()
        func_name = func.__name__
        
        try:
            result = await func(*args, **kwargs)
            duration = time.time() - start_time
            
            # Here you would send metrics to monitoring system
            # For now, just log
            if duration > 1.0:  # Log slow requests
                import logging
                logger = logging.getLogger(__name__)
                logger.warning(f"Slow request: {func_name} took {duration:.3f}s")
            
            return result
        except Exception as e:
            duration = time.time() - start_time
            # Log error metrics
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error in {func_name} after {duration:.3f}s: {e}")
            raise
    
    return wrapper

