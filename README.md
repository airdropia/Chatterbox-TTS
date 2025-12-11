<div align="center">

# Chatterbox TTS Enhanced (Modified Version)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/airdropia/Chatterbox-TTS/blob/main/Chatterbox%20TS.ipynb)

A high-quality, open-source voice cloning, text-to-speech, and voice conversion application.

This is a modified version of the original repository that addresses installation and compatibility issues.
</div>

## Features

- **Text-to-Speech (TTS):** Convert text into high-quality speech using a variety of pre-defined and custom voices.
- **Multilingual TTS:** Generate speech in multiple languages.
- **Voice Conversion (VC):** Transform your voice into someone else's.
- **Voice Cloning:** Clone a new voice from just a few seconds of audio.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/airdropia/Chatterbox-TTS.git
   cd Chatterbox-TTS
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## Modifications

This modified version includes the following fixes and improvements:

1. **Compatible Dependencies:** Updated `requirements.txt` with compatible versions of PyTorch and related libraries.

2. **Fixed Import Paths:** Modified import paths to ensure all modules can be found correctly.

3. **Included s3tokenizer:** Added a complete local copy of the s3tokenizer module to avoid external dependency issues.

4. **Simplified Implementation:** Created simplified implementations of some components to ensure stability.

## How to Run on Google Colab

1. Open the notebook in Colab.
2. Run the cells one by one.
3. A public Gradio URL will be generated. Click on it to open the application in your browser.

## Troubleshooting

If you encounter any issues, please check the following:

1. Ensure you have a compatible GPU (at least 5GB of VRAM).
2. Make sure all dependencies are installed correctly.
3. Check that you're using the correct Python version (3.8+ recommended).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
