"""
PDF Processing Engines
"""
from enum import Enum


class PDFEngine(str, Enum):
    """PDF processing engines"""
    MISTRAL_OCR = "mistral-ocr"
    PDF_TEXT = "pdf-text"
    NATIVE = "native"

