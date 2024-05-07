from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class ExtractionOutputModel(BaseModel):
    data: Dict[str, Any]


class ExtractionExampleModel(BaseModel):
    input: str
    output: Dict[str, Any]


class ExtractionEnumModel(BaseModel):
    description: str
    value: str | int


class ExtractionSchemaModel(BaseModel):
    name: str
    description: str
    type: str
    enum: Optional[List[ExtractionEnumModel]] = None


class ExtractionModel(BaseModel):
    question: str
    json_schema: List[ExtractionSchemaModel] = Field(..., alias="schema")
    examples: List[ExtractionExampleModel]
