"""
Token estimation utilities
"""
from typing import Optional


def estimate_tokens(text: str, model: Optional[str] = None) -> int:
    """
    Estimate token count for text
    
    Simple estimation: ~4 characters per token for English text
    More accurate estimation would require actual tokenizer
    """
    # Simple estimation
    return len(text) // 4


def estimate_cost(
    prompt_tokens: int,
    completion_tokens: int,
    prompt_price_per_million: float,
    completion_price_per_million: float
) -> float:
    """Estimate cost based on token usage"""
    prompt_cost = (prompt_tokens / 1_000_000) * prompt_price_per_million
    completion_cost = (completion_tokens / 1_000_000) * completion_price_per_million
    return prompt_cost + completion_cost

