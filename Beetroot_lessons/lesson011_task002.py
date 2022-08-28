"""Write a Python program to access a function inside a function (Tips: use function,
which returns another function)"""


def first_foo(num1):
    def second_foo(num):
        return num1 * num
    return second_foo(num2)


if __name__ == "__main__":
    try:
        value = int(input('Enter a first integer: '))
        num2 = int(input("Enter a second integer: "))
        print(first_foo(value))
    except ValueError:
        print("Value Error, it must be an integer!")
