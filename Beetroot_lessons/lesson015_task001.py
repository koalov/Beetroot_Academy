"""Method overloading.

Create a base class named Animal with a method called talk and then create two
subclasses: Dog and Cat, and make their own implementation of the method talk
be different. For instance, Dog’s can be to print ‘woof woof’, while Cat’s can
be to print ‘meow’.

Also, create a simple generic function, which takes as input instance of a Cat
or Dog classes and performs talk method on input parameter."""


class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print('woof woof')


class Cat(Animal):
    def talk(self):
        print('meow')


def pets(name, _class):
    name = _class()
    name.talk()


name1 = input("Input any dog's name: ")
name2 = input("Input any cat's name: ")
pets(name1, Dog)
pets(name2, Cat)
