def foreach(l, f):
    for x in l:
        f(x)

def foo(x):
    print('foo: {}'.format(x))


foreach([1, 2, 3, 4, 5], foo)
foreach([1, 2, 3, 4, 5], print)
