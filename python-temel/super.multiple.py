class A:
    def foo(self):
        print('A.foo')

class B(A):
    def foo(self):
        print('B.foo')
        super().foo()

class C(A):
    def foo(self):
        print('C.foo')
        super().foo()

class D(B, C):
    def foo(self):
        print('D.foo')
        super().foo()

print(D.__mro__)
d = D()
d.foo()
