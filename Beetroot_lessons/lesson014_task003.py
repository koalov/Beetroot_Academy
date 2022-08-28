"""Product Store
Write a class Product that has three attributes:
type
name
price
Then create a class ProductStore, which will have some Products and will operate with
all products in the store. All methods, in case they can’t perform its action, should
raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class.
You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:
add(product, amount) - adds a specified quantity of a single product with a predefined
    price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all
    products specified by input identifiers (type or name). The discount must be
    specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the
    store if available, in other case raises an error. It also increments income if
    the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items
    in the store.

class Product:
    pass

class ProductStore:
    pass

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product(Food, 'Ramen, 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell(‘Ramen’, 10)

assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)
"""


class Product:
    def __init__(self, _type, name, price):
        self.type = _type
        self.name = name
        self.price = price
        self.amount = None
        self.percent = None
        self.discount = None


class ProductStore:
    discount = 1.0
    earned_amount = 0

    def __init__(self):
        self.product = Product
        self.products = []

    def add(self, product, amount):
        """adds a specified quantity of a single product with a predefined price
        premium for your store(30 percent)"""
        if type(amount) != int or amount < 1:
            raise ValueError("Amount of product is not integer type or less than 1")
        self.product = product
        self.product.amount = amount
        self.product.price *= 1.3
        self.products.append(self.product)

    def set_discount(self, identifier, percent, identifier_type='name'):
        """adds a discount for all products specified by input identifiers (type or
        # name). The discount must be specified in percentage"""
        percent = int(percent.replace('%', ''))
        if percent < 0:
            raise ValueError("Percent parameter should be positive or equal to zero")
        for item in self.products:
            if ((item.name == identifier and identifier_type == 'name') or
                    (item.type == identifier and identifier_type == 'type')):
                item.price *= 1 - (percent / 100)

    def sell_product(self, product_name, amount):
        """removes a particular amount of products from the store if available,
        in other case raises an error. It also increments income if the sell_product
        method succeeds."""
        if type(amount) != int or amount < 1:
            raise ValueError("Amount of product is not integer type or less than 1")
        for item in self.products:
            if item.name == product_name:
                item.amount -= amount
                ProductStore.earned_amount += item.price * amount

    def get_income(self):
        """returns amount of money earned by ProductStore instance."""
        return round(ProductStore.earned_amount, 3)

    def get_all_products(self):
        """returns information about all available products in the store."""
        for product in self.products:
            print(f'{"=" * 50}\n'
                  f'Product name: => {product.name}\n'
                  f'Product category: => {product.type}\n'
                  f'Product price: => {round(product.price, 3)}\n'
                  f'Products amount: => {product.amount}\n\n'
                  f'{"=" * 50}\n')

    def get_product_info(self, product_name):
        """Returns a tuple with product name and amount of items in the store."""
        info = []
        for item in self.products:
            if item.name == product_name:
                info.append(item.name)
                info.append(item.amount)
                return tuple(info)


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
print(s.get_product_info('Ramen'))
s.set_discount('Ramen', "15%", "name")
s.set_discount('Sport', "18%", 'type')
print(round(p2.price, 3))
print(round(p.price, 3))
print(s.get_income())
s.get_all_products()
