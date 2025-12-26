"""
Usage Analyzer
"""
from typing import Optional
from app.models.responses import Usage
from app.utils.pricing import PricingCalculator
from app.utils.tokenizer import estimate_tokens


class UsageAnalyzer(BaseResponseProcessor):
    """Analyze usage and costs"""
    
    def calculate_cost(self, usage: Usage, model: str) -> float:
        """Calculate cost based on usage"""
        return PricingCalculator.calculate_cost(usage, model)
    
    def estimate_tokens(self, text: str) -> int:
        """Estimate token count"""
        return estimate_tokens(text)
    
    def analyze_usage(self, usage: Usage) -> dict:
        """Analyze usage statistics"""
        return {
            "prompt_tokens": usage.prompt_tokens or 0,
            "completion_tokens": usage.completion_tokens or 0,
            "total_tokens": usage.total_tokens or 0,
            "cache_read_tokens": usage.cache_read_tokens or 0,
            "cache_write_tokens": usage.cache_write_tokens or 0,
            "reasoning_tokens": usage.reasoning_tokens or 0,
            "cache_savings": self._calculate_cache_savings(usage)
        }
    
    def _calculate_cache_savings(self, usage: Usage) -> float:
        """Calculate cache savings percentage"""
        if not usage.cache_read_tokens or not usage.total_tokens:
            return 0.0
        return (usage.cache_read_tokens / usage.total_tokens) * 100
    
    def process(self, response) -> dict:
        """Process response and analyze usage"""
        if not hasattr(response, 'usage') or not response.usage:
            return {}
        return self.analyze_usage(response.usage)

