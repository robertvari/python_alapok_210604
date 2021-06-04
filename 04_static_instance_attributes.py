class Person:
    name = "Csaba"  # static attribute
    address = "Budapest"
    age = 30
    phone = "0630 345245"


class Person2:
    name = "Kriszta"

    def __init__(self):
        print("A new person is born!")
        self.name = "Robert"  # instance attribute


p1 = Person()
p2 = Person()

print(p1.name)
p1.name = "kriszta"
p1.email = "kriszta@gmail.com"
Person.name = "kriszta"
print(p1.name)
print(p1.email)
print(Person.name)