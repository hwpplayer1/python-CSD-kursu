x = 10

def foo():
    def bar():
        #nonlocal x                #error!
        #print(x)
        x = 20
        print(x)
    bar()

foo()
