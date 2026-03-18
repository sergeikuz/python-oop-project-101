class Validator:
    def __init__(self):
        self.conditions = {
            'required': False,
            'contains': None,
            'min_len': None,
        }

    def contains(self, substring):
        self.conditions['contains'] = substring
        return self

    def min_len(self, length: int):
        self.conditions['min_len'] = length
        return self

    def required(self):
        self.conditions['required'] = True
        return self

    def string(self):
        return self.__class__()

    def is_valid(self, data) -> bool:
        if self.conditions['required']:
            if data is None or data == '':
                return False

        if self.conditions['min_len'] is not None:
            if len(data) < self.conditions['min_len']:
                return False

        if self.conditions['contains'] is not None:
            if self.conditions['contains'] not in data:
                return False

        return True
