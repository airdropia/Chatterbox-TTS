import torch
import numpy as np

def padding(x, max_len):
    x = np.pad(x, (0, max_len - len(x)), mode='constant')
    return x