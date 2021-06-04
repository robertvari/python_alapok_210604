class Person:
    name = "Csaba"
    address = "Budapest"
    age = 30
    phone = "0630 345245"

    def report(self):
        print("-"*50)

        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone}")

        print("-"*50)


p = Person()
print(p.name)