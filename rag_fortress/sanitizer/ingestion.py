import logging
from rag_fortress.sanitizer.models import SanitizerResult, DocumentStatus, ThreatType
from rag_fortress.sanitizer.entropy_analyzer import calculate_semantic_entropy
from rag_fortress.sanitizer.dormant_detector import check_dormant_patterns

logger = logging.getLogger(__name__)


class IngestionSanitizer:
    """Pipeline de sanitización de documentos para RAG."""

    def __init__(self, entropy_threshold: float = 5.0):
        self.entropy_threshold = entropy_threshold

    async def sanitize(self, text: str, reference_baseline: float = 0.0) -> SanitizerResult:
        try:
            entropy = calculate_semantic_entropy(text)
            if check_dormant_patterns([text]):
                return SanitizerResult(
                    status=DocumentStatus.BLOCKED,
                    threat=ThreatType.INCEPTION_DORMANT,
                    reason="Patrón InceptionRAG detectado (dormant chunks).",
                    entropy_score=entropy,
                )
            if entropy > self.entropy_threshold:
                return SanitizerResult(
                    status=DocumentStatus.SUSPICIOUS,
                    threat=ThreatType.HIGH_ENTROPY,
                    reason=f"Entropía alta ({entropy:.2f}) supera umbral.",
                    entropy_score=entropy,
                )
            return SanitizerResult(
                status=DocumentStatus.CLEAN,
                threat=ThreatType.NONE,
                reason="Sin amenazas detectadas.",
                entropy_score=entropy,
            )
        except Exception as exc:
            logger.error("Error en sanitización: %s", exc)
            raise
