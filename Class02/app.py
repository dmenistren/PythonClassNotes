# what is parameters and arguments?
'''
parameters are the variables listed inside the parentheses in the function definition.
arguments are the values passed to the function when it is called.
'''

# without parameters and without return value


def check_value():
    print("hello world")


# Without parameters and with return value
def get_value():
    return 42

# With parameters and with return value


def add_values(a, b):
    return a - b

# with parameters and without return value


def print_sum(a, b):
    print(f"The sum is: {a + b}")


def hello():
    print("hello")
    pass
    print("This is after hello function")


check_value()
a = get_value()
print(a)
hello()

# add_values(a, b):
result = add_values(b=0, a=7)


print(f"The result of addition is: {result}")

print_sum(10, 15)


def name(*args):
    print(args)


name("John", "Doe", "Smith")


def name(**a):
    """
    This function accepts arbitrary keyword arguments
    and prints them as a dictionary.
    """
    print(a)


name(first="John", last="Doe", middle="Smith",
     extra="asdkjabdasjkd", another="Asdasd")


print(print.__doc__, end="\n\n ello \t")  # docstring of print function
print(input.__doc__)  # docstring of input function


print(help(name))  # help function
# print(name.__doc__)  # help function


# def add(a, b):
#     return a+b

# def add(a, b): return a+b

add = lambda a, b, c=3: a + b -c

result = add(5, 10, 10)
print(f"The result of addition is: {result}")
