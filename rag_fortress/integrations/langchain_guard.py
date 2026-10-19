SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
SPDX-License-Identifier: AGPL-3.0-or-later

from rag_fortress.guardian.retrieval import RetrievalGuardian


class FortressRetriever:
    """Interceptor tipo LangChain que aplica verificación de integridad antes de devolver chunks."""

    def __init__(self, relevance_threshold: float = 0.3):
        self.guardian = RetrievalGuardian(relevance_threshold=relevance_threshold)

    def retrieve(self, query: str, chunks: list[str]) -> list[str]:
        """Filtra los chunks que no pasan la verificación del guardian."""
        results = self.guardian.verify(query, chunks)
        safe_chunks = [
            chunks[i] for i, r in enumerate(results) if r.status.value == "SAFE" and r.mia_detected is False
        ]
        return safe_chunks
