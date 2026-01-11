# private
# protected
# public

class parent:
    def __init__(self):
        self.__private_var = "I am private"
        self._protected_var = "I am protected"

    def get_private_var(self):
        print(self.__private_var)


class child(parent):
    def access_vars(self):
        print(self._protected_var)
        # try:
        self.get_private_var()
        # print(self.__private_var)
        # except AttributeError:
        #     print("Cannot access private variable directly")


c = child()
c.access_vars()
print(c.__private_var)
