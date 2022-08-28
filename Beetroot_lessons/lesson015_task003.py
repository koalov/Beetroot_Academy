"""Fraction

Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для
дробів (+, -, /, *) з належною перевіркою й обробкою помилок. Потрібно додати
магічні методи для математичних операцій та операції порівняння між об'єктами
класу Fraction"""


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Denominator must be not equal to zero!")
        elif type(numerator) or type(denominator) not in [int or float]:
            raise ValueError("All parameters should be an int or float numbers!")
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        print("\u0332".join(f'{self.numerator}  '), f'\n{self.denominator}\n')

    @staticmethod
    def print_fraction(a, b):
        print("\u0332".join(f'{a}  '), f'\n{b}\n')
        if a > b or Fraction.get_nod(a, b) > 1:
            a, b = Fraction.get_reduce(a, b)
            if a % b == 0:
                print(a // b, "\n")

    @staticmethod
    def get_nod(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    @staticmethod
    def get_common_denominator(a, b):
        if a == b:
            return a
        elif a % b == 0:
            return a
        elif b % a == 0:
            return b
        else:
            return a * b

    @staticmethod
    def get_reduce(a, b):
        nod = Fraction.get_nod(a, b)
        if nod != 1:
            a //= nod
            b //= nod
        return a, b

    def __add__(self, other):
        # getting common denominator
        common = Fraction.get_common_denominator(self.denominator, other.denominator)
        # if both denominators are equal:
        if self.denominator == other.denominator:
            res_denominator = self.denominator
            res_numerator = self.numerator + other.numerator
            return self.print_fraction(res_numerator, res_denominator)
        # if first denominator greater than other and equal to common denominator
        elif other.denominator < self.denominator == common:
            res_denominator = common
            res_numerator = (other.numerator * (common // other.denominator) +
                             self.numerator)
            return self.print_fraction(res_numerator, res_denominator)
        # if first denominator less than other and other is equal to common denominator
        elif self.denominator < other.denominator == common:
            res_denominator = common
            res_numerator = (self.numerator * (common // self.denominator) +
                             other.numerator)
            return self.print_fraction(res_numerator, res_denominator)

    def __sub__(self, other):
        # getting common denominator
        common = Fraction.get_common_denominator(self.denominator, other.denominator)
        # if both denominators are equal:
        if self.denominator == other.denominator:
            res_denominator = self.denominator
            res_numerator = self.numerator - other.numerator
            return self.print_fraction(res_numerator, res_denominator)
        # if first denominator greater than other and equal to common denominator
        elif other.denominator < self.denominator == common:
            res_denominator = common
            res_numerator = (other.numerator * (common // other.denominator) -
                             self.numerator)
            return self.print_fraction(res_numerator, res_denominator)
        # if first denominator less than other and other is equal to common denominator
        elif self.denominator < other.denominator == common:
            res_denominator = common
            res_numerator = (self.numerator * (common // self.denominator) -
                             other.numerator)
            return self.print_fraction(res_numerator, res_denominator)

    def __mul__(self, other):
        res_numerator = self.numerator * other.numerator
        res_denominator = self.denominator * other.denominator
        return self.print_fraction(res_numerator, res_denominator)

    def __truediv__(self, other):
        # getting second fraction reversed
        other.numerator, other.denominator = other.denominator, other.numerator
        # perform multiplication with resulted fractions
        res_numerator = self.numerator * other.numerator
        res_denominator = self.denominator * other.denominator
        return self.print_fraction(res_numerator, res_denominator)


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    Fraction(3, 4) == x + y
    x - y
    x * y
    x / y
    x.__repr__()
    y.__repr__()
