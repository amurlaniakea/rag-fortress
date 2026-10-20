# SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later

def check_relevance(query: str, chunk: str, threshold: float = 0.3) -> bool:
    """Heurística determinista: Jaccard similarity de conjuntos de palabras clave."""
    q_words = set(query.lower().split())
    c_words = set(chunk.lower().split())
    if not q_words or not c_words:
        return False
    inter = q_words & c_words
    union = q_words | c_words
    score = len(inter) / len(union)
    return score >= threshold
