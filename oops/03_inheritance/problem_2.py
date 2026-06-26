class Vehicle:
    def start_engine(self):
        print("Vehicle Engine Started")

class Car(Vehicle):
    def start_engine(self):
        print("Car Engine Started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike Engine Started")

class Truck(Vehicle):
    def start_engine(self):
        print("Truck Engine Started")

car = Car()

car.start_engine()