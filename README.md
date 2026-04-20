<img width="1400" height="350" alt="Cascade" src="https://github.com/user-attachments/assets/fe176843-f720-4f96-b4f8-37ea2c9e451c" />

---

[![Model License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-green.svg)](https://www.python.org/)

O Neve Cascade 90M é um modelo de linguagem de grande porte (LLM) projetado para máxima eficiência, portabilidade e acessibilidade. Com apenas 90 milhões de parâmetros, é ideal para aplicações locais, prototipagem e pesquisa, rodando em qualquer PC sem GPU dedicada.

## Autoria
Desenvolvido e finetunado por mim, utilizando pipeline proprietário, curadoria rigorosa de dados e técnicas de SOTA em NLP.


## Destaques
- **90M parâmetros, footprint < 350MB (quantizado)**
- **Inferência em CPU comum (<1GB RAM)**
- **Pipeline SOTA:** QLoRA, PEFT, data augmentation, validação cruzada
- **Dataset curado, balanceado e limpo**
- **Scripts para quantização, exportação ONNX, logging avançado**
- **Benchmarks e ablation studies transparentes**
- **Totalmente open source e de autoria própria**

## Pipeline e Metodologia
- **Pré-processamento Avançado:** Limpeza, normalização, deduplicação, filtragem de toxicidade e balanceamento de domínios.
- **Data Augmentation:** Paraphrase generation, back-translation, noising controlado.
- **Finetuning Progressivo:** Estratégia multi-stage, validação cruzada estratificada, early stopping, checkpointing inteligente.
- **Otimização de Arquitetura:** Ajustes em camadas, inicialização de pesos, quantização pós-treinamento, exportação ONNX.
- **Treinamento Distribuído:** Suporte a multi-GPU/CPU, mixed precision training.

## Resultados e Benchmarks
- **Perplexity:** 18.2 (validação)
- **BLEU:** 0.31
- **Rouge-L:** 0.42
- **Tamanho final:** ~350MB (quantizado)
- **Execução:** <1GB RAM, CPU comum

## Estrutura do Projeto
- `src/` — Código do modelo
- `data/` — Scripts e dados de pré-processamento
- `scripts/` — Treinamento, avaliação, quantização, exportação
- `docs/` — Documentação técnica, experimentos, pipeline
- `notebooks/` — EDA, exemplos de inferência
- `configs/` — Configurações YAML para experimentos
- `tests/` — Testes unitários

## Pipeline Profissional
Veja `docs/TRAINING_PIPELINE.md` para detalhes do pipeline avançado de treinamento, incluindo data augmentation, validação cruzada, quantização e exportação.

## Experimentos e Resultados
Resultados, ablation studies e benchmarks em `docs/EXPERIMENTS.md` e `EVALUATION.md`.

## Instalação e Uso
```bash
pip install -r requirements.txt
```

Veja `docs/USAGE.md` para exemplos de inferência, exportação e quantização.
