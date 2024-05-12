from typing import Any, Dict, List
from app.models import (
    SchemaGenerationColumnModel,
    SchemaGenerationModel,
    SchemaGenerationOutputModel,
)


class SchemaGenerationChain:
    def _flatten_json(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        separator = "_"
        output = dict()

        def flatten(object_: Any, name: str):
            if isinstance(object_, dict):
                for key, value in object_.items():
                    flatten(value, name + key + separator)
            elif isinstance(object_, list):
                for index, item in enumerate(object_):
                    flatten(item, name + str(index) + separator)
            else:
                output[name[:-1]] = object_

        flatten(data, "")
        return output

    def _find_type(self, value: Any) -> str:
        if isinstance(value, (int, float)):
            return "number"
        if isinstance(value, bool):
            return "boolean"
        return "string"

    def _create_columns(
        self, columns: List[Dict[str, Any]]
    ) -> List[SchemaGenerationColumnModel]:
        output = []
        keys = []
        for object_ in columns:
            for key, value in object_.items():
                if key not in keys:
                    column = SchemaGenerationColumnModel(
                        name=key, type=self._find_type(value)
                    )
                    output.append(column)
                    keys.append(key)
        return output

    def invoke(self, data: SchemaGenerationModel) -> SchemaGenerationOutputModel:
        columns = self._create_columns([self._flatten_json(d) for d in data.data])
        return {"data": columns}
