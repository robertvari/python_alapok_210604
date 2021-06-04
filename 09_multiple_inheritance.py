class VehicleBase:
    def __init__(self):
        self.speed = 100


class Bike(VehicleBase):
    def __init__(self):
        super().__init__()
        print("I'm a Bike")


class Car(VehicleBase):
    def __init__(self):
        super().__init__()
        print("I'm a Car")


class MySpecialCar(Bike, Car):
    def __init__(self):
        super().__init__()
        print("I'm a special Car")


my_special_car = MySpecialCar()