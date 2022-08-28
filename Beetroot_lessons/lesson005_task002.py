"""Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a
third list containing the common integers between the 2 initial lists without any
duplicates.

Constraints: use only while loop and random module to generate numbers"""
import random
list_1 = []
list_2 = []
list_3 = []
i = 0

while i < 10:
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))
    i += 1
i = 0
while i < len(list_1):
    if list_1[i] in list_2 and list_1[i] not in list_3:
        list_3.append(list_1[i])
    elif list_2[i] in list_1 and list_2[i] not in list_3:
        list_3.append(list_2[i])
    i += 1
print(list_3)