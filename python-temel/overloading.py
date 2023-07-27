class Number:
    def __init__(self, number):
        self.number = number

    def disp(self):
        print(self.number)

    def __add__(self, x):
        return Number(self.number + x.number)

    def __sub__(self, x):
        return Number(self.number - x.number)

    def __mul__(self, x):
        return Number(self.number * x.number)

    def __truediv__(self, x):
        return Number(self.number / x.number)

    def __str__(self):
        return str(self.number)

x = Number(10)
y = Number(20)
z = Number(2)

k = x + y * z
print(k)
