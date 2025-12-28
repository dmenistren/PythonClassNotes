# comparsion or operator?
input1= input("Do you want to make a Comparsion (c) or an arithmetic Operation(o)?")

num1 = int(input("Please give the first number for the comparsion"))
num2 = int(input("Please give the second number for the comparsion"))

# case comparsion
if input1.lower() == "c":
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1< num2:
        print(f"{num2} is greater than {num1}")
    elif num1 == num2:
        print(f"{num1} equals {num2}")
    else:
        print("Invalid Input")

# Case arithmetic operation
if input1.lower() == "o":
    operation = input("Do you want to do a Divison(d), Addition(a), Multiplication(m), or a Subtraction(s)?")
    if operation.lower() == "s":
        print(f"The Result is {num1 - num2}")
    elif operation.lower() == "m":
        print(f"The Result is {num1 * num2}")
    elif operation.lower() == "a":
        print(f"The Result is {num1 + num2}")
    else:
        print(f"The Result is {num1 / num2}")        