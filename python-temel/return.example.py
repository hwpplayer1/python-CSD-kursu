def foo(a):
    x = a
    def bar():
        print(x)
    return bar

f = foo(10)
f()
foo(20)
f()
