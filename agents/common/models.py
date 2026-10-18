from typing import List
from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    test_case_id: str = Field(min_length=1)
    question: str = Field(min_length=2)

class ContextItem(BaseModel):
    document_id: str
    document_name: str
    content: str

class AskResponse(BaseModel):
    test_case_id: str
    agent_version: str
    response: str
    retrieved_context: List[ContextItem]
    citations: List[str]
    input_tokens: int
    output_tokens: int
    total_tokens: int
    model: str
    latency_ms: int
    status: str
