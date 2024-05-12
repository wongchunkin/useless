import json
from dotenv import load_dotenv
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from fastapi.encoders import jsonable_encoder
from app.models import DataSummarizationModel, DataSummarizationOutputModel
from app.prompts import DATA_SUMMARIZATION_PROMPT

load_dotenv()


class DataSummarizationChain:
    def invoke(self, data: DataSummarizationModel) -> DataSummarizationOutputModel:
        context = json.dumps(data.context)
        json_compatible_schema = jsonable_encoder(data.json_schema)
        schema = json.dumps(json_compatible_schema)
        output_parser = StrOutputParser()
        chat = ChatGroq(temperature=0, model_name="llama3-70b-8192")
        prompt = ChatPromptTemplate.from_messages(
            [("human", DATA_SUMMARIZATION_PROMPT)]
        )
        chain = prompt | chat | output_parser
        output = chain.invoke(
            {"question": data.question, "schema": schema, "context": context}
        )
        return {"data": output}
