"""Plugin models"""
from app.models.plugins.web_plugin import WebPlugin
from app.models.plugins.pdf_plugin import PDFPlugin
from app.models.plugins.response_healing_plugin import ResponseHealingPlugin

__all__ = [
    "WebPlugin",
    "PDFPlugin",
    "ResponseHealingPlugin",
]
