class Person:
    name = "Csaba"
    address = "Budapest"
    age = 30
    phone = "0630 345245"

    @staticmethod
    def report():
        print("-"*50)

        print(f"Name: {Person.name}")
        print(f"Address: {Person.address}")
        print(f"Age: {Person.age}")
        print(f"Phone: {Person.phone}")

        print("-"*50)


print(Person.name)