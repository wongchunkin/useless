import json
from dotenv import load_dotenv
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from fastapi.encoders import jsonable_encoder
from app.models.api_answer_model import APIAnswerModel, APIAnswerOutputModel
from app.prompts.api_answer_prompt import API_ANSWER_PROMPT

load_dotenv()


class APIAnswerChain:
    def invoke(self, data: APIAnswerModel) -> APIAnswerOutputModel:
        context = json.dumps(data.context)
        json_compatible_schema = jsonable_encoder(data.json_schema)
        schema = json.dumps(json_compatible_schema)
        output_parser = StrOutputParser()
        chat = ChatGroq(temperature=0, model_name="llama3-70b-8192")
        prompt = ChatPromptTemplate.from_messages([("human", API_ANSWER_PROMPT)])
        chain = prompt | chat | output_parser
        output = chain.invoke(
            {"question": data.question, "schema": schema, "context": context}
        )
        return {"data": output}
