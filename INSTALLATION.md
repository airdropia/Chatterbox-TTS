# Installation Guide for Chatterbox TTS Enhanced (Modified Version)

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Chatterbox-TTS-Modified.git
   cd Chatterbox-TTS-Modified
   ```

2. Run the setup script:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. Start the application:
   ```bash
   python app.py
   ```

## Manual Installation

If the setup script doesn't work, you can install manually:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create necessary directories:
   ```bash
   mkdir -p samples
   mkdir -p models
   ```

3. Start the application:
   ```bash
   python app.py
   ```

## Running on Google Colab

1. Open the notebook in Colab.
2. Run the installation cell:
   ```python
   !git clone https://github.com/your-username/Chatterbox-TTS-Modified.git
   %cd Chatterbox-TTS-Modified
   !pip install -r requirements.txt
   ```

3. Run the application:
   ```python
   !python app.py
   ```

## Troubleshooting

If you encounter any issues, please check the following:

1. Make sure you're using Python 3.8 or higher.
2. Ensure you have a compatible GPU (at least 5GB of VRAM).
3. Check that all dependencies are installed correctly.

For more information, please refer to the README.md file.