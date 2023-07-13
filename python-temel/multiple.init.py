class A:
    def __init__(self, a):
        self.a = a
        print('A.__init__')

class B(A):
    def __init__(self, b, **args):
        super().__init__(**args)
        self.b = b
        print('B.__init__')

class C(A):
    def __init__(self, c, **args):
        super().__init__(**args)
        self.c = c
        print('C.__init__')

class D(B, C):
    def __init__(self, d, **args):
        super().__init__(**args)
        self.d = d
        print('D.__init__')

print(D.__mro__)
d = D(10, a = 20, b = 30, c = 40)
print(d.a, d.b, d.c, d.d)             # 20 30 40 10
