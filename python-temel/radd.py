class Sample:
    def __init__(self, a):
        self.a = a

    def __add__(self, s):
        if isinstance(s, Sample):
            return Sample(self.a + s.s)
        if isinstance(s, int):
            return Sample(self.a + s)

    def __radd__(self, a):
        return self.a + a

    def __str__(self):
        return str(self.a)

a = 10
s = Sample(10)

result = s + a           # s.__add__(a)
print(result)

result = a + s           # s.__radd__(a)
print(result)
