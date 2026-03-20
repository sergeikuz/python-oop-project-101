class DictSchema:
    def __init__(self):
        self.conditions = {
            'required': False,
            'shape': None,
        }
        self._validators = {}

    def shape(self, schema_dict: dict):
        """
        Задаёт структуру проверяемого словаря.

        Args:
            schema_dict (dict): словарь, где ключи — имена полей,
                значения — схемы валидации (StringSchema, NumberSchema и т. д.)
        """
        self.conditions['shape'] = schema_dict
        return self

    def required(self):
        """Помечает схему как обязательную."""
        self.conditions['required'] = True
        return self

    def is_valid(self, data) -> bool:
        """
        Проверяет, соответствует ли данные заданной схеме.

        Args:
            data: данные для валидации.

        Returns:
            bool: True, если данные валидны, иначе False.
        """
        if self.conditions['required']:
            if data is None:
                return False
            if not isinstance(data, dict):
                return False

        if data is None:
            return True

        if self.conditions['shape'] is None:
            return isinstance(data, dict)

        expected_keys = set(self.conditions['shape'].keys())
        actual_keys = set(data.keys())

        if not expected_keys.issubset(actual_keys):
            return False

        for key, schema in self.conditions['shape'].items():
            value = data[key]
            if not schema.is_valid(value):
                return False

        return True
