"""
Make a program that has some sentence (a string) on input and returns a dict containing
all unique words as keys and the number of occurrences as values.
"""
user_string = list(input("Enter a sting: ").split(" "))
final_dict = {}
for i in user_string:
    if i not in final_dict.keys():
        current_var = {i: user_string.count(i)}
        final_dict.update(current_var)
print(final_dict)

