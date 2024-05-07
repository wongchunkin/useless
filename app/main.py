from fastapi import FastAPI
from app.chains.api_answer_chain import APIAnswerChain
from app.chains.extraction_chain import ExtractionChain
from app.models.api_answer_model import APIAnswerModel, APIAnswerOutputModel
from app.models.extraction_model import ExtractionModel, ExtractionOutputModel

app = FastAPI()
v1 = FastAPI()

api_answer_chain = APIAnswerChain()
extraction_chain = ExtractionChain()


@v1.post("/summarize")
def api_answer(data: APIAnswerModel) -> APIAnswerOutputModel:
    return api_answer_chain.invoke(data)


@v1.post("/extract")
def extraction(data: ExtractionModel) -> ExtractionOutputModel:
    return extraction_chain.invoke(data)


app.mount("/api/v1", v1)
