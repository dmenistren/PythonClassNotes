
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
