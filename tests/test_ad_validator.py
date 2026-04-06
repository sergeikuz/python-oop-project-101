from validator.validator import Validator


class TestValidatorAddSchema:
    def test_base(self):
        v = Validator()

        def starts_with(value, start):
            result = value.startswith(start)
            return result

        v.add_validator('string', 'startwith', starts_with)
        schema = v.string().test('startwith', 'H')

        is_valid = schema.is_valid('exlet')

        assert is_valid is False

        def starts_with(value, start):
            return value.startswith(start)

        v.add_validator('string', 'startwith', starts_with)
        schema = v.string().test('startwith', 'H')
        assert schema.is_valid('exlet') is False
        assert schema.is_valid('Hexlet') is True

        def greater_than_or_equal(value, min_val):
            return value >= min_val

        v.add_validator('number', 'min', greater_than_or_equal)
        schema = v.number().test('min', 5)

        assert schema.is_valid(4) is False
        assert schema.is_valid(6) is True
