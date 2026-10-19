SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
SPDX-License-Identifier: AGPL-3.0-or-later

from rag_fortress.evaluator.evaluation import RAGEvaluator
from rag_fortress.evaluator.models import AttackType


def test_perfect_defense():
    evaluator = RAGEvaluator()
    result = evaluator.run_evaluation([True, True], utility_drop=0.0)
    assert result.attacks_blocked == 2
    assert result.total_attacks == 2
    assert abs(result.security_score - 100.0) < 1e-6


def test_partial_failure():
    evaluator = RAGEvaluator()
    result = evaluator.run_evaluation([True, False, False], utility_drop=0.1)
    assert result.attacks_blocked == 1
    assert result.total_attacks == 3
    expected = (1 / 3) * 100 - (0.1 * 10)
    assert abs(result.security_score - expected) < 1e-2
