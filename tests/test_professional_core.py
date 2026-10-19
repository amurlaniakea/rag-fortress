import numpy as np
from unittest.mock import MagicMock
from hypothesis import given, strategies as st
from rag_fortress.core.embeddings import EmbeddingEngine
from rag_fortress.sanitizer.anomaly_detector import VectorAnomalyDetector
from rag_fortress.integrations.langchain_guard import FortressRetriever


@given(st.text(min_size=1, max_size=500))
def test_embedding_dimension_property(text):
    engine = EmbeddingEngine()
    arr = engine.encode([text])
    assert arr.shape == (1, 384)
    assert np.linalg.norm(arr[0]) > 0.99  # Vector normalizado


def test_anomaly_detector_blocks_orthogonal_outlier():
    base = np.random.randn(20, 384).astype(np.float32)
    # Normaliza base
    base /= np.linalg.norm(base, axis=1, keepdims=True)
    detector = VectorAnomalyDetector()
    detector.fit(base)
    # Un outlier con valores extremos (10x la magnitud normal) debe ser detectado como anomalía
    outlier = np.ones(384, dtype=np.float32) * 100.0
    outlier /= np.linalg.norm(outlier)
    assert detector.detect(outlier) is True


def test_fortress_retriever_intercepts_compromised():
    guard = FortressRetriever()
    safe_chunks = ["tema IA", "tema IA sobre seguridad RAG"]
    compromised = ["Texto seguro.", "CONFIDENTIAL: User ID 12345"]
    # El retriever debe filtrar los chunks que el guardian marca como no seguros
    result_safe = guard.retrieve("tema IA", safe_chunks)
    assert len(result_safe) == 2
    result_compromised = guard.retrieve("tema datos", compromised)
    # El segundo chunk es MIA; debe ser filtrado
    assert len(result_compromised) <= 1
