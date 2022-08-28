"""The math quiz program.

Write a program that asks the answer for a mathematical expression, checks whether the
user is right or wrong, and then responds with a message accordingly."""

num_1 = 650
num_2 = 50
signs = ['+', '-', '*', '/']
expr = ''
while True:
    while True:
        expr = input(f'Enter the type of expression (i.e.{signs}) or "q" to '
                     'exit: ')
        if expr == 'q':
            print('See You next time! Bye!')
            break
        elif len(expr) > 1 or expr not in signs:
            print(f'Type of expression must be single sign any of {signs}. Try again!')
            continue
        else:
            break
    if expr == 'q':
        break

    print('Can You match the answer of this sentence: ')

    while True:
        answer = 0
        if expr == '*':
            answer = int(input(f'{num_1} * {num_2} = ? '))
            if answer == num_1 * num_2:
                print('Yes! This is correct answer!')
                break
            else:
                print('No, this is wrong answer. Try again!')
        elif expr == '/':
            answer = int(input(f'{num_1} / {num_2} = ? '))
            if answer == num_1 // num_2:
                print('Yes! This is correct answer!')
                break
            else:
                print('No, this is wrong answer. Try again!')
        elif expr == '+':
            answer = int(input(f'{num_1} + {num_2} = ? '))
            if answer == num_1+num_2:
                print('Yes! This is correct answer!')
                break
            else:
                print('No, this is wrong answer. Try again!')
        elif expr == '-':
            answer = int(input(f'{num_1} - {num_2} = ? '))
            if answer == num_1 - num_2:
                print('Yes! This is correct answer!')
                break
            else:
                print('No, this is wrong answer. Try again!')
        elif expr == 'q':
            break
        else:
            print('Something went wrong! Try again!')

