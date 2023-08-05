class bar:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print('araya giren kod')
        self.f(*args, **kwargs)

class Sample:
    def __init__(self, a):
        self.a = a

    @bar
    def foo(self):
        print(self.a)
    # foo = bar(foo)

s = Sample(10)
s.foo()                 # Sample.foo(s, 10)
