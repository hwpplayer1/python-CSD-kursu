def foo():
    print('foo begins')
    def bar():
        print('bar begins')
        print('bar ends')
        bar()
        print('foo ends')
foo()
