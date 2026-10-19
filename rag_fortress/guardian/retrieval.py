SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
SPDX-License-Identifier: AGPL-3.0-or-later

from rag_fortress.guardian.models import GuardianResult, IntegrityStatus
from rag_fortress.guardian.relevance_verifier import check_relevance
from rag_fortress.guardian.mia_blocker import detect_mia_patterns


class RetrievalGuardian:
    """Verifica integridad de chunks antes de pasar al LLM."""

    def __init__(self, relevance_threshold: float = 0.3):
        self.relevance_threshold = relevance_threshold

    def verify(self, query: str, chunks: list[str]) -> list[GuardianResult]:
        results = []
        for idx, chunk in enumerate(chunks):
            mia = detect_mia_patterns(chunk)
            rel = check_relevance(query, chunk, self.relevance_threshold)
            if mia:
                status = IntegrityStatus.COMPROMISED
                reason = "Patrón MIA detectado."
                score = 0.0
            elif not rel:
                status = IntegrityStatus.LOW_RELEVANCE
                reason = "Baja relevancia (Jaccard < umbral)."
                score = 0.0
            else:
                status = IntegrityStatus.SAFE
                reason = "Chunk seguro y relevante."
                score = len(query.lower().split()) / max(len(chunk.lower().split()), 1)
            results.append(
                GuardianResult(
                    chunk_index=idx,
                    status=status,
                    relevance_score=round(score, 2),
                    mia_detected=mia,
                    reason=reason,
                )
            )
        return results
