def foo(f):
    print('foo')

    def g(*args, **kwargs):
        print('g')
        f(*args, **kwargs)

    return g

@foo
def bar(a, b, c, **kwargs):
    print(f'bar: {a}, {b}, {c}, {kwargs}')

bar(10, 20, 30, xx=100, yy=200)
bar(50, 60, 70, zz=300, kk=400)
