def bar():
    print('Global bar')

def foo():
    global bar
    bar()
    def bar():
        print('Nested bar')
    bar()

foo()
bar()
