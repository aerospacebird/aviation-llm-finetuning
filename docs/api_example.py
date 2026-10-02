# API / inference example

This module is a lightweight placeholder for serving the aviation fine-tuned model through an HTTP endpoint.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Aviation LLM API")


class QueryRequest(BaseModel):
    prompt: str
    max_new_tokens: int = 256


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/generate")
def generate(req: QueryRequest) -> dict:
    return {
        "prompt": req.prompt,
        "result": "This is a placeholder response. Connect with your fine-tuned model for live generation.",
        "max_new_tokens": req.max_new_tokens,
    }
```
