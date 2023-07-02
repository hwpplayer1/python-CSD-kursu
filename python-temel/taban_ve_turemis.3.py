class A:
    def foo(self):
        print('A.foo')

class B(A):
    def foo(self):
        print('B.foo')

b = B()
A.foo(b)                    # A.foo çağrılır
super(B, b).foo()           # A.foo çağrılır
