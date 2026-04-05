from typing import Callable


class ValidatorRegistry:
    def __init__(self) -> None:
        self._validators: dict[str, dict[str, Callable[..., bool]]] = {}

    def add_validator(
        self,
        type_name: str,
        validator_name: str,
        fn: Callable[..., bool],
    ) -> None:
        if type_name not in self._validators:
            self._validators[type_name] = {}
        self._validators[type_name][validator_name] = fn

    def get_validators(self, type_name: str) -> dict[str, Callable[..., bool]]:
        return self._validators.get(type_name, {})
