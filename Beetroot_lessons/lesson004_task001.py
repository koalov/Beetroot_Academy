"""The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user
guess what number was generated. The result should be sent back to the user via a
print statement."""
import random
while True:
    user_number = input('Enter an integer from "1" to "10" or "q" to exit: ')
    if user_number == 'q':
        print('See You later! Bye!')
        break
    elif not 0 < int(user_number) <= 10 and not user_number.isdigit():
        print('Number should be integer from "1" to "10"! Try again!')
        continue
    elif 0 < int(user_number) <= 10:
        comp_number = random.randint(1, 10)
        if int(user_number) == comp_number:
            print(f"Yoouh! You guess the number! Computer has been guess "
                  f"{comp_number} too!")
            continue
        else:
            print(f"Oh no! You don't guess! Computer number is {comp_number}. Try "
                  f"again!")
            continue
    else:
        print('Something goes wrong. Try again!')
        continue
