def bar():
    print('Global bar')

def foo():
    def bar():
        print('Nested bar')
    bar()

foo()
bar()
