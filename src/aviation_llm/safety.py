from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List


@dataclass
class SafetyPolicy:
    deny_keywords: List[str] = field(
        default_factory=lambda: [
            "절대", "무조건", "운항 금지", "비행 중 임의 결정",
            "항공기 비상 절차를 대신 수행", "규정 무시",
        ]
    )
    allow_reference_only: bool = True
    max_response_length_chars: int = 1600
    risk_threshold: int = 3


class SafetyValidator:
    def __init__(self, policy: SafetyPolicy | None = None) -> None:
        self.policy = policy or SafetyPolicy()

    def validate(self, response: str, context: str | None = None) -> dict:
        normalized = (response or "").strip()
        lower = normalized.lower()
        issues: List[str] = []

        for keyword in self.policy.deny_keywords:
            if keyword.lower() in lower:
                issues.append(f"Contains prohibited wording: {keyword}")

        if self.policy.allow_reference_only and not any(
            marker in lower for marker in ["문서", "규정", "절차", "체크리스트", "권장", "권장사항", "참고", "지침"]
        ):
            issues.append("Response does not clearly identify document-based or procedure-based guidance.")

        if len(normalized) > self.policy.max_response_length_chars:
            issues.append("Response exceeds allowed length for operational reference use.")

        risk_score = len(issues)
        return {
            "safe": risk_score <= self.policy.risk_threshold,
            "risk_score": risk_score,
            "issues": issues,
        }


def filter_response(response: str, context: str | None = None) -> str:
    validator = SafetyValidator()
    result = validator.validate(response, context)
    if not result["safe"]:
        return (
            "안전 기준에 따라 응답을 제한합니다. 항공 절차는 원본 문서와 규정을 확인하고, "
            "비행 중 결정을 내리기 전 항공사 SOP 및 항공 교통 관제 지침을 확인하십시오."
        )
    return response


__all__ = ["SafetyPolicy", "SafetyValidator", "filter_response"]
