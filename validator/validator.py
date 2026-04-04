from validator.schemas.dict_schema import DictSchema
from validator.schemas.list_schema import ListSchema
from validator.schemas.number_schema import NumberSchema
from validator.schemas.string_schema import StringSchema
from validator.validator_registry import ValidatorRegistry


class Validator:
    def __init__(self):
        self._registry = ValidatorRegistry()

    def add_validator(self, type: str, name: str, fn):
        self._registry.add_validator(type, name, fn)

    def string(self):
        schema = StringSchema()
        schema._validators = self._registry.get_validators('string')
        return schema

    def number(self):
        schema = NumberSchema()
        schema._validators = self._registry.get_validators('number')
        return schema

    def list(self):
        schema = ListSchema()
        schema._validators = self._registry.get_validators('list')
        return schema

    def dict(self):
        schema = DictSchema()
        schema._validators = self._registry.get_validators('dict')
        return schema
