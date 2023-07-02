class A:
    def foo(self):
        print('A.foo')

class B(A):
    def foo(self):
        print('B.foo')

a = A()
a.foo()                     # A.foo çağrılır

b = B()
b.foo()                     # B.foo çağrılır
