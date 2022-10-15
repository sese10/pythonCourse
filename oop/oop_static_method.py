# create a class called Utilities
# create a static method called print_name which accepts a parameter, and prints out the parameter.
# invoke the static method print_name()

class Utilities:

    @staticmethod
    def print_name(num1, num2):
        return num1 + num2


print("1 + 1 =", Utilities.print_name(1, 1))




"""
class Calculator:

    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def multiply(num1, num2):
        return num1 + num2

    @staticmethod
    def divide(num1, num2):
        return num1 + num2

Calculator.add = staticmethod(Calculator.add)

print("1 + 1", Calculator.add(1,1))
print("2 * 2", Calculator.add(2,2))
print("100/2", Calculator.add(100,2))"""
