from typing import List, Optional
from pydantic import BaseModel, Field


class SQLQueryOutputModel(BaseModel):
    data: str


class SQLQueryExampleModel(BaseModel):
    input: str
    output: str


class SQLQueryColumnModel(BaseModel):
    name: str
    description: Optional[str] = None
    type: str


class SQLQueryForeignKeyReferencesModel(BaseModel):
    table_name: str
    column_name: str


class SQLQueryForeignKeyModel(BaseModel):
    name: str
    references: SQLQueryForeignKeyReferencesModel


class SQLQueryTableModel(BaseModel):
    name: str
    description: Optional[str] = None


class SQLQuerySchemaModel(BaseModel):
    table: SQLQueryTableModel
    columns: List[SQLQueryColumnModel]
    primary_keys: List[str]
    foreign_keys: Optional[List[SQLQueryForeignKeyModel]] = []


class SQLQueryModel(BaseModel):
    question: str
    json_schema: List[SQLQuerySchemaModel] = Field(..., alias="schema")
    examples: List[SQLQueryExampleModel]
    engine: str
