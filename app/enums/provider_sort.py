"""
Provider Sort Options
"""
from enum import Enum


class ProviderSort(str, Enum):
    """Provider sorting options"""
    PRICE = "price"
    THROUGHPUT = "throughput"
    LATENCY = "latency"

