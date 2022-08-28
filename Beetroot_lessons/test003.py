class Product:
    def __init__(self, name, prise):
        self.name = name
        self.prise = prise


class ProductItem:
    def __init__(self, product, color, size, qtty=1):
        self.product = product
        self.color = color
        self.size = size
        self.qtty = qtty

    def get_products(self):
        for product in self.product:
            print(f"Product name:=>     {self.product.name}, "
                  f"Product color:=>    {product.color}, "
                  f"Product size:=>     {product.size}, "
                  f"Product quantity:=> {product.quantity}, "
                  f"Product price:=>    {product.price}")


class WareHouse:
    def __init__(self):
        self.product = None
        self.products = []

    def add_product(self, product_item):
        self.products.append(product_item)

    def get_products(self):
        return ProductItem.get_products


wh = WareHouse()

sneakers = Product("sneakers", 28.90)

wh.add_product(ProductItem("sneakers", "white", 43, 15))
wh.add_product(ProductItem("sneakers", "black", 42, 15))
wh.add_product(ProductItem("sneakers", "space grey", 41, 15))
wh.add_product(ProductItem("sneakers", "rose gold", 39, 15))

wh.get_products()
