import math

class SqrtIterable:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return SqrtIterator(self.limit)

class SqrtIterator:
    def __init__(self, limit):
        self.limit = limit
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.limit:
            raise StopIteration()
        self.i += 1

        return math.sqrt(self.i)

s = SqrtIterable(25)

for f in s:
    print(f)

l = list(SqrtIterable(100))

for f in l:
    print(f)
print()
