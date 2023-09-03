import random

class RandIterable:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __iter__(self):
        return RandIterator(self)

class RandIterator:
    def __init__(self, ri):
        self.ri = ri
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.ri.c:
            raise StopIteration
        self.count += 1

        return random.randint(self.ri.a, self.ri.b)

a = list(RandIterable(10, 20, 5))
print(a)

for x in RandIterable(0, 100, 10):
    print(x, end=' ')
print()

try:
    ri = RandIterable(0, 100, 10)
    iterator = iter(ri)                  # iterator = ri.__iter__()
    while True:
        x = next(iterator)               # iterator.__next__()
        print(x, end=' ')
    print()
except:
    pass

    
