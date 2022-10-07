print("Parameters")
# create a function that accepts two numbers, adds the numbers and prints out the result in the console.
# create a function that return the string value "Testify Python"
# invoke/call the two functions


def add(num1=10, num2=10):
    result = num1 + num2
    print("Result", result)
add()

def course(name):
    print("Testify", name)
course("python")













"""
print("\nrequired parameter")
def greet(name):
    print("Hello", name)
greet("Testify")

print("\ndefault parameter")
def add(num1=10, num2=15):
    result = num1 + num2
    print("Result", result)
add()
add(5)
add(5, 5)

print("\nkeyword argument")
def minus(num1, num2):
    result = num1 - num2
    print("Result:", result)
minus(10, 2)

print("\narbitrary argument")
def print_value(*args):
    print("Args:", args, args[0])
#print_value()
print_value(1)
print_value(1, 2)
print_value(1, 2, 3)

print("\narbitrary keyword argument")
def print_kvalue(**kargs):
    print("Args:", kargs, kargs["num1"], kargs["num2"])
print_kvalue(num1=1, num2=2)


print("\nReturn statement")
def add_and_return(num1, num2):
    result = num1 + num2
    return result

res = add_and_return(50, 50)
print("50 + 50:", res)

def check_number(number):
    if number > 5:
        return
    print("Number:", number)
check_number(1)
check_number(2)
check_number(3)
check_number(4)
check_number(5)
check_number(6)"""
