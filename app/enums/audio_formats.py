"""
Audio Formats
"""
from enum import Enum


class AudioFormat(str, Enum):
    """Supported audio formats"""
    WAV = "wav"
    MP3 = "mp3"
    AIFF = "aiff"
    AAC = "aac"
    OGG = "ogg"
    FLAC = "flac"
    M4A = "m4a"
    PCM16 = "pcm16"
    PCM24 = "pcm24"

