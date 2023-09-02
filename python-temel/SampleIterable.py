class SampleIterable:
    def __init__(self, *args):
        self.args = args
    def __iter__(self):
        return SampleIterator(self.args)

class SampleIterator:
    def __init__(self, args):
        self.args = args
        self.index = 0

    def __next__(self):
        self.index += 1
        if self.index > len(self.args):
            raise StopIteration
        return self.args[self.index - 1]

s = SampleIterable(10, 20, 30)

for x in s:
    print(x, end=' ')
print()
