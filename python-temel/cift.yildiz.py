def foo(a, b, **c):
    print("a = {}, b = {}, c = {}".format(a, b, c))

foo(b = 10, a = 20, xx = 30, yy = 40)
