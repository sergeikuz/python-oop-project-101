from validator.validator import Validator


class TestValidatorListSchema:
    def test_base(self):
        validator = Validator()
        schema = validator.list()

        assert schema.is_valid(None) is True

        schema = schema.required()

        assert schema.is_valid([]) is True
        assert schema.is_valid(['hexlet']) is True

        schema.sizeof(2)

        assert schema.is_valid(['hexlet']) is False
        assert schema.is_valid(['hexlet', 'code-basics']) is True
