x = 10

def foo():
    global x
    x = 20
    def bar():
        #nonlocal x                         # error, x üst fonksiyonda global
        x = 30
    bar()
foo()
print(x)
