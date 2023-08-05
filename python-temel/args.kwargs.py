class foo:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print('araya giren kod')
        self.f(*args, **kwargs)

@foo
def bar(a, b, c):
    print(f'foo: {a}, {b}, {c}')

# foo = bar(foo)

bar(1, 2, 3)
bar(4, 5, 6)
