def foo(a, b = 100, c = 200):
    print('a = ', a, 'b = ', b, 'c = ', c)

foo(1)                   # foo(1, 100, 200)
foo(1, 2)                # foo(1, 2, 200)
foo(1, 2, 3)             # foo(1, 2, 3)



