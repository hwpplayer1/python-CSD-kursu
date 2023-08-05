def bar(f):
    def g(*args, **kwargs):
        print('araya girilen kod')
        f(*args, **kwargs)

    return g

class Sample:
    def __init__(self, a):
        self.a = a

    @bar
    def foo(self):
        print(self.a)
    # foo = bar(foo)

s = Sample(10)
s.foo                 # Sample.foo(s, 10)
