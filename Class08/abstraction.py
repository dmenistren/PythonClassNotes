from abc import ABC, abstractmethod


class demo(ABC):
    @abstractmethod
    def display(self):
        pass


class demo1(demo):
    def test(self):
        print("This is test method")

    def display(self):
        print("This is display method implementation")


d = demo1()
d.display()
