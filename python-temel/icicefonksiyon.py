def foo():
    val = 10
    print('foo begins')
    def bar():
        print('bar begins')
        print('val = {0}'.format(val))
        print('bar ends')
    bar()
    print('foo ends')

foo()
