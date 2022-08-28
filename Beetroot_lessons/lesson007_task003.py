"""A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as
a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an
arbitrary number of arguments (only numbers) as the second parameter. Then return the
sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  """


def make_operation(operator, *args):
    if operator not in ['+', '-', '*']:
        return print("You don't enter any arithmetic operator ('+', '-' or '*')")
    elif operator == '+':
        summa = 0
        for num in args:
            summa += num
        return summa
    elif operator == '-':
        difference = args[0] * 2
        for num in args:
            difference -= num
        return difference
    elif operator == '*':
        multiplication = 1
        for num in args:
            multiplication *= num
        return multiplication
    else:
        return print("I dont understand. What should it be?")


test1 = make_operation('+', 7, 7, 2)
test2 = make_operation('-', 5, 5, -10, -20)
test3 = make_operation('*', 7, 6)

print(test1)
print(test2)
print(test3)
