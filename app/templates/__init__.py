"""Prompt templates"""
from app.templates.base import BaseTemplate
from app.templates.text_template import TextTemplate
from app.templates.image_template import ImageTemplate
from app.templates.audio_template import AudioTemplate
from app.templates.video_template import VideoTemplate
from app.templates.file_template import FileTemplate

__all__ = [
    "BaseTemplate",
    "TextTemplate",
    "ImageTemplate",
    "AudioTemplate",
    "VideoTemplate",
    "FileTemplate",
]
