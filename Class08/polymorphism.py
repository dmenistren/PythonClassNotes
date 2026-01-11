def name(val, test="Default"):
    return val + test


print(name("Hello ", "World"))
print(name("Hello "))


class Calculator:
    def add(self, *args):
        print(type(args))
        return sum(args)


calc = Calculator()
print(calc.add(5, 10))       # Two arguments
print(calc.add(5, 10, 15))   # Three arguments
print(calc.add(1, 2, 3, 4))
