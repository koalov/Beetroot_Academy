"""Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the
list that are divisible by 7 but not a multiple of 5, and store them in a separate list.
Finally, print the list.

Constraint: use only while loop for iteration"""
list_1 = []
list_2 = []
i = 1
while i <= 100:
    list_1.append(i)
    if i % 7 == 0 and not i % 5 == 0:
        list_2.append(i)
    i += 1

print(list_2)
