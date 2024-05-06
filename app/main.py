from fastapi import FastAPI
from app.chains.api_answer_chain import APIAnswerChain
from app.models.api_answer_model import APIAnswerModel, APIAnswerOutputModel

app = FastAPI()
v1 = FastAPI()

api_answer_chain = APIAnswerChain()


@v1.post("/summarize")
def api_answer(data: APIAnswerModel) -> APIAnswerOutputModel:
    return api_answer_chain.invoke(data)


app.mount("/api/v1", v1)
