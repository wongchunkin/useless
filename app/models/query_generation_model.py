from typing import List, Optional
from pydantic import BaseModel, Field


class QueryGenerationOutputModel(BaseModel):
    data: str


class QueryGenerationExampleModel(BaseModel):
    input: str
    output: str


class QueryGenerationColumnModel(BaseModel):
    name: str
    description: Optional[str] = None
    type: str


class QueryGenerationForeignKeyReferencesModel(BaseModel):
    table_name: str
    column_name: str


class QueryGenerationForeignKeyModel(BaseModel):
    name: str
    references: QueryGenerationForeignKeyReferencesModel


class QueryGenerationTableModel(BaseModel):
    name: str
    description: Optional[str] = None


class QueryGenerationSchemaModel(BaseModel):
    table: QueryGenerationTableModel
    columns: List[QueryGenerationColumnModel]
    primary_keys: Optional[List[str]] = []
    foreign_keys: Optional[List[QueryGenerationForeignKeyModel]] = []


class QueryGenerationModel(BaseModel):
    question: str
    json_schema: List[QueryGenerationSchemaModel] = Field(..., alias="schema")
    examples: List[QueryGenerationExampleModel]
    engine: str
