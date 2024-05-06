from typing import Any, Dict, List
from pydantic import BaseModel, Field


class APIAnswerOutputModel(BaseModel):
    data: str


class APIAnswerSchemaModel(BaseModel):
    name: str
    description: str
    type: str


class APIAnswerModel(BaseModel):
    question: str
    json_schema: List[APIAnswerSchemaModel] = Field(..., alias="schema")
    context: Dict[str, Any]
