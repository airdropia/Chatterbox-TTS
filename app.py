import sys
import os
# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
# Add the models directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src", "chatterbox", "models"))

import torch
import gradio as gr
import time
import spaces
import warnings
import psutil
import platform
import GPUtil
from modules.config import LANGUAGE_CONFIG, SUPPORTED_LANGUAGES
from modules.utils import convert_audio, load_audio, save_audio, validate_audio
from modules.ui import create_interface

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

# Check system resources
def check_system_resources():
    """Check system resources and print information"""
    print("=" * 50)
    print("🚀 Chatterbox TTS Enhanced Starting...")
    
    # Device information
    device = "CUDA" if torch.cuda.is_available() else "CPU"
    print(f"📱 Device: {device}")
    
    if device == "CUDA":
        try:
            # GPU information
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu = gpus[0]
                print(f"🎮 GPU: {gpu.name}")
                print(f"💾 GPU Memory: {gpu.memoryTotal:.2f} GB")
                
                # Check if GPU has sufficient memory
                if gpu.memoryTotal < 5:
                    print("⚠️ Warning: GPU has less than 5GB of memory. Performance may be limited.")
                else:
                    print("✅ GPU has sufficient memory (≥5GB)")
            else:
                print("⚠️ Warning: CUDA is available but no GPU was detected")
        except Exception as e:
            print(f"⚠️ Error detecting GPU information: {str(e)}")
    
    # CPU information
    cpu_count = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"🖥️ CPU: {platform.processor()} ({cpu_count} cores, {cpu_percent}% usage)")
    
    # Memory information
    memory = psutil.virtual_memory()
    print(f"💾 RAM: {memory.total / (1024**3):.2f} GB ({memory.percent}% usage)")
    
    print("=" * 50)

# Main function
def main():
    # Check system resources
    check_system_resources()
    
    # Create the interface
    interface = create_interface()
    
    # Launch the interface
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,
        debug=False,
        show_error=True,
        quiet=False
    )

if __name__ == "__main__":
    main()