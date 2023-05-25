def foo(a, b, c, d, e, f):
    print('a = {}, b = {}, c = {}, d = {}, e = {}, f = {}'.format(a, b, c, d, e, f))


foo(10, 20, *[40], **{'d':100}, **{'e':200, 'f': 300})
