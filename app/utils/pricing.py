"""
Pricing calculator
"""
from typing import Optional, Dict, Any
from app.models.responses import Usage


class PricingCalculator:
    """Calculate costs based on usage"""
    
    # Example pricing (should be fetched from Models API)
    MODEL_PRICING: Dict[str, Dict[str, float]] = {
        "openai/gpt-4o": {
            "prompt": 2.50,
            "completion": 10.00
        },
        "anthropic/claude-sonnet-4": {
            "prompt": 3.00,
            "completion": 15.00
        }
    }
    
    @classmethod
    def calculate_cost(
        cls,
        usage: Usage,
        model: str
    ) -> float:
        """Calculate cost based on usage and model"""
        pricing = cls.MODEL_PRICING.get(model, {})
        prompt_price = pricing.get("prompt", 0.0)
        completion_price = pricing.get("completion", 0.0)
        
        prompt_tokens = usage.prompt_tokens or 0
        completion_tokens = usage.completion_tokens or 0
        
        prompt_cost = (prompt_tokens / 1_000_000) * prompt_price
        completion_cost = (completion_tokens / 1_000_000) * completion_price
        
        return prompt_cost + completion_cost

