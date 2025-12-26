"""API routes"""
from app.routers.chat import router as chat_router
from app.routers.multimodal import router as multimodal_router
from app.routers.models import router as models_router
from app.routers.health import router as health_router
from app.routers.translation import router as translation_router

__all__ = [
    "chat_router",
    "multimodal_router",
    "models_router",
    "health_router",
    "translation_router",
]
