# create a class called User
# create a private attribute called __password with the value "password" in the User class
# create a method get_password() that returns self.__password in the User class
# create another class called ActiveUser that inherits from the User class
# create a method get_password() that returns "********" in the ActiveUser class
# instantiate an object of the ActiveUser class
# print the value of get_password() from the object instance

class User:
    __password = "password"

    def get_password(self):
        return self.__password


class ActiveUser(User):

    def get_password(self):
        return "*****"


active_user = ActiveUser()
print(active_user.get_password())

"""
class LoginSession:

    __email = "user@test.com"
    __password = "password"

    def get_email(self):
        return self.__email

    def get_password(self):
        return "**********"

session = LoginSession()
print(session.get_email())
print(session.get_password())"""
