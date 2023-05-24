def foo(*a, b):
    print('a = {}, b = {}'.format(a, b))

foo(10, b = 100)                       # a = (10,), b = 100
foo(10, 20, b = 100)                   # (10, 20), b = 100
foo(10, 20, b = 100)                   # (10, 20), b = 100
#foo(10, 20, 30)                        # geçerli değil! b değer almamış
