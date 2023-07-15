class Sample:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return 'Sample object, value = {}'.format(self.val)

s = Sample(100)
print(s)
