def foo(a, b, c, d, e, f):
    print('a = {}, b = {}, c = {}, d = {}, e = {}, f = {}'.format(a, b, c, d, e, f))

foo(10, 20, e = 30, *(40, 50), f = 60)
