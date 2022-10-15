print("\nglobal and local variable")
# declare a global variable with name as language and the value as "Python"
# create a function, in the function declare a variable with name as language and value as "Java", then print out the variable in the function
# print out the variable name into the console
# invoke the function

name = "Testify" # global variable

def greet():
    language = "python" #local variable
    print("Name", name, "language", language)
    print(language)

def hello():
    framework = "selenium" #local variable
    print("Name", name, "framework", framework)
    print(framework)

platform = "web"

def print_platform():
    platform = "Mobile"
    print("platform", platform)


print(name)
greet()
hello()
print_platform()