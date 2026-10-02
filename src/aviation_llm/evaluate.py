from __future__ import annotations

import argparse
import json
from pathlib import Path

import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer


def evaluate_model(model_path: str, dataset_path: str) -> dict:
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, device_map="auto")
    dataset = load_dataset("json", data_files=dataset_path, split="train")

    correct = 0
    total = min(len(dataset), 20)

    for item in dataset.select(range(total)):
        prompt = f"### Instruction\n{item['instruction']}\n\n### Context\n{item.get('input','')}\n\n### Response\n"
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=128,
                do_sample=False,
            )

        generated = tokenizer.decode(output[0], skip_special_tokens=True)
        response = generated.split("### Response\n", 1)[-1].strip()
        expected = item.get("output", "").strip()
        if response and expected and response[: min(len(response), len(expected))] == expected[: min(len(response), len(expected))]:
            correct += 1

    return {
        "total": total,
        "correct": correct,
        "accuracy": round(correct / total * 100.0, 2) if total else 0.0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple evaluation script for aviation model")
    parser.add_argument("--model-path", type=str, required=True)
    parser.add_argument("--dataset", type=str, required=True)
    args = parser.parse_args()

    report = evaluate_model(args.model_path, args.dataset)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
