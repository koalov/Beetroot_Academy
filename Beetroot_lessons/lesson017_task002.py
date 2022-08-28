"""Task 2

Create your own implementation of a built-in function range, named in_range(), which
takes three parameters: `start`, `end`, and optional step. Tips: See the documentation
for `range` function"""


class in_range:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        a = self.start
        b = self.end
        if self.step == 0:
            raise ValueError("Only start or end parameters can be equal to zero (0).")
        elif self.start == self.end == 0:
            raise StopIteration
        elif ((self.start > self.end and self.step > 0) or
              (self.start < self.end and self.step < 0)):
            raise ValueError("Such kind of iteration does not have sense.")
        elif self.start > self.end:
            while a > b:
                yield a
                a += self.step
        elif self.start < self.end:
            while a < b:
                yield a
                a += self.step

    def __next__(self):
        return self


for i in in_range(-50, 51, 2):
    print(i)
