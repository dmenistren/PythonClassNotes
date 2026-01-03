# raise ValueError(/"asdasd")


def name(val):
    if val == 'test':
        raise ValueError(val)
    print(val)


try:
    name('test')
except ValueError:
    print("value must be test")
except Exception as err:
    print(err)
