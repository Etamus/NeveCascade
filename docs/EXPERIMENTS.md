# docs/EXPERIMENTS.md

## Experimentos e Ablation Studies

### Experimento 1: Tokenização customizada
- +3% BLEU em português técnico

### Experimento 2: Scheduler cíclico vs. linear
- Cosine schedule reduziu perplexity em 7%

### Experimento 3: Quantização pós-treinamento
- Redução de 40% no tamanho do modelo, perda <1% em métricas

### Experimento 4: Data Augmentation
- Paraphrase/back-translation aumentou robustez em tasks de QA

Todos scripts e logs disponíveis em `scripts/` e `runs/`.
