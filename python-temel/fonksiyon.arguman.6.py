def foo(a, b, c, d, e, f):
    print('a = {}, b = {}, c = {}, d = {}, e = {}, f = {}'.format(a, b, c, d, e, f))

foo(10, e=50, *(30, 40), **{'d':100, 'f': 200})
