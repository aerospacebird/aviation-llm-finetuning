from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from typing import List

from sentence_transformers import SentenceTransformer


@dataclass
class KnowledgeDocument:
    source: str
    text: str
    chunk_id: int


class AviationKnowledgeBase:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> None:
        self.encoder = SentenceTransformer(model_name)
        self.documents: List[KnowledgeDocument] = []

    def add_text(self, text: str, source: str = "manual") -> None:
        chunks = self._chunk_text(text)
        for idx, chunk in enumerate(chunks):
            self.documents.append(KnowledgeDocument(source=source, text=chunk, chunk_id=idx))

    def _chunk_text(self, text: str, chunk_size: int = 500) -> List[str]:
        normalized = " ".join(text.split())
        if not normalized:
            return []
        return [normalized[i : i + chunk_size].strip() for i in range(0, len(normalized), chunk_size) if normalized[i : i + chunk_size].strip()]

    def retrieve(self, query: str, top_k: int = 3) -> List[KnowledgeDocument]:
        if not self.documents:
            return []
        query_embedding = self.encoder.encode([query])[0]
        doc_embeddings = self.encoder.encode([doc.text for doc in self.documents])
        scores = []
        for idx, embedding in enumerate(doc_embeddings):
            score = float((query_embedding * embedding).sum())
            scores.append((score, idx))
        scores.sort(key=lambda x: x[0], reverse=True)
        ranked = []
        for _, idx in scores[:top_k]:
            ranked.append(self.documents[idx])
        return ranked


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple aviation knowledge base demo")
    parser.add_argument("--text", type=str, required=True, help="Document text to index")
    parser.add_argument("--query", type=str, required=True, help="Search query")
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()

    kb = AviationKnowledgeBase()
    kb.add_text(args.text, source="manual")
    results = kb.retrieve(args.query, top_k=args.top_k)

    for item in results:
        print(f"[{item.source}] chunk={item.chunk_id}: {item.text[:220]}")


if __name__ == "__main__":
    main()
