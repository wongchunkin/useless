import json
from dotenv import load_dotenv
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from fastapi.encoders import jsonable_encoder
from app.models import DataExtractionModel, DataExtractionOutputModel
from app.prompts import DATA_EXTRACTION_PROMPT

load_dotenv()


class DataExtractionChain:
    def invoke(self, data: DataExtractionModel) -> DataExtractionOutputModel:
        json_compatible_examples = jsonable_encoder(data.examples)
        examples = json.dumps(json_compatible_examples)
        json_compatible_schema = jsonable_encoder(data.json_schema)
        schema = json.dumps(json_compatible_schema)
        output_parser = StrOutputParser()
        chat = ChatGroq(temperature=0, model_name="llama3-70b-8192")
        prompt = ChatPromptTemplate.from_messages([("human", DATA_EXTRACTION_PROMPT)])
        chain = prompt | chat | output_parser
        output = chain.invoke(
            {"question": data.question, "schema": schema, "examples": examples}
        )
        json_output = json.loads(output)
        return {"data": json_output}
