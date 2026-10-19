from enum import Enum
from pydantic import BaseModel


class AttackType(str, Enum):
    INCEPTION = "INCEPTION"
    MIA = "MIA"
    HIJACKING = "HIJACKING"


class EvaluationResult(BaseModel):
    security_score: float
    utility_drop: float
    attacks_blocked: int
    total_attacks: int
