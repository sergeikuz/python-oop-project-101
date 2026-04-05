from validator.schemas.base import BaseSchema


class StringSchema(BaseSchema):
    def __init__(self) -> None:
        super().__init__()
        self._contains: str | None = None
        self._min_len: int | None = None

    def contains(self, substring: str) -> "StringSchema":
        self._contains = substring
        return self

    def min_len(self, length: int) -> "StringSchema":
        self._min_len = length
        return self

    def is_valid(self, data) -> bool:
        if not self._check_required(data):
            return False

        if data is not None and not isinstance(data, str):
            return False

        if not self._check_empty_string(data):
            return False

        if self._min_len is not None and len(data) < self._min_len:
            return False

        if self._contains is not None and self._contains not in data:
            return False

        return self._run_tests(data)
