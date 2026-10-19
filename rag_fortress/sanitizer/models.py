from enum import Enum
from pydantic import BaseModel


class DocumentStatus(str, Enum):
    CLEAN = "clean"
    SUSPICIOUS = "suspicious"
    BLOCKED = "blocked"


class ThreatType(str, Enum):
    INCEPTION_DORMANT = "inception_dormant"
    HIGH_ENTROPY = "high_entropy"
    NONE = "none"


class SanitizerResult(BaseModel):
    status: DocumentStatus
    threat: ThreatType
    reason: str
    entropy_score: float
