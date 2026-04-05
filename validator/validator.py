from typing import Callable

from validator.schemas.dict_schema import DictSchema
from validator.schemas.list_schema import ListSchema
from validator.schemas.number_schema import NumberSchema
from validator.schemas.string_schema import StringSchema
from validator.validator_registry import ValidatorRegistry


class Validator:
    def __init__(self) -> None:
        self._registry: ValidatorRegistry = ValidatorRegistry()

    def add_validator(
        self,
        schema_type: str,
        name: str,
        fn: Callable[..., bool],
    ) -> None:
        self._registry.add_validator(schema_type, name, fn)

    def string(self) -> StringSchema:
        schema = StringSchema()
        schema._validators = self._registry.get_validators('string')
        return schema

    def number(self) -> NumberSchema:
        schema = NumberSchema()
        schema._validators = self._registry.get_validators('number')
        return schema

    def list(self) -> ListSchema:
        schema = ListSchema()
        schema._validators = self._registry.get_validators('list')
        return schema

    def dict(self) -> DictSchema:
        schema = DictSchema()
        schema._validators = self._registry.get_validators('dict')
        return schema
