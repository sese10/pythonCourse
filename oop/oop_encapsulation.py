# create a class called Hunt
# create a private attribute called __weapon with the value "Assault Rifle" in the Hunt class
# create a method get_weapon() that returns "Not Available" in the Hunt class
# instantiate an object of the Hunt class
# print the value of get_weapon() from the object instance

class Hunt:
    __weapon = "Assault Rifle"
    __not_weapon = "Not Available"

    def get_weapon(self):
        value = self.__not_weapon
        return value


hunt = Hunt()
print(hunt.get_weapon())

"""
class User:

    __first_name = "Testify"
    __last_name = "QA"
    __attendance = 1

    def get_name(self):
        return "User-" + self.__first_name

    def get_attendance(self):
        value = self.__attendance * 20
        return value


user = User()
print(user.get_name())
print(user.get_attendance()) """
