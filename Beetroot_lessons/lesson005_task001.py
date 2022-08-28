"""The greatest number

Write a Python program to get the largest number from a list of random numbers with the
length of 10

Constraints: use only while loop and random module to generate numbers"""
import random
rand_list = []
i = 0
while i < 10:
    rand_list.append(random.randint(1, 100))
    i += 1

print(max(rand_list))
