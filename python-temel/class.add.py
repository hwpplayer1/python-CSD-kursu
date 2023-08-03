class Number:
    def __init__(self, val):
        self.val = val

    def __add__(self, x):
        return Number(self.val + x.val)

    def __iadd__(self, x):
        return Number(self.val + x.val + 1)

    def __repr__(self):
        return str(self.val)

a = Number(10)
b = Number(20)

a = a + b
print(a)

a = Number(10)
b = Number(20)

a += b
print(a)
