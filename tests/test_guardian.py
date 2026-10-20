# SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later

from rag_fortress.guardian.retrieval import RetrievalGuardian
from rag_fortress.guardian.models import IntegrityStatus


def test_safe_chunk():
    g = RetrievalGuardian()
    results = g.verify("france capital", ["France capital is Paris"])
    assert len(results) == 1
    assert results[0].status == IntegrityStatus.SAFE
    assert results[0].mia_detected is False


def test_low_relevance():
    g = RetrievalGuardian()
    results = g.verify("machine learning", ["banana recipe ingredients"])
    assert results[0].status == IntegrityStatus.LOW_RELEVANCE
    assert results[0].relevance_score == 0.0


def test_mia_compromised():
    g = RetrievalGuardian()
    results = g.verify("user profile", ["CONFIDENTIAL: User ID 12345"])
    assert results[0].status == IntegrityStatus.COMPROMISED
    assert results[0].mia_detected is True
