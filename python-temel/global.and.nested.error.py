def bar():
    print('Global bar')

def foo():
    #bar()                   #error
    def bar():
        print('Nested bar')
    bar()

foo()
