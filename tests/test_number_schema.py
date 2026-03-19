from validator.validator import Validator


class TestValidatorNumberSchema:
    def test_required_valid(self):
        validator = Validator()
        scheme = validator.number()
        scheme.required()
        assert scheme.is_valid(3) is True
        assert scheme.is_valid(42) is True
        assert scheme.is_valid(-7) is True
        assert scheme.is_valid(0) is True

    def test_required_invalid(self):
        validator = Validator()
        scheme = validator.number()
        scheme.required()
        assert scheme.is_valid(None) is False
        assert scheme.is_valid("") is False
        assert scheme.is_valid("a") is False

    def test_positive_valid(self):
        validator = Validator()
        scheme = validator.number()
        scheme.required().positive()
        assert scheme.is_valid(1) is True
        assert scheme.is_valid(42) is True

    def test_positive_invalid(self):
        validator = Validator()
        scheme = validator.number()
        scheme.positive()
        assert scheme.is_valid(0) is False
        assert scheme.is_valid(-7) is False

        scheme2 = validator.number()
        scheme2.required().positive()
        assert scheme2.is_valid(-42) is False
        assert scheme2.is_valid(-101) is False

    def test_range_valid(self):
        validator = Validator()
        scheme = validator.number()
        scheme.range(-5, 5)
        assert scheme.is_valid(-5) is True
        assert scheme.is_valid(5) is True
        assert scheme.is_valid(0) is True

    def test_range_invalid(self):
        validator = Validator()
        scheme = validator.number()
        scheme.range(-5, 5)
        assert scheme.is_valid(-7) is False
        assert scheme.is_valid(7) is False
        assert scheme.is_valid(42) is False

    def test_range_and_positive_invalid(self):
        validator = Validator()
        scheme = validator.number()
        scheme.positive().range(-5, 5)
        assert scheme.is_valid(-5) is False
        assert scheme.is_valid(-3) is False
        assert scheme.is_valid(0) is False

    def test_range_and_positive_valid(self):
        validator = Validator()
        scheme = validator.number()
        scheme.positive().range(-5, 5)
        assert scheme.is_valid(1) is True
        assert scheme.is_valid(3) is True
        assert scheme.is_valid(5) is True

