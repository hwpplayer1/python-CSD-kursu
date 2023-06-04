def foo():
    x = 10
    def bar():
        def tar():
            nonlocal x                     # foo'daki x
            x = 20
        tar()
    bar()
    print(x)                               # 20
foo()
