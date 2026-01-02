def subtraction(a,b):
    return a-b
def additon(a,b):
    return a+b
def division(a,b):
    return a /b
def multiplication(a,b):
    return a * b


def calc(a,b,operation):
    if operation == "m":
        return a * b
    elif operation == "a":
        return a * b
    elif operation == "d":
        return a / b
    elif operation == "s":
        return a-b
    else:
        return "Input is invalid"

print(calc(5,2,"m"))
