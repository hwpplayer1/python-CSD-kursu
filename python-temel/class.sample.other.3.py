class Sample:
    x = 10
    def __init__(self, x):
        self.x = x

s = Sample(20)
print(s.x)                                  # 20
print(Sample.x)                             # 10
