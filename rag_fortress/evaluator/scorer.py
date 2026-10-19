SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
SPDX-License-Identifier: AGPL-3.0-or-later

def calculate_security_score(blocked: int, total: int, utility_drop: float) -> float:
    """Fórmula determinista con acotación [0, 100]."""
    if total == 0:
        return 0.0
    score = (blocked / total) * 100 - (utility_drop * 10)
    return max(0.0, min(100.0, score))
