class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, x):
        if isinstance(x, (int, float)):
            return Number(self.number + x)
        return Number(self.number + x.number)

    def __sub__(self, x):
        if type(x) is int or type(x) is float:
            return Number(self.number - x)
        return Number(self.number - x.number)

    def __mul__(self, x):
        if isinstance(x, (int, float)):
            return Number(self.number * x)
        return Number(self.number * x.number)

    def __truediv__(self, x):
        if isinstance(x, (int, float)):
            return Number(self.number / x)
        return Number(self.number / x.number)

    def __str__(self):
        return str(self.number)


x = Number(10)
y = Number(20)

z = x + y
print(z)

z = x + 10
print(z)
