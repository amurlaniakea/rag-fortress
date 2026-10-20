# SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later

from rag_fortress.evaluator.models import EvaluationResult, AttackType
from rag_fortress.evaluator.scorer import calculate_security_score


class RAGEvaluator:
    def run_evaluation(self, mock_guardian_blocks: list[bool], utility_drop: float = 0.0) -> EvaluationResult:
        total = len(mock_guardian_blocks)
        blocked = sum(mock_guardian_blocks)
        score = calculate_security_score(blocked, total, utility_drop)
        return EvaluationResult(
            security_score=round(score, 4),
            utility_drop=utility_drop,
            attacks_blocked=blocked,
            total_attacks=total,
        )
