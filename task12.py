print("\nglobal and local variable")

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