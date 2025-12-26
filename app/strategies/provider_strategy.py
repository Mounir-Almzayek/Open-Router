"""
Provider Selection Strategy
"""
from abc import ABC, abstractmethod
from typing import Optional
from app.models.requests import ProviderConfig


class ProviderStrategy(ABC):
    """Strategy for provider selection"""
    
    @abstractmethod
    def select_provider(self, model: str, config: Optional[ProviderConfig] = None) -> Optional[str]:
        """Select provider based on strategy"""
        pass


class PriceBasedStrategy(ProviderStrategy):
    """Price-based provider selection"""
    
    def select_provider(self, model: str, config: Optional[ProviderConfig] = None) -> Optional[str]:
        """Select provider based on price"""
        if config and config.sort:
            # OpenRouter handles sorting, we just return None to use default
            return None
        return None


class ThroughputBasedStrategy(ProviderStrategy):
    """Throughput-based provider selection"""
    
    def select_provider(self, model: str, config: Optional[ProviderConfig] = None) -> Optional[str]:
        """Select provider based on throughput"""
        if config:
            config.sort = "throughput"  # This will be handled by OpenRouter
        return None


class LatencyBasedStrategy(ProviderStrategy):
    """Latency-based provider selection"""
    
    def select_provider(self, model: str, config: Optional[ProviderConfig] = None) -> Optional[str]:
        """Select provider based on latency"""
        if config:
            config.sort = "latency"  # This will be handled by OpenRouter
        return None

