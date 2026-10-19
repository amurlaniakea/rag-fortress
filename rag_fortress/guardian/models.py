from enum import Enum
from pydantic import BaseModel


class IntegrityStatus(str, Enum):
    SAFE = "SAFE"
    COMPROMISED = "COMPROMISED"
    LOW_RELEVANCE = "LOW_RELEVANCE"


class GuardianResult(BaseModel):
    chunk_index: int
    status: IntegrityStatus
    relevance_score: float
    mia_detected: bool
    reason: str
