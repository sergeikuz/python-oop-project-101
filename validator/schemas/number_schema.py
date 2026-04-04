from validator.schemas.base import BaseSchema


class NumberSchema(BaseSchema):
    def __init__(self) -> None:
        super().__init__()
        self._positive: bool = False
        self._range: tuple | None = None

    def positive(self) -> "NumberSchema":
        self._positive = True
        return self

    def range(self, min_val: int | float, max_val: int | float) -> "NumberSchema":
        self._range = (min_val, max_val)
        return self

    def is_valid(self, data) -> bool:
        if data is not None and not isinstance(data, (int, float)):
            return False

        if not self._check_required(data):
            return False

        if data is None:
            return True

        if self._positive and data <= 0:
            return False

        if self._range is not None:
            min_val, max_val = self._range
            if not (min_val <= data <= max_val):
                return False

        return self._run_tests(data)
