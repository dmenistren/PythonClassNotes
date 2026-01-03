#Calculation logic with return and arg
def add_return(a,b):
    """
    Additon of two numbers
    Args:
        a (float): The first number
        b(float): The second number
    Returns:
        returns sum of a and b
    """
    return a + b
def sub_return(a,b):
    """
    Subtraction of two numbers
    Args:
        a (float): The first number
        b (float): The second number
    Returns:
        returns diffrence of a and b
    """
    return a-b
def mul_return(a,b):
    """
    Multiplication of two numbers
    Args:
        a (float): The first number
        b (float): The second number
    Returns:
        returns product of a and b
    """
    return a*b
def div_return(a,b):
    """
    Division of two numbers
    Args:
        a (float): The first number
        b (float): The second number
    Returns:
        returns ratio of a and b
    """
    return a/b

# Calculation logic without return
def add_noreturn(a,b):
    """
    Additon of two numbers
    Args:
        a (float): The first number
        b(float): The second number
    Returns:
        none
    """
    print(f"Result: {a+b}")
def sub_noreturn(a,b):
    """
    Subtraction of two numbers
    Args:
        a (float): The first number
        b (float): The second number
    Returns:
        none
    """
    print(f"Result: {a-b}")
def mul_noreturn(a,b):
    """
    Multiplication of two numbers
    Args:
        a (float): The first number
        b (float): The second number
    Returns:
        none
    """
    print(f"Result: {a*b}")
def div_noreturn(a,b):
    """
    Division of two numbers
    Args:
        a (float): The first number
        b (float): The second number
    Returns:
         none
    """
    print(f"Result: {a/b}")

#Calculation logic with lambda
add = lambda a,b: a+b
sub = lambda a,b: a -b
mul = lambda a,b: a * b
div = lambda a,b: a / b
def calculator():
        while True:
            try:
                num1 = float(input("Please give the first number for the calculation!"))
                num2 = float(input("Please give the second number for the calculation!"))
                calc = input("Which function type should the Calculator use? 1 function with arg and return 2 function with arg and without return and 3 lambda?")
                op = input("Which Operation do you want to do? Division(d), Multiplication(m), Subtraction(s), Addition(a) or Quit(q)?").lower()
           
                if calc == "1":
                    if op == "s":
                        print(f"Result: {sub_return(num1,num2)}")
                    elif op == "a":
                         print(f"Result: {add_return(num1,num2)}")
                    elif op == "d":
                         print(f"Result: {div_return(num1,num2)}")
                    elif op == "m":
                        print(f"Result: {mul_return(num1,num2)}")
                elif calc == "2":
                    if op == "s":
                        sub_noreturn(num1,num2)
                    elif op == "a":
                        add_noreturn(num1,num2)
                    elif op == "d":
                        div_noreturn(num1,num2)
                    elif op == "m":
                        mul_noreturn(num1,num2)
                elif calc == "3":
                    if op == "s":
                        print(f"Result: {sub(num1,num2)}")
                    elif op == "a":
                        print(f"Result: {add(num1,num2)}")
                    elif op == "d":
                        print(f"Result: {div(num1,num2)}")
                    elif op == "m":
                        print(f"Result: {mul(num1,num2)}")
                if op == "q":
                    print("Process is finishing")
                    break
            except ValueError:
                print("That's not a valid Input")
            except ZeroDivisionError:
                print("You can't divide by Zero!")





calculator()