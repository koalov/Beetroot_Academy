"""Write a Python program to detect the number of local variables declared in a
function."""


def hello():
    first_string = 'Hello Everyone!'
    second_string = 'How are You doing?'
    third_string = "Is everything is OK?"
    fourth_string = "All right, all looks well!"
    print(first_string, second_string)
    print(third_string, fourth_string)


print(f'There are {hello.__code__.co_nlocals} variable(s) in the "{hello.__name__}" '
      f'function')
