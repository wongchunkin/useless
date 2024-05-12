from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class DataExtractionOutputModel(BaseModel):
    data: Dict[str, Any]


class DataExtractionExampleModel(BaseModel):
    input: str
    output: Dict[str, Any]


class DataExtractionEnumModel(BaseModel):
    description: str
    value: str | int


class DataExtractionSchemaModel(BaseModel):
    name: str
    description: str
    type: str
    enum: Optional[List[DataExtractionEnumModel]] = None


class DataExtractionModel(BaseModel):
    question: str
    json_schema: List[DataExtractionSchemaModel] = Field(..., alias="schema")
    examples: List[DataExtractionExampleModel]
