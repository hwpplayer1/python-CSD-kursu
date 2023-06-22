class Sample:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def foo(k):
    print(k.a, k.b)                  # 10 20
    k.a = 100
    k.b = 200

s = Sample(10, 20)
print(s.a, s.b)                      # 10 20
foo(s)
print(s.a, s.b)                      # 100 200
