from validator.validator import Validator


class TestValidatorStringSchema:
    def test_required_valid(self):
        validator = Validator()
        scheme = validator.string()
        scheme.required()
        assert scheme.is_valid("hello") is True
        assert scheme.is_valid(" ") is True

    def test_required_invalid(self):
        validator = Validator()
        scheme = validator.string()
        scheme.required()
        assert scheme.is_valid(None) is False
        assert scheme.is_valid("") is False

    def test_min_len_valid(self):
        validator = Validator()
        scheme = validator.string()
        scheme.required().min_len(3)
        assert scheme.is_valid("abc") is True
        assert scheme.is_valid("abcd") is True

    def test_min_len_invalid(self):
        validator = Validator()
        scheme = validator.string()
        scheme.min_len(3)  # min_len без required — пустая строка валидна
        assert scheme.is_valid("ab") is False
        assert scheme.is_valid("") is False

        # Проверка с required
        scheme2 = validator.string()
        scheme2.required().min_len(3)
        assert scheme2.is_valid("ab") is False
        assert scheme2.is_valid("") is False

    def test_contains_valid(self):
        validator = Validator()
        scheme = validator.string()
        scheme.contains("hello")
        assert scheme.is_valid("hello world") is True
        assert scheme.is_valid("say hello") is True
        assert scheme.is_valid("hello") is True

    def test_contains_invalid(self):
        validator = Validator()
        scheme = validator.string()
        scheme.contains("hello")
        assert scheme.is_valid("world") is False
        assert scheme.is_valid("hi") is False
        assert scheme.is_valid("") is False

    def test_no_conditions_always_valid(self):
        validator = Validator()
        scheme = validator.string()  # создаём схему без условий
        assert scheme.is_valid("any") is True
        assert scheme.is_valid("") is True
        assert scheme.is_valid(None) is True

    def test_multiple_conditions_all_pass(self):
        validator = Validator()
        scheme = validator.string()
        scheme.required().min_len(5).contains("test")
        assert scheme.is_valid("this is a test string") is True

    def test_multiple_conditions_one_fails(self):
        validator = Validator()
        scheme1 = validator.string()
        scheme1.required().min_len(10).contains("test")

        assert scheme1.is_valid("test") is False
        assert scheme1.is_valid("very long string") is False

    def test_chaining_methods(self):
        validator = Validator()
        scheme = validator.string()
        scheme.required().min_len(2).contains("ab")

        assert scheme.is_valid("abc") is True
        assert scheme.is_valid("ab") is True
        assert scheme.is_valid("a") is False
        assert scheme.is_valid("cd") is False

    def test_conditions_(self):
        v = Validator()
        assert v.string().min_len(10).min_len(4).is_valid('Hexlet') is True

    def test_edge_cases(self):
        validator = Validator()

        # min_len(0) — любая строка проходит
        scheme1 = validator.string()
        scheme1.min_len(0)
        assert scheme1.is_valid("") is True
        assert scheme1.is_valid("a") is True

        # min_len(1) — пустая строка не проходит
        scheme2 = validator.string()
        scheme2.min_len(1)
        assert scheme2.is_valid("a") is True
        assert scheme2.is_valid("") is False

        # contains("") — пустая подстрока содержится в любой строке
        scheme3 = validator.string()
        scheme3.contains("")
        assert scheme3.is_valid("anything") is True
        assert scheme3.is_valid("") is True

        # contains("a") — строка должна содержать "a"
        scheme4 = validator.string()
        scheme4.contains("a")
        assert scheme4.is_valid("a") is True
        assert scheme4.is_valid("abc") is True
        assert scheme4.is_valid("bc") is False
