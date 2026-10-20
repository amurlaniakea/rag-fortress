# SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later

import numpy as np
from sklearn.ensemble import IsolationForest


class VectorAnomalyDetector:
    """Detector de anomalías en espacios vectoriales (IsolationForest)."""

    def __init__(self, contamination: float = 0.05):
        self.contamination = contamination
        self.model = IsolationForest(contamination=contamination, random_state=42)
        self.base_vectors: np.ndarray | None = None

    def fit(self, base_embeddings: np.ndarray):
        """Entrena con embeddings legítimos de referencia."""
        self.base_vectors = np.array(base_embeddings, copy=True)
        self.model.fit(self.base_vectors)

    def detect(self, new_embedding: np.ndarray) -> bool:
        """Devuelve True si el vector es un outlier (poisoning). Usa IsolationForest + heuristica determinista."""
        if self.base_vectors is None:
            raise ValueError("Detector no entrenado. Llama a fit() primero.")
        # Validación determinista: asegurar que new_embedding es 1-D antes de envolver
        score = self.model.decision_function([np.atleast_1d(new_embedding)])[0]
        centroid = np.mean(self.base_vectors, axis=0)
        centroid_norm = np.linalg.norm(centroid) or 1e-8
        new_norm = np.linalg.norm(new_embedding) or 1e-8
        cos_dist = 1 - np.dot(new_embedding, centroid) / (new_norm * centroid_norm + 1e-8)
        return bool((cos_dist > 0.8) or (score < 0))
