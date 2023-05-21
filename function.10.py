def foo():
    print('foo')

def bar():
    print('bar')

def tar():
    print('tar')

d = {1: foo, 2: bar, 3: tar}

d[1]()
d[2]()
d[3]()
