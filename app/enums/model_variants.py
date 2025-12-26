"""
Model Variants
"""
from enum import Enum


class ModelVariant(str, Enum):
    """Model variant suffixes"""
    FREE = ":free"
    EXTENDED = ":extended"
    EXACTO = ":exacto"
    THINKING = ":thinking"
    ONLINE = ":online"
    NITRO = ":nitro"
    FLOOR = ":floor"

