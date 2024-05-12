from fastapi import FastAPI
from app.chains import (
    DataSummarizationChain,
    SchemaGenerationChain,
    DataExtractionChain,
    QueryGenerationChain,
)
from app.models import (
    DataSummarizationModel,
    DataSummarizationOutputModel,
    SchemaGenerationModel,
    SchemaGenerationOutputModel,
    DataExtractionModel,
    DataExtractionOutputModel,
    QueryGenerationModel,
    QueryGenerationOutputModel,
)

app = FastAPI()
v1 = FastAPI()

data_summarization_chain = DataSummarizationChain()
data_extraction_chain = DataExtractionChain()
query_generation_chain = QueryGenerationChain()
schema_generation_chain = SchemaGenerationChain()


@v1.post("/structured/dataSummarization")
def data_summarization(data: DataSummarizationModel) -> DataSummarizationOutputModel:
    return data_summarization_chain.invoke(data)


@v1.post("/structured/dataExtraction")
def data_extraction(data: DataExtractionModel) -> DataExtractionOutputModel:
    return data_extraction_chain.invoke(data)


@v1.post("/database/schemaGeneration")
def schema_generation(data: SchemaGenerationModel) -> SchemaGenerationOutputModel:
    return schema_generation_chain.invoke(data)


@v1.post("/database/queryGeneration")
def query_generation(data: QueryGenerationModel) -> QueryGenerationOutputModel:
    return query_generation_chain.invoke(data)


app.mount("/api/v1", v1)
