# Decorator
import time


def check_time(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
    return wrapper


@check_time
def print_value(a):
    # start = time.time()
    for i in range(a):
        print("Hello")
        time.sleep(1)
 

@check_time
def print_value2(a):
    for i in range(a):
        print("Hello")


@check_time
def print_value3(a):
    for i in range(a):
        print("Hello")


@check_time
def print_value4(a):
    for i in range(a):
        print("Hello")


@check_time
def print_value5(a):
    for i in range(a):
        print("Hello")


print_value(3)
