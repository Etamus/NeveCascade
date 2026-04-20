# DATASET.md

## Curadoria e Pré-processamento de Dados

O dataset utilizado foi composto por múltiplas fontes públicas e privadas, com foco em diversidade e qualidade textual. O pipeline de pré-processamento removeu duplicatas, normalizou pontuação, corrigiu encoding e aplicou filtros de toxicidade.

- **Fontes:** Common Crawl, Wikipedia, livros, fóruns técnicos
- **Filtros:** Regex customizados, heurísticas de linguagem, deduplicação hash
- **Tokenização:** Utilização de tokenizer proprietário otimizado para português

Scripts de preparação disponíveis em `data/preprocess.py`.
