def foo():
    x = 10
    def bar():
        x = 20                   # yeni bir x
        print(x)
    bar()
    print(x)

foo()
