class ValidatorRegistry:
    def __init__(self):
        self._validators = {}

    def add_validator(self, type_name: str, validator_name: str, fn):
        if type_name not in self._validators:
            self._validators[type_name] = {}
        self._validators[type_name][validator_name] = fn

    def get_validators(self, type_name: str):
        return self._validators.get(type_name, {})
