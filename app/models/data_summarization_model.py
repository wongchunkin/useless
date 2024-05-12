from typing import Any, Dict, List
from pydantic import BaseModel, Field


class DataSummarizationOutputModel(BaseModel):
    data: str


class DataSummarizationSchemaModel(BaseModel):
    name: str
    description: str
    type: str


class DataSummarizationModel(BaseModel):
    question: str
    json_schema: List[DataSummarizationSchemaModel] = Field(..., alias="schema")
    context: Dict[str, Any]
