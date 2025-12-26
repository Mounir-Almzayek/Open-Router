"""
Data Collection Policies
"""
from enum import Enum


class DataCollection(str, Enum):
    """Data collection policy options"""
    ALLOW = "allow"
    DENY = "deny"

