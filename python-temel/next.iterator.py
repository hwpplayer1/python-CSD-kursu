def foo():
    x = yield
    print(x)

try:
    iterator = foo()
    val = next(iterator)            # val = iterator.send(None)
    print(val)
    next(iterator)                  # iterator.send(None)
except StopIteration:
    pass
