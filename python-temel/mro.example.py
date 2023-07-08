class A:
    def foo(self):
        print('A.foo')


class B(A):
    def foo(self):
        print('B.foo')


class C(B):
    pass

c = C()

c.foo()                 # B.foo
