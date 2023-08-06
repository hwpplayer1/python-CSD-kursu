def foo(c):
    print('foo')
    return c

@foo
class Sample:
    def disp(self):
        print('disp')

# Sample = foo(Sample)

s = Sample()
s.disp()
