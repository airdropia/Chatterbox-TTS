# Chatterbox TTS Enhanced

A high-quality, open-source voice cloning, text-to-speech, and voice conversion application.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/airdropia/Chatterbox-TTS/blob/master/Chatterbox%20TTS.ipynb)

## Features

- **Text-to-Speech (TTS):** Convert text into high-quality speech using a variety of pre-defined and custom voices.
- **Multilingual TTS:** Generate speech in multiple languages.
- **Voice Conversion (VC):** Transform your voice into someone else's.
- **Voice Cloning:** Clone a new voice from just a few seconds of audio.

## How to Run on Google Colab

1. Click the "Open in Colab" badge above.
2. In the Colab notebook, run the cells one by one.
3. A public Gradio URL will be generated. Click on it to open the application in your browser.

## Installation Troubleshooting

If you encounter issues with the `s3tokenizer` dependency during installation, especially in Google Colab, try the following approach:

### For Google Colab Environment
If running the notebook directly in Colab fails due to Git clone errors, manually install the dependencies in this order:
1. First install the problematic dependency separately: `!pip install git+https://github.com/step-audio/s3tokenizer.git@88f2263 --quiet`
2. Then install the remaining requirements: `!pip install -r requirements.txt --quiet`
3. Finally, run the application: `!python app.py`

### Alternative Installation Methods
If the standard installation fails, you can also try one of these approaches:
1. **Install with no dependencies first**: `pip install git+https://github.com/step-audio/s3tokenizer.git@88f2263 --no-deps --quiet`, then install other requirements separately
2. **Manual cloning**: Clone the s3tokenizer repository manually, checkout the specific commit (88f2263), and install it locally with `pip install -e .`
