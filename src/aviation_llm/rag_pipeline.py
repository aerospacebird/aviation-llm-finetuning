from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import List

from sentence_transformers import SentenceTransformer


@dataclass
class DocumentChunk:
    id: str
    text: str
    source: str


class AviationRAG:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> None:
        self.encoder = SentenceTransformer(model_name)
        self.documents: List[DocumentChunk] = []

    def add_document(self, text: str, source: str = "manual") -> None:
        for idx, chunk in enumerate(self.chunk_text(text)):
            self.documents.append(DocumentChunk(id=f"{source}-{idx}", text=chunk, source=source))

    def chunk_text(self, text: str, chunk_size: int = 500) -> List[str]:
        normalized = text.replace("\r", "").strip()
        if not normalized:
            return []
        chunks = []
        for i in range(0, len(normalized), chunk_size):
            part = normalized[i:i + chunk_size]
            if part.strip():
                chunks.append(part.strip())
        return chunks

    def retrieve(self, query: str, top_k: int = 3) -> List[DocumentChunk]:
        if not self.documents:
            return []
        query_embedding = self.encoder.encode([query])[0]
        doc_embeddings = self.encoder.encode([doc.text for doc in self.documents])
        similarities = []
        for i, emb in enumerate(doc_embeddings):
            score = float((query_embedding * emb).sum())
            similarities.append((score, i))
        similarities.sort(key=lambda x: x[0], reverse=True)
        return [self.documents[idx] for _, idx in similarities[:top_k]]


def load_documents_from_text(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple RAG layer for aviation documents")
    parser.add_argument("--document", type=str, required=True)
    parser.add_argument("--query", type=str, required=True)
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()

    rag = AviationRAG()
    text = load_documents_from_text(args.document)
    rag.add_document(text, source=args.document)
    results = rag.retrieve(args.query, top_k=args.top_k)

    print(f"Retrieved {len(results)} documents:")
    for result in results:
        print(f"- [{result.source}] {result.text[:220]}")


if __name__ == "__main__":
    main()
