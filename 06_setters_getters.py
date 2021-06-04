class Person:
    def __init__(self, name=None):
        self._name = name

    def set_name(self, value):
        assert isinstance(value, str), "Name must be of string type."
        self._name = value

    def get_name(self):
        return self._name

    def __str__(self):
        return str(self._name)


p1 = Person()
print(p1)