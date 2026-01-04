Reference Document: https://www.geeksforgeeks.org/python/file-handling-python/

### File Reading Syntax

```python
file = open(filename, mode)
```

### Modes:

- r - Read a file
- w - Write a file
- a - Append a File
- R+ - Read + Write

### Read a File

```python
try:
    file = None
    file = open('demo.txt')
    print(file.read())
except Exception as err:
    print(err)
finally:
    if file:
        file.close()
 # or
 
 try:
    file = None
    file = open('demo.txt','r')
    print(file.read())
except Exception as err:
    print(err)
finally:
    if file:
        file.close()
 
```

### Write a File

```python
try:
    file = None
    file = open('demo2.txt', 'w') # create a file if not exisit
    file.write("hello world")
except Exception as err:
    print(err)
finally:
    if file:
        file.close()

```

### Append a File

```python
try:
    file = None
    file = open('demo3.txt', 'a')
    file.write("hello world")
except Exception as err:
    print(err)
finally:
    if file:
        file.close()
```

## Read and write a file

```python

try:
    file = None
    file = open('demo3.txt', 'r+')
    file.write("hello asdas")
    print(file.read())
except Exception as err:
    print(err)
finally:
    if file:
        file.close()

```