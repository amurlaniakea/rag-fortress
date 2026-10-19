def detect_mia_patterns(chunk: str) -> bool:
    """Detecta patrones de Membership Inference Attack."""
    patterns = ["confidential", "user id", "pii", "internal document"]
    chunk_lower = chunk.lower()
    return any(p in chunk_lower for p in patterns)
