from __future__ import annotations

import argparse
import os
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

from aviation_llm.safety import filter_response

app = FastAPI(title="Aviation LLM Service", version="0.1.0")


class GenerateRequest(BaseModel):
    prompt: str
    context: str | None = None
    max_new_tokens: int = 256


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "aviation-llm"}


@app.post("/generate")
def generate(req: GenerateRequest) -> dict[str, Any]:
    generated = (
        "안전한 항공 운영을 위해 먼저 항공기 상태, 비행 경로, 기상, 통신 상태를 확인하고, "
        "관련 체크리스트와 항공사 SOP를 우선 확인하십시오."
    )
    safe_result = filter_response(generated, req.context)
    return {
        "prompt": req.prompt,
        "result": safe_result,
        "max_new_tokens": req.max_new_tokens,
        "source": "safety-guarded-template",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Launch aviation LLM FastAPI service")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    import uvicorn

    uvicorn.run(app, host=args.host, port=args.port)
