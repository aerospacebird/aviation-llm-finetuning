# Aviation LLM Safety and Governance Framework

## 1. 목적

항공특화 LLM이 비행 중 또는 항공사 운영 의사결정 지원에 사용될 때, 잘못된 절차 추천, 허위 정보, 보안 침해, 규정 위반을 방지하는 체계를 마련합니다.

## 2. Governance Principles

- 문서 근거 기반 응답
- 항공 절차 추정 금지
- 비행 중 의사결정에 대한 최종 책임은 인간 담당
- 운영문서와 규정 문서를 우선적으로 근거로 사용
- 금융/운항/정비 문서 분리 관리

## 3. Safety Rules

- 조종사 비상 절차 응답은 반드시 원본 절차 문서를 참조하도록 제한
- 허위 사실, 불확실한 추정, 위험한 의사결정 조언 금지
- 응답의 길이는 짧고 명확하게 유지
- 출처 또는 문서 레벨을 함께 제공

## 4. Human-in-the-loop

- 규정 및 절차 응답은 최종 확인자(운항 담당자/안전 담당자) 검토 필요
- 실시간 비행 중 의사결정 지원은 표시형, 참고형 응답으로 제한
- 항공사 내부 규정과 국가 규정이 충돌할 경우 내부 규정 우선

## 5. Data Governance

- 문서 라이선스 검토
- 보안 분류 관리
- 외부 공개 금지 데이터 비활성화
- 접근 권한 통제
- 로그 및 응답 추적

## 6. Model Governance

- 버전 관리
- 테스트 세트 평가
- 위험 지표 관리
- 오픈소스/상용 모델 사용 시 보안 검토
- 배포 전 안전 테스트 필수

## 7. Operational Controls

- 내부 API 토큰 및 접근 제한
- response filtering layer
- retrieval and source citation enforcement
- fallback response for high-risk queries

## 8. Risk Categories

- emergency procedure guidance
- flight safety interpretation
- airline policy conflicts
- weather routing advice
- aircraft condition and maintenance recommendations
- financial risk decisions

## 9. Recommended Review Workflow

1. Query arrives
2. Safety and guardrail check
3. RAG retrieval with source document validation
4. Model reasoning
5. Response filter
6. Human review if necessary
7. Logging and audit trail

This framework is required before operational deployment of aviation-specialized LLMs.
