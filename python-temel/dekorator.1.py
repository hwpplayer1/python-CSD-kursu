def foo(f):
    print('foo')
    return f

@foo
def bar():
    print('bar')

# eşdeğeri -> bar = foo(bar)

bar()