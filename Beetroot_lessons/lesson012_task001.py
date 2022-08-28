"""Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!

For example:
"add called with 4, 5"

def logger(func):
    pass

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]"""

from functools import wraps


def logger(func):
    @wraps(func)
    def print_func(*args):
        arguments = ", ".join([repr(a) for a in args])
        print(f'{func.__name__}({arguments})')
    return print_func


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


if __name__ == "__main__":
    add(4, 5)
    square_all(4, 6, 8, 9, 2)
