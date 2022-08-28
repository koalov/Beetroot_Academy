# If I correctly understood the task requirements:


def calculation():
    try:
        a = int(input('Enter a first integer: '))
        b = int(input('Enter a second integer: '))
        c = a * a / b
        return print(c)
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except ValueError:
        print('Values should be an integer type')


calculation()

# ====================================================================================
# Another version  of task realisation (should give an ValueError if incorrect input
# happen, regardless try/except statement, where ValueError is also excepted):


def calculation_1(a, b):
    try:
        c = a * a / b
        return print(c)
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except ValueError:
        print('Values should be an integer type')


first = int(input('Enter a first integer: '))
second = int(input('Enter a second integer: '))
calculation_1(first, second)

# ====================================================================================
# And another version of task, where try/except block is outside the function,
# and just checking if all the values have correct type to continue, and calls
# function only if no errors happen using "else:" construction for this.


def calculation_2(a, b):
    c = a * a / b
    return print(c)


first, second = 0, 0
try:
    first = int(input('Enter a first integer: '))
    second = int(input('Enter a second integer: '))
    if second == 0:
        raise ZeroDivisionError
except ValueError:
    print('Values should be an integer type')
except ZeroDivisionError:
    print('Cannot divide by zero')
else:
    calculation_2(first, second)
