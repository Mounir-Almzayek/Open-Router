"""
Routing Strategy
"""
from typing import List, Optional
from app.models.requests import ProviderConfig
from app.enums import ProviderSort


class RoutingStrategy:
    """Strategy for request routing"""
    
    @staticmethod
    def configure_for_price(config: Optional[ProviderConfig] = None) -> ProviderConfig:
        """Configure routing for lowest price"""
        if config is None:
            config = ProviderConfig()
        config.sort = ProviderSort.PRICE
        return config
    
    @staticmethod
    def configure_for_throughput(config: Optional[ProviderConfig] = None) -> ProviderConfig:
        """Configure routing for highest throughput"""
        if config is None:
            config = ProviderConfig()
        config.sort = ProviderSort.THROUGHPUT
        return config
    
    @staticmethod
    def configure_for_latency(config: Optional[ProviderConfig] = None) -> ProviderConfig:
        """Configure routing for lowest latency"""
        if config is None:
            config = ProviderConfig()
        config.sort = ProviderSort.LATENCY
        return config
    
    @staticmethod
    def configure_with_order(
        providers: List[str],
        allow_fallbacks: bool = True,
        config: Optional[ProviderConfig] = None
    ) -> ProviderConfig:
        """Configure routing with specific provider order"""
        if config is None:
            config = ProviderConfig()
        config.order = providers
        config.allow_fallbacks = allow_fallbacks
        return config

