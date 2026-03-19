from validator.schemas.dict_schema import DictSchema
from validator.schemas.list_schema import ListSchema
from validator.schemas.number_schema import NumberSchema
from validator.schemas.string_schema import StringSchema


class Validator:

    def string(self):
        return StringSchema()

    def number(self):
        return NumberSchema()

    def list(self):
        return ListSchema()

    def dict(self):
        return DictSchema()
