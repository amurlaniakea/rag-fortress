SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
SPDX-License-Identifier: AGPL-3.0-or-later

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
