class ListSchema:
    def __init__(self):
        self.conditions = {
            'required': False,
            'sizeof': None,
        }

    def sizeof(self, length: int):
        self.conditions['sizeof'] = length
        return self

    def required(self):
        self.conditions['required'] = True
        return self

    def is_valid(self, data) -> bool:
        if self.conditions['required']:
            if not isinstance(data, list):
                return False

        if self.conditions['sizeof'] is not None:
            if len(data) < self.conditions['sizeof']:
                return False

        return True
