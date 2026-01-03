

def hanlde_value(a):
    return a-21


a = [1, 2, 3, 4]

print(list(map(hanlde_value, a)))



"""
Two types of scope 
1. Local scope
2. global scope
"""


def name():
    print(a)


a = 10
print(a)
name()
