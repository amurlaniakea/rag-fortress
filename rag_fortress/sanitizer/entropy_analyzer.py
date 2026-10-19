import statistics


def calculate_semantic_entropy(text: str) -> float:
    """Heurística: varianza de longitud de oraciones como proxy de entropía."""
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    if not sentences:
        return 0.0
    lengths = [len(s.split()) for s in sentences]
    return float(statistics.stdev(lengths)) if len(lengths) > 1 else 0.0
