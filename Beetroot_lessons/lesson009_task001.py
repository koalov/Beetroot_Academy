def oops():
    raise IndexError


def another_function():
    try:
        oops()
    except KeyError:
        print('This is a KeyError!')


another_function()
