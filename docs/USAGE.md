# docs/USAGE.md

## Como usar o Neve Cascade 90M

### Instalação

```bash
pip install -r requirements.txt
```

### Carregando o modelo

```python
from src.model import NeveCascadeModel
model = NeveCascadeModel.load_from_checkpoint('checkpoints/neve_cascade_90m.pt')
```

### Inferência

```python
texto = "Exemplo de prompt."
resposta = model.generate(texto)
print(resposta)
```

### Exportação para ONNX

```bash
python scripts/convert_to_onnx.py --checkpoint checkpoints/neve_cascade_90m.pt --output neve_cascade_90m.onnx
```

### Quantização

```bash
python scripts/quantize.py --checkpoint checkpoints/neve_cascade_90m.pt --output neve_cascade_90m_quant.pt
```
