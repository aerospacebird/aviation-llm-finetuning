# Aviation LLM Integration Notes

## 1. Device-level strategy

### CPU
- For local validation and document processing
- Suitable for baseline text analysis and training scripts

### GPU
- For training and inference at scale
- Best for large context lengths and multi-user experiments

### NPU
- For edge or on-device inference
- Suitable for lightweight assistants and sensitive local use

## 2. Deployment suitability

### In-flight assistant
- Short, concise, framework-based answers only
- Use retrieval from approved manuals and SOPs
- Add explicit source references

### Airline ops desk
- Richer contextual response with document-based reasoning
- Add policy metadata and human review

### Finance and risk desk
- Limit to summary and contextual analysis
- Do not provide binding operational decisions using model output alone

## 3. Practical recommendations

- Separate model variants by use case:
  - flight safety assistant
  - airline ops assistant
  - finance-risk summarizer
  - edge NPU model
- Maintain explicit document provenance in every answer
- Use safety guardrails before model output reaches user

## 4. Suggested architecture

```text
User Query
   -> Safety Filter
   -> RAG Knowledge Search
   -> Model Inference
   -> Output Validator
   -> Human Review (if needed)
   -> Final Response
```
