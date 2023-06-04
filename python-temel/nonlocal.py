def foo():
    x = 10
    def bar():
        nonlocal x
        print(x)                       # foo'daki x
        x = 20                         # foo'daki x
        print(x)                       # foo'daki x
    bar()
    print(x)

foo()
