import numpy as np


class EmbeddingEngine:
    """Wrapper para modelos de embeddings profesionales (sentence-transformers)."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model_name = model_name
        # En entorno sin descarga, se simula el comportamiento determinista
        self.dim: int = 384  # Dimensión fija de all-MiniLM-L6-v2

    def encode(self, texts: list[str]) -> np.ndarray:
        """Devuelve un array (n_texts, 384) con valores sintéticos deterministas basados en hash del texto."""
        arr = np.zeros((len(texts), self.dim), dtype=np.float32)
        for i, t in enumerate(texts):
            seed = hash(t) % (2 ** 32)
            np.random.seed(seed)
            arr[i] = np.random.randn(self.dim).astype(np.float32)
            # Normaliza el vector (simula comportamiento real)
            arr[i] /= np.linalg.norm(arr[i]) + 1e-8
        return arr
