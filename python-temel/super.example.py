class A:
    def foo(self):
        print('A.foo')

class B(A):
    def foo(self):
        print('B.foo')

class C(A):
    def foo(self):
        print('C.foo')

class D(B, C):
    def foo(self):
        print('D.foo')
        super(C, self).foo()              # A.foo çağrılacak

print(D.__mro__)
d = D()
d.foo()
