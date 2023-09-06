def foo():
    print('one')
    yield 1
    print('two')
    yield 2
    print('three')
    yield 3

for i in foo():
    print(i)

l = list(foo())
print(l)
