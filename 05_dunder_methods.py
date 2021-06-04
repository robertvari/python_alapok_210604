class Person:
    def __init__(self, name, address=None, age=None):
        self.name = name
        self.address = address
        self.age = age

    def __str__(self):
        return f"Name: {self.name} Address: {self.address} Age: {self.age}"

    def __repr__(self):
        return self.name

    def __add__(self, other):
        return self.age + other.age

p1 = Person("Robert", "Budapest", 24)
p2 = Person("Kriszta", "Debrecen", 21)
p3 = Person("Csaba")

print(p1 + p2)