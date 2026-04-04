from validator.schemas.base import BaseSchema


class DictSchema(BaseSchema):
    def __init__(self) -> None:
        super().__init__()
        self._shape: dict | None = None

    def shape(self, schema_dict: dict) -> "DictSchema":
        self._shape = schema_dict
        return self

    def is_valid(self, data) -> bool:
        if not self._check_required(data):
            return False

        if data is None:
            return True

        if not isinstance(data, dict):
            return False

        if self._shape is None:
            return True

        if not set(self._shape.keys()).issubset(set(data.keys())):
            return False

        for key, schema in self._shape.items():
            if not schema.is_valid(data[key]):
                return False

        return True
