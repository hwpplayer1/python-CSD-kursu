class Sample:
    def __init__(self):
        self.a = 10
        self.b = 20

s = Sample()
print(s.a, s.b)                       # 10, 20

s.a = 100
s.b = 200
print(s.a, s.b)                       # 100, 200
