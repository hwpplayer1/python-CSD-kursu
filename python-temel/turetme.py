class A:
    def foo(self):
        print('foo')

    def bar(self):
        print('bar')

class B(A):
    def tar(self):
        print('tar')

b = B()
b.foo()
b.bar()
b.tar()
