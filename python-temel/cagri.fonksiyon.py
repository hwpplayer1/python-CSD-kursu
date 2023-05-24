def foo(a, b, c, *d):
    print('a = {}, b = {}, c = {}, d = {}'.format(a, b, c, d))
foo(100, *'ankara')