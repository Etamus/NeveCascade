# scripts/train_utils.py

"""
Utilitários avançados para treinamento do Neve Cascade 90M
"""
import torch
import random
import numpy as np

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

# ... outras funções fictícias para logging, checkpointing, etc ...
