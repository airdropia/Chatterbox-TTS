import torch
import torch.nn as nn

class ModelConfig:
    def __init__(self):
        self.hidden_size = 768
        self.num_layers = 12
        self.num_heads = 12
        self.vocab_size = 1024

class S3TokenizerV2(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.hidden_size = config.hidden_size
        self.vocab_size = config.vocab_size
        
        # Simplified model architecture
        self.embedding = nn.Embedding(config.vocab_size, config.hidden_size)
        self.transformer = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(
                d_model=config.hidden_size,
                nhead=config.num_heads,
                batch_first=True
            ),
            num_layers=config.num_layers
        )
        self.output = nn.Linear(config.hidden_size, config.vocab_size)
    
    def forward(self, x):
        x = self.embedding(x)
        x = self.transformer(x)
        x = self.output(x)
        return x