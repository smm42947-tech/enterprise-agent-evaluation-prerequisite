from fastapi.testclient import TestClient
from agents.version_a.api import app as app_a
from agents.version_b.api import app as app_b

def test_health():
    assert TestClient(app_a).get("/health").status_code == 200
    assert TestClient(app_b).get("/health").status_code == 200

def test_common_contract():
    payload={"test_case_id":"TC001","question":"What is a Sev1 incident?"}
    for app in (app_a,app_b):
        data=TestClient(app).post("/ask",json=payload).json()
        for key in ["response","retrieved_context","citations","input_tokens","output_tokens","total_tokens","latency_ms"]:
            assert key in data

def test_unknown_case():
    r=TestClient(app_a).post("/ask",json={"test_case_id":"BAD","question":"Unknown question"})
    assert r.status_code == 404
