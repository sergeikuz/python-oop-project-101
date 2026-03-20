class StringSchema:
    def __init__(self):
        self.conditions = {
            'required': False,
            'contains': None,
            'min_len': None,
            'tests': {},
        }
        self._validators = {}

    def contains(self, substring):
        self.conditions['contains'] = substring
        return self

    def min_len(self, length: int):
        self.conditions['min_len'] = length
        return self

    def required(self):
        self.conditions['required'] = True
        return self

    def test(self, name, *args):
        self.conditions['tests'][name] = args
        return self

    def is_valid(self, data) -> bool:
        if data is None:
            return not self.conditions['required']

        if not isinstance(data, str):
            return False

        if self.conditions['required'] and data == '':
            return False

        if self.conditions['min_len'] is not None:
            if len(data) < self.conditions['min_len']:
                return False

        if self.conditions['contains'] is not None:
            if self.conditions['contains'] not in data:
                return False

        for name, args in self.conditions['tests'].items():
            fn = self._validators.get(name)
            if fn and not fn(data, *args):
                return False

        return True


