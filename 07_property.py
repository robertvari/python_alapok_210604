class Person:
    def __init__(self, name, address="", age=""):
        self._full_name = name
        self._address = address
        self._age = age

    @property
    def name(self):
        print("Using name property")
        return self._full_name

    @name.setter
    def name(self, value):
        print("Using name setter")
        self._full_name = value


p1 = Person("Robert")

p1.name = "Kriszta"
print(p1.name)