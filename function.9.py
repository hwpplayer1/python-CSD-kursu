def foo():
    print('foo')

def bar():
    print('bar')

def tar():
    print('tar')

a = [foo, bar, tar]

for f in a:
    f()
    
