"""
Chatterbox TTS - A high-quality text-to-speech system
"""

__version__ = "1.0.0"

from .tts import ChatterboxTTS
from .vc import ChatterboxVC

__all__ = ["ChatterboxTTS", "ChatterboxVC"]