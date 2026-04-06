from validator.schemas.base import BaseSchema


class ListSchema(BaseSchema):
    def __init__(self) -> None:
        super().__init__(expected_type=list)
        self._sizeof: int | None = None

    def sizeof(self, length: int) -> "ListSchema":
        self._sizeof = length
        return self

    def is_valid(self, data) -> bool:
        if not self._check_required(data):
            return False

        if self._sizeof is not None and len(data) < self._sizeof:
            return False

        return self._run_tests(data)
