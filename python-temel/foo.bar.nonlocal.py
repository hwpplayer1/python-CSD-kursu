def foo():
    x = 10
    def bar():
        nonlocal x                       # foo'daki x
        x = 20
        def tar():
            nonlocal x                   # bar'daki x
            x = 30                       
        tar()
    bar()
    print(x)                             # 30
foo()
