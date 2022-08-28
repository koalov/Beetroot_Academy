"""The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. The
program should check that the string contains only numerical characters and is only 10
characters long. Print a suitable message depending on the outcome of the string
evaluation."""

phone = input('Enter a phone number: ')
if len(phone) == 10 and phone.isdigit():
    print('This is correct phone number')
else:
    print("Your input doesn't match the criteria: to be a 10 numbers long, "
          "and all symbols is digits.")