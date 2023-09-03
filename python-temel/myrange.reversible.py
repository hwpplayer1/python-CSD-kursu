class myrange:
    def __init__(self, start, stop = None, step = 1):
        if stop == None:
            self._start = 0
            self._stop = start
        else:
            self._start = start
            self._stop = stop
        self._step = step

    def __iter__(self):
        return myrange_iterator(self)

    def __reversed__(self):
        return myrange_reverse_iterator(self)

class myrange_iterator:
    def __init__(self, mr):
        self._mr = mr
        self._i = mr._start

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= self._mr._stop:
            raise StopIteration
        self._i += self._mr._step

        return self._i - self._mr._step

class myrange_reverse_iterator:
    def __init__(self, mr):
        self._mr = mr
        self._i = mr._stop

    def __iter__(self):
        return self

    def __next__(self):
        if self._i <= self._mr._start:
            raise StopIteration
        self._i -= self._mr._step
        return self._i

for i in myrange(10):
    print(i, end = ' ')
print()

for i in reversed(range(10)):
    print(i, end = ' ')
print()
