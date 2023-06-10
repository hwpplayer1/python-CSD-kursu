def foo():
    y = 20

    def bar():
        z = 30
        d = locals()
        print(d)

    d = locals()
    print(d)

    bar()

foo()
