# docs/TRAINING_CONFIG.md

## Hiperparâmetros e Configurações

- batch_size: 128
- learning_rate: 2e-4 (cosine schedule)
- epochs: 24
- otimizador: AdamW (weight decay 0.01)
- warmup_steps: 2000
- max_seq_length: 512
- grad_clip: 1.0
- dropout: 0.15
- seed: 42
- mixed_precision: True
- distributed: True

Configurações completas e exemplos de YAML disponíveis em `configs/`.
