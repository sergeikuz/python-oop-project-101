class NumberSchema:
    def __init__(self):
        self.conditions = {
            'required': False,
            'positive': False,
            'range': None,
        }

    def range(self, min_val, max_val):
        self.conditions['range'] = (min_val, max_val)
        return self

    def positive(self):
        self.conditions['positive'] = True
        return self

    def required(self):
        self.conditions['required'] = True
        return self

    def is_valid(self, data) -> bool:
        if self.conditions['required']:
            if data is None or data == '':
                return False
            if not isinstance(data, int):
                return False

        if self.conditions['positive']:
            if isinstance(data, int):
                if data <= 0:
                    return False

        if self.conditions['range'] is not None:
            min_val, max_val = self.conditions['range']
            if not (min_val <= data <= max_val):
                return False

        return True
