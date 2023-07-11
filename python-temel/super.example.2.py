class A:
    def foo(self):
        print('A.foo')

class B(A):
    def foo(self):
        print('B.foo')
        super().foo()

class C(B):
    def foo(self):
        print('C.foo')
        super().foo()

c = C()
c.foo()
