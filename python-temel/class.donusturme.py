class Number:
    def __init__(self, val):
        self.val = val

    def __int__(self):
        return int(self.val)

    def __float__(self):
        return float(self.val)

    def __bool__(self):
        return bool(self.val)

    def __complex__(self):
        return complex(self.val)

n = Number(10)

val = int(n)
print(val)

val = float(n)
print(val)

val = bool(n)
print(val)

val = complex(n)
print(val)
