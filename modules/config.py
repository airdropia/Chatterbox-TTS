import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from chatterbox.mtl_tts import SUPPORTED_LANGUAGES

# Language configuration
LANGUAGE_CONFIG = {
    "en": {
        "name": "English",
        "voice_samples": [
            "samples/en_sample_1.wav",
            "samples/en_sample_2.wav",
            "samples/en_sample_3.wav"
        ]
    },
    "es": {
        "name": "Spanish",
        "voice_samples": [
            "samples/es_sample_1.wav",
            "samples/es_sample_2.wav",
            "samples/es_sample_3.wav"
        ]
    },
    "fr": {
        "name": "French",
        "voice_samples": [
            "samples/fr_sample_1.wav",
            "samples/fr_sample_2.wav",
            "samples/fr_sample_3.wav"
        ]
    },
    "de": {
        "name": "German",
        "voice_samples": [
            "samples/de_sample_1.wav",
            "samples/de_sample_2.wav",
            "samples/de_sample_3.wav"
        ]
    },
    "it": {
        "name": "Italian",
        "voice_samples": [
            "samples/it_sample_1.wav",
            "samples/it_sample_2.wav",
            "samples/it_sample_3.wav"
        ]
    },
    "pt": {
        "name": "Portuguese",
        "voice_samples": [
            "samples/pt_sample_1.wav",
            "samples/pt_sample_2.wav",
            "samples/pt_sample_3.wav"
        ]
    },
    "zh": {
        "name": "Chinese",
        "voice_samples": [
            "samples/zh_sample_1.wav",
            "samples/zh_sample_2.wav",
            "samples/zh_sample_3.wav"
        ]
    },
    "ja": {
        "name": "Japanese",
        "voice_samples": [
            "samples/ja_sample_1.wav",
            "samples/ja_sample_2.wav",
            "samples/ja_sample_3.wav"
        ]
    }
}
