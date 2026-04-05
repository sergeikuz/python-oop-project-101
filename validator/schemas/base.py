from abc import ABC, abstractmethod
from typing import Any, Callable


class BaseSchema(ABC):
    def __init__(self) -> None:
        self._validators: dict[str, Callable[..., bool]] = {}
        self._required: bool = False
        self._tests: dict[str, tuple[Any, ...]] = {}

    def required(self) -> "BaseSchema":
        self._required = True
        return self

    def test(self, name: str, *args) -> "BaseSchema":
        self._tests[name] = args
        return self

    def _run_tests(self, data) -> bool:
        for name, args in self._tests.items():
            fn: Callable[..., bool] | None = self._validators.get(name)
            if fn and not fn(data, *args):
                return False
        return True

    def _check_required(self, data) -> bool:
        if self._required and data is None:
            return False
        return True

    def _check_empty_string(self, data: str) -> bool:
        if self._required and data == "":
            return False
        return True

    @abstractmethod
    def is_valid(self, data) -> bool:
        pass
