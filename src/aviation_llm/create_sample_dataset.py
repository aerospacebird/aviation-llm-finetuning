from __future__ import annotations

import argparse
import json
from pathlib import Path


def create_sample_dataset(output_path: str) -> None:
    records = [
        {
            "instruction": "비상 상황에서 조종사는 무엇을 우선 점검해야 하나요?",
            "input": "엔진 이상 경고가 발생한 상태",
            "output": "비상 절차를 수행하고 항공기 상태를 점검하며 ATC와 통신하고 안전한 착륙 가능한 지역을 선택하고 체크리스트를 확인합니다.",
        },
        {
            "instruction": "기상 악화 상황에서 조종사는 어떤 결정을 내려야 하나요?",
            "input": "강풍과 난기류가 발생하�� 구역",
            "output": "기상 정보를 재확인하고 항로를 수정하거나 안전 구역으로 회피하며 항공 교통 관제와 협의하고 항공기 성능 한계를 고려해야 합니다.",
        },
        {
            "instruction": "항공사 위험 관리에서 가장 중요하게 고려해야 하는 요소는 무엇인가요?",
            "input": "운항 계획 및 리스크 평가",
            "output": "비행 경로, 기상, 항공기 상태, 인적 요소, 규정 준수, 통신 상태를 종합적으로 검토하여 리스크를 사전에 식별하고 완화해야 합니다.",
        }
    ]

    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create sample aviation dataset")
    parser.add_argument("--output", type=str, default="data/samples/flight_safety_example.jsonl")
    args = parser.parse_args()
    create_sample_dataset(args.output)
    print(f"Sample dataset saved to {args.output}")
