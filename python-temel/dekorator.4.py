def foo(f):
    def g():
        print('araya girilen kod')
        f()

    return g

@foo
def bar():
    print('bar')

bar()
bar()
