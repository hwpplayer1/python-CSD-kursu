def foo():
    x = yield 10
    print(x)
    x = yield 20
    print(x)
    x = yield 30
    print(x)

iterator = foo()

try:
    val = next(iterator)
    val = iterator.send(val * val)
    val = iterator.send(val * val)
    iterator.send(val * val)
except StopIteration:
    pass

    