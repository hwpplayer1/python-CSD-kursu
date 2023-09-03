class SampleIterable:
    def __init__(self, *args):
        self._args = args

    def __iter__(self):
        return SampleIterator(self._args)

    def __reversed__(self):
        return SampleReverseIterator(self._args)

class SampleIterator:
    def __init__(self, args):
        self._args = args
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i == len(self._args):
            raise StopIteration
        self._i += 1

        return self._args[self._i - 1]

class SampleReverseIterator:
    def __init__(self, args):
        self._args = args
        self._i = len(self._args) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < 0:
            raise StopIteration
        self._i -= 1

        return self._args[self._i + 1]

for i in SampleIterable(1, 2, 3, 4, 5):
    print(i, end = ' ')
print()

for i in reversed(SampleIterable(1, 2, 3, 4, 5)):
    print(i, end = ' ')
print()
