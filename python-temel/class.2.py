class Sample:
    def foo(self):
        print('foo')

def b(self):
    print('bar')

Sample.bar = b

s = Sample()
s.foo()
s.bar()
