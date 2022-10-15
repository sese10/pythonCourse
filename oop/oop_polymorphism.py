# create a class called Human
# add an attribute leg_count with the value of 4
# add a method called get_gender() that returns "Unknown" in the Human class
# create another class called Man that extends Human
# create another class called Woman that extends Human
# in the class, Man create the method get_gender() which should return "man"
# in the class, Woman create the method get_gender() which should return "woman"
# instantiate the Man and Woman classes
# print out the value of get_gender() from the Man and Woman object instances

class Human:
    leg_count = 4

    def get_gender(self):
        return "Unknown"


class Man(Human):
    def get_gender(self):
        return "Man"


class Woman(Human):
    def get_gender(self):
        return "Woman"


man = Man()
print(man.get_gender())

woman = Woman()
print(woman.get_gender())

"""
class Vehicle:
    def drive_direction(self):
        print("Drive Forward")


class Plane(Vehicle):

    def drive_direction(self):
        print("Plane: Drive Upward")

class SubMarine(Vehicle):

    def drive_direction(self):
        print("SubMarine: Drive Downward")

vehicle = Vehicle()
vehicle.drive_direction()

plane = Plane()
plane.drive_direction()

Sub_marine = SubMarine()
Sub_marine.drive_direction()"""
