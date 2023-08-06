def foo(c):
    def bar():
        print('bar')
        return c()
    return bar

@foo
class Sample:
    def disp(self):
        print('disp')

# Sample = foo(Sample)

s = Sample()
s.disp()
