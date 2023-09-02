def __next__(self):
    if self.count == self.stop:
        raise StopIteration
    self.count += 1
    return self.count - 1
