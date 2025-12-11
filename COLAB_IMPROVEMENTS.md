# Colab Notebook Improvements for Chatterbox TTS

This document outlines the recommended improvements to the `Chatterbox TTS.ipynb` notebook to address installation issues.

## Current Issues
The notebook currently installs dependencies in a single step which can fail due to Git-related issues with the `s3tokenizer` dependency.

## Recommended Improvements

### 1. Enhanced Installation Cell
Replace the current installation cell (Step 4) with a more robust version:

```python
### Step 4: Install Dependencies

Next, we install all the required libraries. We'll handle the `s3tokenizer` dependency separately to avoid Git clone issues, and install `pyngrok` as a fallback for sharing the Gradio app.

# First, install the problematic s3tokenizer dependency separately
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])

try:
    print("Installing s3tokenizer...")
    install_package("git+https://github.com/step-audio/s3tokenizer.git@88f2263")
    print("s3tokenizer installed successfully!")
except subprocess.CalledProcessError:
    print("Attempting alternative installation method for s3tokenizer...")
    # Alternative: install with no-deps first
    subprocess.check_call([sys.executable, "-m", "pip", "install", "git+https://github.com/step-audio/s3tokenizer.git@8f2263", "--no-deps", "--quiet"])
    # Then install torch separately
    subprocess.check_call([sys.executable, "-m", "pip", "install", "torch", "torchaudio", "--quiet"])
    print("s3tokenizer installed with alternative method!")

# Install other requirements
print("Installing other dependencies...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--quiet"])

# Install pyngrok
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyngrok", "--quiet"])

print("All dependencies installed successfully!")
```

### 2. Error Handling Cell
Add a troubleshooting cell after installation:

```python
### Troubleshooting

If you encounter any issues with the installation, try running this cell to diagnose the problem:

import sys
import subprocess

def check_installation():
    try:
        import s3tokenizer
        print("✓ s3tokenizer is installed")
    except ImportError:
        print("✗ s3tokenizer is not installed")
        
    try:
        import torch
        print("✓ torch is installed")
    except ImportError:
        print("✗ torch is not installed")
        
    try:
        import gradio
        print("✓ gradio is installed")
    except ImportError:
        print("✗ gradio is not installed")

check_installation()
```

### 3. Alternative Installation Cell
Add an alternative installation cell for users who continue to have issues:

```python
### Alternative Installation Method

If the standard installation fails, run this cell instead:

import os
import subprocess
import sys

# Clone s3tokenizer manually
if not os.path.exists("s3tokenizer"):
    subprocess.check_call(["git", "clone", "https://github.com/step-audio/s3tokenizer.git"])
    
os.chdir("s3tokenizer")
subprocess.check_call(["git", "checkout", "88f2263"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])
os.chdir("..")

# Install remaining requirements
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--quiet"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyngrok", "--quiet"])

print("Installation completed using alternative method!")
```

These improvements will make the Colab notebook more resilient to dependency installation issues.