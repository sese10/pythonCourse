# create a class called Human
# initialize the class

class Human:
    name1 = "man"
    name2 = "woman"
    group = "species"

    def get_name1_name2_group(self):
        return self.name + "." + self.group


man = Human()
print(man.name1, man.name2, man.group)

"""
class Animal:
    name = "Cow"
    group = "Mammal"

    def get_name_group(self):
        return self.name + "." + self.group

# object
cow = Animal()
print(cow.name, cow.group, cow.get_name_group())"""
