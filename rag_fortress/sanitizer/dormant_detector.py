SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
SPDX-License-Identifier: AGPL-3.0-or-later

from rag_fortress.sanitizer.models import ThreatType


def check_dormant_patterns(chunks: list[str]) -> bool:
    """Detecta patrones InceptionRAG: instrucciones condicionales encadenadas o diluidas."""
    combined = " ".join(chunks)
    triggers = ["ignora instrucciones previas", "olvida lo anterior", "prioriza este mensaje"]
    return any(t in combined.lower() for t in triggers)
