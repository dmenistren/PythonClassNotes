# import demo

from demo import test as demo_test


def test():
    print("This is the main file.")


def add(a,b):
    """
    a: int (first number)
    b: int (second number)
    return: int (sum of a and b)
    """
    return a + b

def name(value="Guest"):
    """
    value: str (get the string value to greet)
    """
    demo_test()
    print(f"Hello, {value}!")


name()
name("Alice")

a = "hello"
print(a[::-1])
