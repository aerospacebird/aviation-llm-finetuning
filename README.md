# Aviation LLM Domain Project

이 저장소는 항공산업 특화 LLM을 설계, 학습, 평가, 배포하기 위한 실험용 프레임워크입니다.

주요 목표:
- 항공 규정, 비행 절차, 운영 매뉴얼, 정비 문서와 같은 도메인 문맥을 학습
- 조종사 및 항공사 운영 인력의 빠른 참조용 응답 제공
- 위험 문맥에서 안전한 답변 스타일 보장
- CPU / GPU / NPU 환경에서 모델을 운영할 수 있는 구조 제공
- 항공 + 금융 + 전세계 항공사 운영 문맥을 통합하는 RAG/지식기반 아키텍처 설계

## 프로젝트 아키텍처

- Base Model: Llama family
- Fine-tuning: LoRA / QLoRA
- Knowledge layer: RAG + 문서 인덱싱
- Safety layer: 규정 근거 검증 + 금지 응답 필터
- Deployment: CPU/GPU/NPU-aware serving

## 빠른 시작

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 샘플 데이터 준비

```bash
python -m src.aviation_llm.data.prepare_dataset \
  --input data/samples/flight_safety_example.jsonl \
  --output data/processed/flight_safety_example.jsonl \
  --max-samples 5000
```

### 사전 학습 모델 기반 파인튜닝

```bash
python -m src.aviation_llm.train_lora --config configs/llama3_8b_aviation.yaml
```

### 추론 예시

```bash
python -m src.aviation_llm.inference \
  --model-path checkpoints/aviation-llm \
  --prompt "비상 상황에서 조종사는 무엇을 우선 점검해야 하나요?"
```

### 평가 예시

```bash
python -m src.aviation_llm.evaluate \
  --model-path checkpoints/aviation-llm \
  --dataset data/processed/flight_safety_example.jsonl
```

## 데이터 구조

```json
{
  "instruction": "비상 상황에서 조종사는 무엇을 먼저 확인해야 하나요?",
  "input": "엔진 고장, 고도 12,000ft",
  "output": "항공기 상태 확인, ATC 소통, 비행 경로 안정화, 관련 체크리스트 수행, 안전한 착륙 가능한 곳 탐색"
}
```

## 하드웨어 전략

### CPU
- 로컬 검증
- 경량 서빙
- 작은 모델 테스트

### GPU
- 대용량 학습
- 빠른 추론
- 다중 문맥 처리

### NPU
- 온디바이스 경량 추론
- 민감정보 로컬 처리
- 보조형 서브모델 배포

## 안전성 원칙

- 항공 관련 비상 절차는 반드시 문서 근거 기반 응답
- 환각 방지: 문서 인용 및 출처 제시
- 조종사 의사결정에 대한 위험한 추정은 제한
- 비행 중 참조용 응답은 짧고 명확해야 함

## 문서 구조

- `docs/architecture.md`: 전체 시스템 설계
- `docs/hardware_strategy.md`: CPU/GPU/NPU 운영 전략
- `data/README.md`: 데이터셋 가이드
- `src/aviation_llm/`: 파인튜닝 및 추론 코드

## 라이선스

Apache 2.0
