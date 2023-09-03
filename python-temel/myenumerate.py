class myenumerate:
    def __init__(self, iterable):
        self._iterator = iter(iterable)

    def __iter__(self):
        return myenumerate_iterator(self._iterator)

class myenumerate_iterator:
    def __init__(self, iterator):
        self._iterator = iterator
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        return self._index - 1, self._iterator.__next__()

a = [10, 20, 30, 40, 50]

for index, val in myenumerate(a):
    print(index, '=>', val)
