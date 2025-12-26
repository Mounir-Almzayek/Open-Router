"""
Cache TTL Options
"""
from enum import Enum


class CacheTTL(str, Enum):
    """Cache time-to-live options"""
    FIVE_MINUTES = "5m"
    ONE_HOUR = "1h"

