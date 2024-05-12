from fastapi import FastAPI
from app.chains import (
    APIAnswerChain,
    SchemaGenerationChain,
    ExtractionChain,
    SQLQueryChain,
)
from app.models import (
    APIAnswerModel,
    APIAnswerOutputModel,
    SchemaGenerationModel,
    SchemaGenerationOutputModel,
    ExtractionModel,
    ExtractionOutputModel,
    SQLQueryModel,
    SQLQueryOutputModel,
)

app = FastAPI()
v1 = FastAPI()

api_answer_chain = APIAnswerChain()
extraction_chain = ExtractionChain()
sql_query_chain = SQLQueryChain()
schema_generation_chain = SchemaGenerationChain()


@v1.post("/summarize")
def api_answer(data: APIAnswerModel) -> APIAnswerOutputModel:
    return api_answer_chain.invoke(data)


@v1.post("/extract")
def extraction(data: ExtractionModel) -> ExtractionOutputModel:
    return extraction_chain.invoke(data)


@v1.post("/database/schemaGeneration")
def schema_generation(data: SchemaGenerationModel) -> SchemaGenerationOutputModel:
    return schema_generation_chain.invoke(data)


@v1.post("/sqlQuery")
def sql_query(data: SQLQueryModel) -> SQLQueryOutputModel:
    return sql_query_chain.invoke(data)


app.mount("/api/v1", v1)
