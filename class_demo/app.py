# constructor or initialization file
# Destructor class
class data:
    def __init__(self, a, b):
        print("Data class initialized")
        self.a = a
        self.b = b

    def add(self, a, b):
        return a + b

    def add_value(self):
        value = self.add(self.a, self.b)
        print(value)

    def __del__(self):
        print("Data class destroyed")


data = data(5, 10)
print(data.a, data.b)
print(data.add_value())
del data
