"""
Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

Create a function which takes as input two dicts with structure mentioned above, then
computes and returns the total price of stock."""
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = []
for key in stock:
    total_price.append(stock[key] * prices[key])
print(int(sum(total_price)))


def final_price(x, y):
    price = 0
    for i in x:
        price += (x[i] * y[i])
    return price


print(final_price(stock, prices))


