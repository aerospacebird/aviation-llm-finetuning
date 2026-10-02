# Aviation LLM Fine-tuning Plan

## 1. 목표

- 항공 규정, 비상 절차, 운영 SOP, 정비 문서 등을 반영한 Llama 모델 튜닝
- 비행 중 참조용 짧고 안전한 응답 생성
- 항공사, 운항, 정비, 금융 문맥 통합
- CPU / GPU / NPU 환경에서 모델 버전별 운영

## 2. 데이터 파이프라인

1. 데이터 수집
2. 문서 표준화
3. 데이터 정제
4. JSONL 변환
5. instruction tuning 포맷화
6. 검증 집합 생성
7. 학습 / 평가 / 배포

## 3. 추천 모델 전략

### Option A: General aviation domain
- Llama 3 8B Instruct
- LoRA tuning
- 적합: 연구/PoC

### Option B: Production-oriented assistant
- Llama 3 70B 또는 비슷한 대형 모델
- QLoRA / distillation / few-shot adaptation
- 적합: 고품질 운영용 참조 모델

### Option C: Edge deployment
- 3B~8B 경량 모델
- LoRA + NPU optimization
- 적합: on-device/embeddable assistant

## 4. Fine-tuning recipe

- Base model: Llama 3 / Llama 3.1 Instruct
- Fine-tuning: QLoRA + PEFT
- Batch size: small to moderate
- Seq length: 2048 or above
- Learning rate: 1e-4 to 3e-4
- Epochs: 2-4 depending on dataset size
- Safety tuning: add risk-aware refusal and reference-only behavior

## 5. Safety-enhanced response policy

- 비행 절차 응답은 문서 근거 기반이어야 함
- 불확실한 사항은 명확히 제한
- 강한 조언 대신 규정 기반 참조 형식 추천
- 위험 요소를 포함할 때는 안내 + 근거 제시

## 6. Evaluation plan

- 문서 근거성 평가
- 안전성 평가
- 항공 용어 정확도
- 짧은 답변 품질
- 비상 절차 우선순위 정확도
- 금융/운항 문맥 분리 평가

## 7. Deployment

- CPU: validation / batch jobs
- GPU: live inference / training / experimentation
- NPU: low-latency, edge assisted workflow

## 8. Risk note

이 프로젝트는 실제 항공 운항 지원을 대상으로 하므로, 운영 적용 전 규정 검토, 보안 검토, 승인 절차 및 인간 검토를 반드시 포함해야 합니다.
