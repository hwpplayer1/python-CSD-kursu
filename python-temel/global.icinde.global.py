x = 10
def foo():
    global x
    x = 20
    def bar():
        global x
        x = 30
    bar()

foo()
print(x)
