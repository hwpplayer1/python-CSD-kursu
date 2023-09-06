def foo():
    print('one')
    yield
    print('two')
    yield
    print('three')

try:
    g = foo()
    iterator = iter(g)
    next(iterator)
    next(iterator)
    next(iterator)
except:
    pass
