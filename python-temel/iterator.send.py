def foo():
    x = yield
    print(x)
    x = yield
    print(x)
    x = yield
    print(x)

iterator = foo()

try:
    next(iterator)
    iterator.send(10)
    iterator.send(20)
    iterator.send(30)
except StopIteration:
    pass
