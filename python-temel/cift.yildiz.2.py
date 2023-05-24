def foo(a, b, **c):
    print('a = {}, b = {}, c = {}'.format(a, b, c))
    for key, val in c.items():
        print('{} ---> {}'.format(key, val))

foo(10, 20, ali = 100, veli = 200, selami = 300)
