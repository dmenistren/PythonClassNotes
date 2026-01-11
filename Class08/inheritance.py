# single parent-child inheritance example


class father():
    def func1(self):
        print("This is function 1 from parent class")


class mother:
    def func3(self):
        print("This is function 2 from mother class")


class child2(father, mother):
    def func2(self):
        print("This is function 2 from child class")


class child3(father, mother):

    def func3(self):
        super().func3()
        print("This is function 3 from child2 class")

    def func4(self):
        print("This is function 4 from child3 class")


a = child3()
a.func4()
a.func3()
# a.func2()
a.func1()
