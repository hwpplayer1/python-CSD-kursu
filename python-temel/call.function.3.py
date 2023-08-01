class Sample:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x ** self.n


s = Sample(3)
result = map(s, range(10))

for x in result:
    print(x)
