x = 10
y = 20

def foo():
    print('foo')

g = globals()

val = g['x']
print(val)

val = g['y']
print(val)

val = g['foo']
print(val)
