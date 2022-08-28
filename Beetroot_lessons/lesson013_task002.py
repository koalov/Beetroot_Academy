"""Doggy age

Create a class Dog with class attribute `age_factor` equals to 7. Make __init__()
which takes values for a dog’s age. Then create a method `human_age` which returns
the dog’s age in human equivalent."""


class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        print(f"This dog have {self.dog_age * Dog.age_factor} "
              f"years in human equivalent")


fluffy = Dog(7)
fluffy.human_age()
