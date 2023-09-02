class MySimpleRange:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        return MySimpleRangeIterator(self.stop)

class MySimpleRangeIterator:
    def __init__(self, stop):
        self.stop = stop
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.stop:
            raise StopIteration
        return self.count - 1
