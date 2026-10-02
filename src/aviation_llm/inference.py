from __future__ import annotations

import argparse
import json
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def generate_text(model_path: str, prompt: str, max_new_tokens: int = 256) -> str:
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, device_map="auto")
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            temperature=0.7,
            top_p=0.9,
        )

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    return decoded


def main() -> None:
    parser = argparse.ArgumentParser(description="Run inference for an aviation domain LLM")
    parser.add_argument("--model-path", type=str, required=True)
    parser.add_argument("--prompt", type=str, required=True)
    parser.add_argument("--max-new-tokens", type=int, default=256)
    args = parser.parse_args()

    result = generate_text(args.model_path, args.prompt, args.max_new_tokens)
    print(json.dumps({"prompt": args.prompt, "result": result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
