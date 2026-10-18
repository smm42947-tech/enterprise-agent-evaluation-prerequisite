import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from agents.common.models import AskRequest, AskResponse
from agents.common.runtime import build_response

VERSION = "support-agent-v2"
RESPONSES = json.loads((Path(__file__).parent / "responses.json").read_text(encoding="utf-8"))
app = FastAPI(title="IT Operations Support Agent support-agent-v2", version="1.0")

@app.get("/health")
def health():
    return {"status": "healthy", "agent_version": VERSION}

@app.get("/version")
def version():
    return {"agent_version": VERSION, "role": "candidate-release"}

@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest):
    entry = RESPONSES.get(payload.test_case_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Unknown test_case_id")
    return build_response(payload, VERSION, entry)
