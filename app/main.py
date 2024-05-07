from fastapi import FastAPI
from app.chains.api_answer_chain import APIAnswerChain
from app.chains.extraction_chain import ExtractionChain
from app.chains.sql_query_chain import SQLQueryChain
from app.models.api_answer_model import APIAnswerModel, APIAnswerOutputModel
from app.models.extraction_model import ExtractionModel, ExtractionOutputModel
from app.models.sql_query_model import SQLQueryModel, SQLQueryOutputModel

app = FastAPI()
v1 = FastAPI()

api_answer_chain = APIAnswerChain()
extraction_chain = ExtractionChain()
sql_query_chain = SQLQueryChain()


@v1.post("/summarize")
def api_answer(data: APIAnswerModel) -> APIAnswerOutputModel:
    return api_answer_chain.invoke(data)


@v1.post("/extract")
def extraction(data: ExtractionModel) -> ExtractionOutputModel:
    return extraction_chain.invoke(data)


@v1.post("/sqlQuery")
def sql_query(data: SQLQueryModel) -> SQLQueryOutputModel:
    return sql_query_chain.invoke(data)


app.mount("/api/v1", v1)
