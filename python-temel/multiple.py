class A:
    def foo(self):
        print('foo')

class B:
    def bar(self):
        print('bar')

class C(A, B):
    def tar(self):
        print('tar')

c = C()
c.foo()
c.bar()
c.tar()
