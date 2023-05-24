def foo(a, b, *c):
    print('a = {}, b = {}, c = {}'.format(a, b, c))
l = [10, 20, 30, 40, 50]
foo(10, 20, *l)