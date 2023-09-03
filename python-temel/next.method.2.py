import math

class SqrtIterable:
    def __init__(self, limit):
        self._limit = limit

    def __iter__(self):
        return SqrtIterator(self._limit)

class SqrtIterator:
    def __init__(self, limit):
        self._limit = limit
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i == self._limit:
            raise StopIteration()
        self._i += 1

        return self._i, math.sqrt(self._i)

si = SqrtIterable(25)

for t in si:
    print(t, end = ' ')
print()

for i, x in si:
    print(f'{i} --> {x}')
