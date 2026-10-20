# SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later

def detect_mia_patterns(chunk: str) -> bool:
    """Detecta patrones de Membership Inference Attack."""
    patterns = ["confidential", "user id", "pii", "internal document"]
    chunk_lower = chunk.lower()
    return any(p in chunk_lower for p in patterns)
