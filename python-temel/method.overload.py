class Sample:
    def foo(self):
        print('foo')

def tar(self):
    print('bar')

Sample.bar = tar

s = Sample()
s.foo()
s.bar()

Sample.x = 100
print(Sample.x)
