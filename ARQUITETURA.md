# Neve Cascade 90M - Arquitetura

Este documento detalha a arquitetura do modelo Neve Cascade 90M.

## Estrutura
- 24 camadas Transformer
- 90 milhões de parâmetros
- Embeddings de 512 dimensões
- Atenção multi-cabeça (8 heads)
- Dropout e LayerNorm otimizados

## Customizações
- Redução de parâmetros sem perda significativa de performance
- Inicialização de pesos baseada em técnicas recentes
- Suporte a quantização para execução em CPUs

---

Para detalhes técnicos, consulte o código em `src/model.py`.
