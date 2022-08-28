class Laptop:

    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin

    def display_private_attrs(self):
        for attr in self.__dict__:
            if attr.startswith(f'_{self.__class__.__name__}__'):
                print(attr)

    def display_protected_attrs(self):
        for attr in self.__dict__:
            if attr.startswith(f"_") and \
                    not attr.startswith(f"_{self.__class__.__name__}__"):
                print(attr)


laptop = Laptop('Acer', 'Predator', 'AC-100', 5490, 0.2)
laptop.display_private_attrs()
laptop.display_protected_attrs()


class Laptop:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price
        return self.__price


laptop = Laptop(3499)
print(laptop.get_price())
laptop.set_price(3999)
print(laptop.get_price())


class Laptop:

    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        if not isinstance(value, int or float):
            raise TypeError('The price attribute must be an int or float type.')
        elif value < 0:
            raise ValueError(
                'The price attribute must be a positive int or float value.')
        self._price = value


laptop = Laptop(3499)
try:
    laptop.set_price('-3000')
except ValueError as error:
    print(error)
