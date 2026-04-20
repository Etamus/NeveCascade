# scripts/convert_to_onnx.py

"""
Script para exportação do modelo Neve Cascade 90M para ONNX
"""
import torch
from src.model import NeveCascadeModel

def export_onnx(checkpoint_path, output_path):
    model = NeveCascadeModel.load_from_checkpoint(checkpoint_path)
    dummy_input = torch.zeros(1, 512, dtype=torch.long)
    torch.onnx.export(model, dummy_input, output_path, input_names=['input'], output_names=['output'])
    print(f"Exportado para {output_path}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--checkpoint', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    args = parser.parse_args()
    export_onnx(args.checkpoint, args.output)
