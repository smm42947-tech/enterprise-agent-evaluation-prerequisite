# Enterprise Agent Evaluation Framework - Candidate Starter Kit

This repository is the prerequisite package for the **AI Platform & Agentic Build Hackathon** use case: **Enterprise Agent Evaluation Framework for Financial Services**.

## Candidate objective

Build an evaluation platform that compares an approved baseline agent with a candidate release and produces an evidence-based recommendation:

- **PASS**
- **REVIEW**
- **FAIL**

## What is provided

- Two runnable mock IT Operations Support agents
  - Version A: approved baseline
  - Version B: candidate release
- Common REST API contract
- 24 golden test evaluation dataset in JSON and CSV
- Synthetic approved knowledge documents
- Release-policy and sample-pricing configuration
- Example API client
- Basic health tests
- Docker Compose startup

## What you must build

1. Batch execution against both agent versions
2. Accuracy evaluation
3. Groundedness and unsupported-claim evaluation
4. Relevance evaluation
5. Completeness evaluation
6. Latency, token and cost analytics
7. Per-version scorecards
8. Regression detection
9. PASS, REVIEW or FAIL recommendation with evidence
10. Executive dashboard
11. Engineering dashboard
12. Persistent evaluation-result storage

> Do not treat the supplied agent output as an evaluation result. Your framework must independently score and compare it.
------------
## Expected Deliverables

### Deliverable 1 – Evaluation Engine
- Run batch evaluations against Agent Version A and Agent Version B
- Capture and store execution results

### Deliverable 2 – Multi-Dimensional Scoring
Generate scores for:
- Accuracy
- Groundedness
- Relevance
- Completeness

### Deliverable 3 – Performance Analytics
Capture:
- Response Time
- Input Tokens
- Output Tokens
- Total Tokens
- Estimated Cost

### Deliverable 4 – Version Comparison
Compare Baseline vs Candidate and highlight:
- Improvements
- Regressions
- No Material Change

### Deliverable 5 – Release Readiness Assessment
Generate:
- PASS
- REVIEW
- FAIL

with supporting evidence.

### Deliverable 6 – Executive Dashboard
Display:
- Overall Quality Score
- Pass Rate
- Accuracy
- Groundedness
- Latency
- Cost
- Release Recommendation

### Deliverable 7 – Engineering Dashboard
Display:
- Failed Test Cases
- Metric Breakdown
- Regression Analysis
- Latency Distribution
- Cost Analysis
- Top Failure Categories
-------
## Repository structure

```text
.
├── agents/
│   ├── common/
│   ├── version_a/
│   └── version_b/
├── approved_knowledge/
├── configuration/
├── datasets/
├── examples/
├── tests/
├── .env.example
├── docker-compose.yml
└── requirements.txt
```

## Prerequisites

- Python 3.10+
- Git
- Docker and Docker Compose, recommended
- curl or Postman
- VS Code or another Python IDE

No paid LLM API is required for the supplied deterministic mock agents. Teams may optionally use an external or local LLM judge for evaluation.

## Quick start with Docker

```bash
git clone <YOUR-REPOSITORY-URL>
cd enterprise-agent-evaluation-prerequisite
docker compose up --build
```

Services:

- Agent A: `http://localhost:8001`
- Agent B: `http://localhost:8002`

Validate:

```bash
curl http://localhost:8001/health
curl http://localhost:8002/health
```

## Local Python setup

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install and run:

```bash
pip install -r requirements.txt
uvicorn agents.version_a.api:app --port 8001
```

Open a second terminal:

```bash
uvicorn agents.version_b.api:app --port 8002
```

## API contract

### Health

```text
GET /health
```

### Version

```text
GET /version
```

### Ask

```text
POST /ask
```

Request:

```json
{
  "test_case_id": "TC001",
  "question": "What is a Sev1 incident?"
}
```

Response includes:

- agent version
- response text
- retrieved approved context
- citations
- input, output and total token estimates
- latency
- execution status

Try the included client:

```bash
python examples/invoke_agent.py --base-url http://localhost:8001 --test-case-id TC001 --question "What is a Sev1 incident?"
```

## Dataset

Use either:

- `datasets/golden_test_dataset.json`
- `datasets/golden_test_dataset.csv`

Fields include expected answer, expected facts, approved document IDs, criticality, required points and prohibited claims.

## Approved knowledge

Only documents under `approved_knowledge/` are approved grounding sources. The supplied information is synthetic and intended only for the hackathon.

## Release policy

`configuration/release_policy.yaml` contains sample quality, performance, cost and regression thresholds. Your implementation must load the policy rather than hard-code it.

## Suggested result data model

At minimum, persist:

- run ID and timestamp
- test-case ID
- agent version
- actual response
- retrieved context and citations
- metric scores and explanations
- latency and tokens
- estimated cost
- pass/fail status
- regression classification
- final release recommendation

## Required demonstration

Your final demonstration should show:

1. Both agent versions are reachable.
2. The full dataset runs against both versions.
3. Scores are generated for every test case.
4. Failed and unsupported responses are visible.
5. Candidate metrics are compared with baseline metrics.
6. Regressions and improvements are highlighted.
7. The policy generates PASS, REVIEW or FAIL with reasons.
8. Executive and engineering dashboards show supporting evidence.

## Scope boundary

The repository intentionally does **not** include:

- evaluation algorithms
- LLM-judge prompts
- evaluation-result database schema
- regression engine
- release-decision implementation
- completed dashboards
- reference solution

## Data and security

- All names, policies and records are synthetic.
- Never commit secrets or API keys.
- Copy `.env.example` to `.env` for local configuration.
- Keep `.env` excluded through `.gitignore`.

--------------
## Important

This repository intentionally provides:
- Agent Version A
- Agent Version B
- Golden Test Dataset
- Approved Knowledge Sources
- Sample Policies and Configurations

The Evaluation Engine, Scoring Logic, Regression Detection, Release Recommendation Engine, Persistence Layer, and Dashboards are NOT provided and must be implemented by participants.
