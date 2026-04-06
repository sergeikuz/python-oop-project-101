from abc import ABC, abstractmethod
from typing import Any, Callable, Optional, Tuple, Type, Union


class BaseSchema(ABC):
    def __init__(
        self,
        expected_type: Optional[Union[Type, Tuple[Type, ...]]] = None,
    ) -> None:
        self._validators: dict[str, Callable[..., bool]] = {}
        self._required: bool = False
        self._tests: dict[str, tuple[Any, ...]] = {}
        self._expected_type = expected_type

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

    def _check_required(self, data: Any) -> bool:
        return all([self._check_empty_string(data),
                   self._check_isinstance(data),
                   self._check_with_none(data)])

    def _check_with_none(self, data: Any) -> bool:
        if self._required and data is None:
            return False
        return True

    def _check_empty_string(self, data: Any) -> bool:
        if self._required and data == "":
            return False
        return True

    def _check_isinstance(self, data: Any) -> bool:
        if self._required and self._expected_type is not None:
            if not isinstance(data, self._expected_type):
                return False
        return True

    @abstractmethod
    def is_valid(self, data) -> bool:
        pass
