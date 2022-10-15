# create a class called Human
# add an attribute leg_count with the value of 4
# add another attribute can_walk with value of True

class Human:
    leg_count = 4
    can_walk = True

    def __init__(self, name):
        self.name = name


man = Human("Rita")
print(man.leg_count)

"""
class Animal:
    group = "mammal"
    can_walk = True

    def __init__(self, name):
        self.name = name

cat = Animal("cat")
dog = Animal("dog")
print(cat.name)
print(dog.name)"""
