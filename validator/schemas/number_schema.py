class NumberSchema:
    def __init__(self):
        self.conditions = {
            'required': False,
            'positive': False,
            'range': None,
            'tests': {},
        }
        self._validators = {}

    def range(self, min_val, max_val):
        self.conditions['range'] = (min_val, max_val)
        return self

    def positive(self):
        self.conditions['positive'] = True
        return self

    def required(self):
        self.conditions['required'] = True
        return self

    def test(self, name, *args):
        self.conditions['tests'][name] = args
        return self

    def is_valid(self, data) -> bool:
        if self.conditions['required']:
            if data is None:
                return False
            if not isinstance(data, (int, float)):
                return False

        if data is None and not self.conditions['required']:
            return True

        if not self._is_positive(data):
            return False
        if not self._is_in_range(data):
            return False
        for name, args in self.conditions['tests'].items():
            fn = self._validators.get(name)
            if fn and not fn(data, *args):
                return False
        return True

    def _is_positive(self, data):
        if data is None:
            return True
        if self.conditions['positive']:
            if data <= 0:
                return False
        return True

    def _is_in_range(self, data):
        if data is None:
            return True
        if self.conditions['range'] is not None:
            min_val, max_val = self.conditions['range']
            if not (min_val <= data <= max_val):
                return False
        return True
