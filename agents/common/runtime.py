import re, time
from agents.common.knowledge_loader import load_document

def token_estimate(text: str) -> int:
    return max(1, len(re.findall(r"\w+|[^\w\s]", text)))

def build_response(payload, version, entry):
    start = time.perf_counter()
    response = entry["response"]
    contexts = [load_document(x) for x in entry.get("document_ids", [])]
    contexts = [x for x in contexts if x]
    input_tokens = token_estimate(payload.question)
    output_tokens = token_estimate(response)
    configured = entry.get("latency_ms", 500)
    time.sleep(min(configured / 1000.0, 0.08))
    measured = int((time.perf_counter() - start) * 1000)
    return {
        "test_case_id": payload.test_case_id,
        "agent_version": version,
        "response": response,
        "retrieved_context": contexts,
        "citations": entry.get("citations", []),
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "model": "deterministic-hackathon-agent",
        "latency_ms": configured + measured,
        "status": "success"
    }
