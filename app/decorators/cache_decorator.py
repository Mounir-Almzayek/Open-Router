"""
Cache decorator
"""
import time
import hashlib
import json
from functools import wraps
from typing import Callable, TypeVar, Any, Dict

T = TypeVar('T')


def cache_result(ttl: int = 300):
    """Cache result decorator for async functions"""
    cache: Dict[str, tuple[Any, float]] = {}
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> T:
            # Create cache key
            key_data = {
                "args": str(args),
                "kwargs": json.dumps(kwargs, sort_keys=True, default=str)
            }
            key_string = json.dumps(key_data, sort_keys=True)
            key = hashlib.md5(key_string.encode()).hexdigest()
            
            # Check cache
            if key in cache:
                result, timestamp = cache[key]
                if time.time() - timestamp < ttl:
                    return result
                else:
                    del cache[key]
            
            # Execute function
            result = await func(*args, **kwargs)
            
            # Store in cache
            cache[key] = (result, time.time())
            
            return result
        
        return wrapper
    return decorator

