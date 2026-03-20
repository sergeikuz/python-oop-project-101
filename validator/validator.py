from validator.schemas.dict_schema import DictSchema
from validator.schemas.list_schema import ListSchema
from validator.schemas.number_schema import NumberSchema
from validator.schemas.string_schema import StringSchema


class Validator:
    _TYPE_MAP = {
        'string': StringSchema,
        'number': NumberSchema,
        'list': ListSchema,
        'dict': DictSchema,
    }

    def __init__(self):
        self._custom_validators = {}

    def string(self):
        schema = StringSchema()
        schema._validators = self._custom_validators.get('string', {})
        return schema

    def number(self):
        schema = NumberSchema()
        schema._validators = self._custom_validators.get('number', {})
        return schema

    def list(self):
        schema = ListSchema()
        schema._validators = self._custom_validators.get('list', {})
        return schema

    def dict(self):
        schema = DictSchema()
        schema._validators = self._custom_validators.get('dict', {})
        return schema

    def add_validator(self, type: str, name: str, fn):
        if type not in self._TYPE_MAP:
            raise ValueError(f"Unsupported type: {type}")
        if type not in self._custom_validators:
            self._custom_validators[type] = {}
        self._custom_validators[type][name] = fn
