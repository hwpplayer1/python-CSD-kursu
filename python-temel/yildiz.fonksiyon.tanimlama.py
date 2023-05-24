def foo(a, b, *c, d = 100, e):
    print("a = {}, b = {}, c = {}, d = {}, e = {}".format(a, b, c, d, e))
foo(10, 20, 30, 40, 50, e=60)