from validator.validator import Validator  


class TestValidator:
    def test_required_valid(self):
        validator = Validator().required()
        assert validator.is_valid("hello") is True
        assert validator.is_valid(" ") is True

    def test_required_invalid(self):
        validator = Validator().required()
        assert validator.is_valid(None) is False
        assert validator.is_valid("") is False

    def test_min_len_valid(self):
        validator = Validator().min_len(3)
        assert validator.is_valid("abc") is True
        assert validator.is_valid("abcd") is True

    def test_min_len_invalid(self):
        validator = Validator().min_len(3)
        assert validator.is_valid("ab") is False
        assert validator.is_valid("") is False

    def test_contains_valid(self):
        validator = Validator().contains("hello")
        assert validator.is_valid("hello world") is True
        assert validator.is_valid("say hello") is True
        assert validator.is_valid("hello") is True

    def test_contains_invalid(self):
        validator = Validator().contains("hello")
        assert validator.is_valid("world") is False
        assert validator.is_valid("hi") is False
        assert validator.is_valid("") is False

    def test_no_conditions_always_valid(self):
        validator = Validator()
        assert validator.is_valid("any") is True
        assert validator.is_valid("") is True
        assert validator.is_valid(None) is True

    def test_multiple_conditions_all_pass(self):
        validator = Validator().required().min_len(5).contains("test")
        assert validator.is_valid("this is a test string") is True

    def test_multiple_conditions_one_fails(self):
        validator = Validator().required().min_len(10).contains("test")

        assert validator.is_valid("test") is False

        assert validator.is_valid("very long string") is False

    def test_chaining_methods(self):
        validator = (
            Validator()
            .required()
            .min_len(2)
            .contains("ab")
        )
        assert validator.is_valid("abc") is True
        assert validator.is_valid("ab") is True
        assert validator.is_valid("a") is False
        assert validator.is_valid("cd") is False

    def test_conditions_reset_with_string(self):
        base_validator = Validator().required().min_len(5)
        new_validator = base_validator.string()

        assert new_validator.conditions == {
            'required': False,
            'contains': None,
            'min_len': None,
        }
        assert new_validator.is_valid("") is True
        assert new_validator.is_valid(None) is True

    def test_edge_cases(self):
        validator = Validator()

        assert validator.min_len(0).is_valid("") is True
        assert validator.min_len(1).is_valid("a") is True
        assert validator.contains("").is_valid("anything") is True
        assert validator.contains("a").is_valid("a") is True
