from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class SchemaGenerationColumnModel(BaseModel):
    name: str
    description: Optional[str] = None
    type: str


class SchemaGenerationModel(BaseModel):
    data: List[Dict[str, Any]]


class SchemaGenerationOutputModel(BaseModel):
    data: List[SchemaGenerationColumnModel]
