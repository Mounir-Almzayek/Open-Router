"""
Metrics Collection
"""
from typing import Dict, Any
from app.config import settings


class MetricsCollector:
    """Metrics collector"""
    
    def __init__(self):
        self.metrics: Dict[str, Any] = {}
        self.enabled = settings.enable_metrics
    
    def increment(self, metric_name: str, value: int = 1, tags: Dict[str, str] = None):
        """Increment metric"""
        if not self.enabled:
            return
        
        key = self._build_key(metric_name, tags)
        if key not in self.metrics:
            self.metrics[key] = 0
        self.metrics[key] += value
    
    def set(self, metric_name: str, value: Any, tags: Dict[str, str] = None):
        """Set metric value"""
        if not self.enabled:
            return
        
        key = self._build_key(metric_name, tags)
        self.metrics[key] = value
    
    def get(self, metric_name: str, tags: Dict[str, str] = None) -> Any:
        """Get metric value"""
        key = self._build_key(metric_name, tags)
        return self.metrics.get(key, 0)
    
    def _build_key(self, metric_name: str, tags: Dict[str, str] = None) -> str:
        """Build metric key"""
        if tags:
            tag_str = ",".join(f"{k}={v}" for k, v in sorted(tags.items()))
            return f"{metric_name}[{tag_str}]"
        return metric_name
    
    def get_all_metrics(self) -> Dict[str, Any]:
        """Get all metrics"""
        return self.metrics.copy()


# Global metrics collector
metrics = MetricsCollector()

