# docs/TRAINING_PIPELINE.md

## Pipeline de Treinamento Avançado

O pipeline do Neve Cascade 90M foi projetado para máxima eficiência e reprodutibilidade, utilizando técnicas de ponta em cada etapa:

### 1. Pré-processamento
- Limpeza e normalização de texto
- Remoção de duplicatas e dados tóxicos
- Tokenização customizada
- Balanceamento de classes e domínios

### 2. Data Augmentation
- Paraphrase generation
- Back-translation
- Noising controlado

### 3. Treinamento
- Mixed precision training (FP16)
- Gradual unfreezing
- Scheduler de learning rate cíclico
- Early stopping e checkpointing inteligente
- Distributed training (multi-GPU e CPU)

### 4. Validação e Testes
- Validação cruzada estratificada
- Métricas customizadas para português
- Logging com TensorBoard e Weights & Biases

### 5. Pós-processamento
- Quantização pós-treinamento
- Exportação ONNX e TorchScript

Scripts e configs em `scripts/train.py` e `docs/TRAINING_CONFIG.md`.
