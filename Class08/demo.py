class name:
    def __init__(self, name):
        self.name = name

    def call_name(self):
        self.test = 10
        print(f"Name is: {self.name}")

    def greet(self):
        print(self.test)
        name.farewell(self.name)
        return f"Hello, {self.name}!"

    @staticmethod  # decorator in python
    def farewell(name):
        return f"Goodbye, {name}!"


obj = name("Alice")
obj.call_name()
obj.greet()
