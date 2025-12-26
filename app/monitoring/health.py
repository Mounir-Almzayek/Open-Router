"""
Health Checks
"""
from typing import Dict, Any
from app.services import OpenRouterClient
from app.config import settings


class HealthChecker:
    """Health checker"""
    
    async def check_openrouter(self, client: OpenRouterClient) -> Dict[str, Any]:
        """Check OpenRouter connectivity"""
        try:
            await client.list_models()
            return {"status": "healthy", "service": "openrouter"}
        except Exception as e:
            return {"status": "unhealthy", "service": "openrouter", "error": str(e)}
    
    async def check_all(self, client: OpenRouterClient) -> Dict[str, Any]:
        """Check all services"""
        checks = {
            "app": {
                "status": "healthy",
                "name": settings.app_name,
                "version": settings.app_version
            },
            "openrouter": await self.check_openrouter(client)
        }
        
        all_healthy = all(
            check.get("status") == "healthy"
            for check in checks.values()
        )
        
        return {
            "status": "healthy" if all_healthy else "degraded",
            "checks": checks
        }


# Global health checker
health_checker = HealthChecker()

