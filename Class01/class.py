'''
This is a sample python file
that prints hello world
to the console.
'''

"""
This is a sample python file
that prints hello world
to the console.
"""

# this is print statement used to print the hello world
# Ctrl + / to comment or uncomment the line
print("hello world")


# Integers
a = -10
print(a)
print(type(a))

# float
b = -10.5
print(b)
print(type(b))

# complex
c = 2 + 3j
print(c)
print(type(c))


# String
d = "Hello, 'Python!"
d = 'Hello, "Python!'
print(d)
print(type(d))

Multiline_string = '''This is a multiline string.
It can span multiple lines.
You can use triple quotes for this.'''
print(Multiline_string)
print(type(Multiline_string))

# Boolean
e = True
print(e)
print(type(e))

f = False
print(f)
print(type(f))


# Type casting
z = 10.26
z = round(z)
print(z)
print(type(z))

z = 20
print(str(z))
print(type(str(z)))

# keywords
# int,float,str,bool,list,tuple,set,dict,round,complex


# List
my_list = [1, 2.5, 'Hello', True, 3 + 4j, 'Hello']  # []
print(my_list)
print(type(my_list))

# Tuple
my_tuple = (1, 2.5, 'Hello', True, 3 + 4j, 'Hello', [2, 3])  # ()
print(my_tuple)
print(type(my_tuple))

# Set
my_set = {2.5, 'Hello', False, 3 + 4j, 0, 'Hello'}  # {}

print(my_set)
print(type(my_set))

# binary
"""
    0 - False
    1 - True
"""

# Dictionary
my_dict = {
    'name': 'John',
    'age': 30,
    'is_student': False,
    'marks': [85, 90, 78],
    'address': {
        'city': 'New York',
        'zip': '10001'
    }
}  # {}
print(my_dict)
print(type(my_dict))

# None
my_var = None
print(my_var)
print(type(my_var))
