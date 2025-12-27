# comparsion or operator?
input1= input("Do you want to make a Comparsion (c) or an arithmetic Operation(o)?")

#case comparsion
if input1 == "c" or input1 == "C":
    num1=int(input("Please give the first number for the comparsion"))
    num2=int(input("Please give the second number for the comparsion"))
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1< num2:
        print(f"{num2} is greater than {num1}")
    else:
        print(f"{num1} equals {num2}")
#case arithmetic operation
if input1 == "o" or input1 == "O":
    num1=int(input("Please give the first number for the operation"))
    num2=int(input("Please give the second number for the operation"))
    operation = input("Do you want to do a Divison(d), Addition(a), Multiplication(m), or a Subtraction(s)?")
    if operation == "s":
        print(f"The Result is {num1 - num2}")
    elif operation == "m":
        print(f"The Result is {num1 * num2}")
    elif operation == "a":
        print(f"The Result is {num1 + num2}")
    else:
        print(f"The Result is {num1 / num2}")        