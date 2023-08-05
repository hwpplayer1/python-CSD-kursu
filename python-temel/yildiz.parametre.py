def foo(f):
    print('foo')

    def g(*args):
        print('g')
        f(*args)

    return g

@foo
def bar(a, b, c):
    print(f'bar: {a}, {b}, {c}')

bar(10, 20, 30)
bar(50, 60, 70)

