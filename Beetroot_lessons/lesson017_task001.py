"""Task 1

Create your own implementation of a built-in function enumerate, named `with_index`,
which takes two parameters: `iterable` and `start`, default is 0. Tips: see the
documentation for the enumerate function"""


def with_index(iterable, start=0):
    n = start
    for element in iterable:
        yield f'{n} => {element}'
        n += 1


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']

enum_months = list(with_index(months, start=1))
print(enum_months)

