import re

def clean_portuguese_text(text):
    """Limpeza profissional de ruído em textos PT-BR"""
    # Remove tags HTML e URLs residuais
    text = re.sub(r'http\S+', '', text)
    # Normalização de caracteres especiais brasileiros
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Exemplo de uso: limpeza de datasets do Common Crawl