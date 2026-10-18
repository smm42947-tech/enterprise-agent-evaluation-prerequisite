import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

@lru_cache
def load_manifest():
    path = ROOT / "approved_knowledge" / "knowledge_manifest.json"
    return json.loads(path.read_text(encoding="utf-8"))["documents"]

@lru_cache
def load_document(document_id: str):
    item = next((d for d in load_manifest() if d["document_id"] == document_id), None)
    if not item:
        return None
    text = (ROOT / item["file_path"]).read_text(encoding="utf-8")
    return {"document_id": document_id, "document_name": item["title"], "content": text}
