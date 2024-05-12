import re
import json
from dotenv import load_dotenv
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from fastapi.encoders import jsonable_encoder
from app.models import QueryGenerationModel, QueryGenerationOutputModel
from app.prompts import (
    MSSQL_PROMPT,
    MYSQL_PROMPT,
    ORACLE_PROMPT,
    POSTGRES_PROMPT,
    SQLITE_PROMPT,
)

load_dotenv()


class QueryGenerationChain:
    _sql_prompts = {
        "mysql": MYSQL_PROMPT,
        "postgres": POSTGRES_PROMPT,
        "mssql": MSSQL_PROMPT,
        "oracle": ORACLE_PROMPT,
        "sqlite": SQLITE_PROMPT,
    }

    def _find_sql_query(self, output: str) -> str:
        prefix = "SQLQuery:"
        suffix = "SQLResult"
        pattern = f"{prefix}(.*?){suffix}"
        content = re.compile(pattern, re.DOTALL)
        match = content.search(output)
        return match.group(1) if match else ""

    def _find_sql_prompt(self, engine: str) -> str:
        return (
            self._sql_prompts[engine]
            if engine in self._sql_prompts
            else self._sql_prompts["sqlite"]
        )

    def invoke(self, data: QueryGenerationModel) -> QueryGenerationOutputModel:
        json_compatible_examples = jsonable_encoder(data.examples)
        examples = json.dumps(json_compatible_examples)
        json_compatible_schema = jsonable_encoder(data.json_schema)
        schema = json.dumps(json_compatible_schema)
        output_parser = StrOutputParser()
        chat = ChatGroq(temperature=0, model_name="llama3-70b-8192")
        prompt = ChatPromptTemplate.from_messages(
            [("human", self._find_sql_prompt(data.engine))]
        )
        chain = prompt | chat | output_parser
        output = chain.invoke(
            {
                "question": data.question,
                "examples": examples,
                "schema": schema,
                "top_k": 5,
            }
        )
        sql_query_output = " ".join(self._find_sql_query(output).splitlines()).strip()
        return {"data": sql_query_output}
