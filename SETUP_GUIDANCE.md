# Setup Configuration Guidance for Chatterbox TTS

This document provides guidance on how to configure the project's setup files to better handle Git dependencies like `s3tokenizer`.

## Recommended Changes to setup.py or pyproject.toml

### Option 1: Using pyproject.toml (Recommended)

Create or update the `pyproject.toml` file with the following content:

```toml
[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "chatterbox-tts"
version = "1.0.0"
description = "A high-quality, open-source voice cloning, text-to-speech, and voice conversion application"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "numpy==1.26.0",
    "librosa==0.1.0",
    "torch==2.3.1",
    "torchaudio==2.3.1",
    "transformers==4.46.3",
    "diffusers==0.29.0",
    "resemble-perth==1.0.1",
    "conformer==0.3.2",
    "safetensors==0.5.3",
    "pykakasi==2.3.0",
    "gradio==4.39.0",
    "unidecode==1.3.8",
    # Note: s3tokenizer is handled separately due to Git dependency
]

[project.optional-dependencies]
s3tokenizer = [
    "s3tokenizer @ git+https://github.com/step-audio/s3tokenizer.git@88f2263"
]

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools.package-dir]
"" = "src"
```

### Option 2: Using setup.py

If using setup.py instead of pyproject.toml, use this configuration:

```python
from setuptools import setup, find_packages

setup(
    name="chatterbox-tts",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy==1.26.0",
        "librosa==0.11.0",
        "torch==2.3.1",
        "torchaudio==2.3.1",
        "transformers==4.46.3",
        "diffusers==0.29.0",
        "resemble-perth==1.0.1",
        "conformer==0.3.2",
        "safetensors==0.5.3",
        "pykakasi==2.3.0",
        "gradio==4.39.0",
        "unidecode==1.3.8",
    ],
    extras_require={
        "s3tokenizer": ["s3tokenizer @ git+https://github.com/step-audio/s3tokenizer.git@88f2263"],
    },
    python_requires=">=3.10",
    description="A high-quality, open-source voice cloning, text-to-speech, and voice conversion application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
```

## Why This Approach Improves Dependency Management

1. **Separation of Concerns**: The s3tokenizer dependency is treated as an optional extra, allowing users to install the base package without Git complications.

2. **Explicit Git Dependency**: Using the `@ git+URL` syntax makes the Git dependency explicit and easier to manage.

3. **Installation Options**: Users can choose to install with or without the Git dependency:
   - `pip install .` - installs base package without Git dependencies
   - `pip install .[s3tokenizer]` - installs with s3tokenizer from Git

4. **Better Error Handling**: When the optional dependency fails, the base package is still installed, allowing for fallback options.

## Alternative: Submodule Approach

For even better Git integration, consider using s3tokenizer as a Git submodule:

1. Add s3tokenizer as a submodule: `git submodule add https://github.com/step-audio/s3tokenizer.git src/chatterbox/models/s3tokenizer_repo`
2. Update the Python import paths to use the submodule instead of the package dependency
3. This eliminates the runtime Git clone requirement entirely

This approach would require modifying the import statements in:
- `src/chatterbox/tts.py`
- `src/chatterbox/mtl_tts.py`
- `src/chatterbox/vc.py`
- `src/chatterbox/models/s3gen/s3gen.py`

## Implementation Notes

The submodule approach is the most robust solution for production deployments as it:
- Eliminates external Git clone operations during installation
- Ensures consistent versions of the dependency
- Reduces installation complexity
- Makes the project self-contained