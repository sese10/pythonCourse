# create an abstract class called Vehicle
# create an abstract method called drive_direction()
# create another class Car that inherits from Vehicle
# create another class Plane that inherits from Vehicle
# try running the program and fix the abstract method issues
# optionally instantiate the Car and Plane method,
# then invoke the drive_direction() in each of the object instances.
# hint: the drive_direction() method in your Car should print "Drive forward",
# while drive_direction() in your Plane class should print "Drive Upward"

import abc


class Vehicle(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def drive_direction(self):
        pass


class Car(Vehicle):
    def drive_direction(self):
        return "drive forward"


class Plane(Vehicle):
    def drive_direction(self):
        return "drive upward"


car = Car()
print(car.drive_direction())

plane = Plane()
print(plane.drive_direction())

"""
import abc


class IWebElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_name(self):
        pass

    def set_style(self, style):
        pass

class DivElement(IWebElement):

    def get_name(self):
        return "div"

    def set_style(self, style):
        print("Div Style:", style)

class SpanElement(IWebElement):

    def get_name(self):
        return "span"

    def set_style(self, style):
        print("Div Style:", style)

class ButtonElement(IWebElement):

    def get_name(self):
        return "button"

    def set_style(self, style):
        print("Div Style:", style)

div_element = DivElement()
print(div_element.get_name())
div_element.set_style("width: 100px; height: 100px")

span_element = SpanElement()
print(span_element.get_name())
div_element.set_style("border: 1px; solid: red")

button_element = ButtonElement()
print(button_element.get_name())
div_element.set_style("font-size: 10; height: 100px")"""
