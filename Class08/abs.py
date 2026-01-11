from abc import ABC, abstractmethod


class car(ABC):

    @abstractmethod
    def mileage(self):
        pass

    @abstractmethod
    def fuel_capacity(self):
        pass


class innova(car):
    def feature(self):
        print("This is innova car")

    def mileage(self):
        print("Mileage is 15 km/l")

    def fuel_capacity(self):
        print("Fuel capacity is 42 liters")


inn = innova()
inn.feature()
inn.mileage()
inn.fuel_capacity()
