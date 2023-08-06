def foo(c):
    def g(*args, **kwargs):
        print('g')
        return c(*args, **kwargs)
    return g

@foo
class Sample:
    def __init__(self, a, b):
        print('Sample instance created')
        self.a = a
        self.b = b

# Sample = foo(Sample)

s = Sample(10, 20)

print(s.a, s.b)
