# create a class called Human
# add an attribute leg_count with the value of 4
# add a method called get_gender() that returns "Unknown" in the Human class
# create another class called Man that extends Human

class Human:
    leg_count = 4

    def get_gender(self):
        return "Unknown"


class Man(Human):
    def get_gender(self):
        return "Man"


"""
class Vehicle:
    model = "Unknown"
    make = "Unknown"
    production_year = 1990

    def print_vehicle_info(self):
        print("\n Vehicle{", self.model, ",", self.make + "}")

class Car(Vehicle):

    wheel_count = 4

    def __init__(self, make, model):
        self.model = model
        self.make = make

class Plane(Vehicle):
    model = "Aeroplane"
    make = "Boeing"

vehicle1 = Vehicle()
vehicle1.print_vehicle_info()

car1 = Car("Toyota", "Camery")
car1.print_vehicle_info()

plan1 = Plane()
plan1.print_vehicle_info()"""
