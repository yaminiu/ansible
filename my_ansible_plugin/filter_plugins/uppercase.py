# uppercase.py

class FilterModule(object):
    def filters(self):
        return {
            'to_uppercase': self.to_uppercase,
        }

    def to_uppercase(self, value):
        if isinstance(value, str):
            return value.upper()
        else:
            raise ValueError("Input must be a string")