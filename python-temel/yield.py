def foo():
    print('one')
    yield 1
    print('two')
    yield 2
    print('three')
    yield 3

iterator = foo()

val = iterator.__next__()
print(val)

val = iterator.__next__()
print(val)

val = iterator.__next__()
print(val)
