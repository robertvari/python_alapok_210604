class PersonBase:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def speak(self):
        print(f"Hello. My name is {self.name}")

    def __str__(self):
        return self.name


class Adult(PersonBase):
    def report(self):
        print(self.name, self.address, self.age)


class Child(PersonBase):
    def __init__(self, name, address, age):
        super().__init__(name, address, age)
        self.my_class = "A1"

    def speak(self):
        super().speak()
        print("I'm a child")


class Teacher(Adult):
    def __init__(self, name, address, age):
        super().__init__(name, address, age)
        self.my_school = "International Busines School"

    def speak(self):
        print("I work as a teacher")


class Employee(Adult):
    def __init__(self, name, address, age):
        super().__init__(name, address, age)

        self.my_workplace = "Tesco"


peter = Child("Peter", "Budapest", 13)
tom = Teacher("Tom", "Debrecen", 34)
christina = Employee("Christina", "Pécs", 28)

peter.speak()
tom.report()
christina.report()
